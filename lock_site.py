#!/usr/bin/env python3
"""
lock_site.py -> builds the password-protected index.html

  index.src.html  (your editable copy, NEVER push this)  ->  index.html  (safe to push)

Everything between the SECRET-START and SECRET-END markers in index.src.html
(the letter, quiz, notes and all the code) is encrypted with AES-256-GCM.
The key is derived from the password with PBKDF2-SHA256 (310,000 rounds,
random salt), so the published index.html contains no password and no
plain content -> it can only be opened with the right password.

Usage:
    python3 lock_site.py            # asks for the password (hidden while typing)

Needs the "cryptography" package:
    pip install cryptography        # or: sudo apt install python3-cryptography
"""
import base64, getpass, json, os, re, sys, unicodedata

SRC, OUT = 'index.src.html', 'index.html'
ITERATIONS = 310_000                      # must match nothing else: stored inside index.html
START = re.compile(r'<!-- SECRET-START[^>]*-->\n?')
END = '<!-- SECRET-END -->'

try:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.primitives import hashes
except ImportError:
    sys.exit('Missing package -> run:  pip install cryptography   (or: sudo apt install python3-cryptography)')

def normalise(pw):                        # same as the page: trim + Unicode NFC
    return unicodedata.normalize('NFC', pw.strip())

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src_path, out_path = os.path.join(here, SRC), os.path.join(here, OUT)
    if not os.path.exists(src_path):
        sys.exit(f'{SRC} not found next to this script.')
    html = open(src_path, encoding='utf-8').read()

    m = START.search(html)
    end = html.find(END)
    if not m or end < m.end():
        sys.exit('Could not find the SECRET-START / SECRET-END markers in index.src.html.')
    secret = html[m.end():end]

    pw = normalise(getpass.getpass('New password: '))
    if pw != normalise(getpass.getpass('Type it again: ')):
        sys.exit('Passwords did not match. Nothing was changed.')
    if len(pw) < 4:
        sys.exit('Please use at least 4 characters.')
    if len(pw) < 8:
        print('Note: longer passwords (8+ characters, or a short phrase) are much harder to guess.')

    salt, iv = os.urandom(16), os.urandom(12)                     # fresh random values every time
    key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt,
                     iterations=ITERATIONS).derive(pw.encode('utf-8'))
    ct = AESGCM(key).encrypt(iv, secret.encode('utf-8'), None)     # ciphertext + 16-byte auth tag

    b = lambda x: base64.b64encode(x).decode('ascii')
    payload = json.dumps({'v': 1, 'iter': ITERATIONS, 'salt': b(salt), 'iv': b(iv), 'ct': b(ct)})
    sealed = f'<script id="sealed" type="application/json">{payload}</script>\n'

    out = html[:m.start()] + sealed + html[end + len(END):]
    open(out_path, 'w', encoding='utf-8').write(out)
    print(f'Done -> {OUT} is locked ({len(ct) // 1024} KB encrypted). Push index.html, never index.src.html.')

if __name__ == '__main__':
    main()
