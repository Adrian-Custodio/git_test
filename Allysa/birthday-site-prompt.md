# Prompt to paste into Claude

Build me a single-page interactive birthday gift website as one self-contained HTML file (HTML, CSS, and JS all in one file, no external dependencies except Google Fonts if needed). It needs to work well on both mobile phones and desktop/PC (fully responsive).

## Concept
This is a digital birthday card for my girlfriend/crush. The flow is:

1. **Landing / envelope screen** — A cute closed envelope or gift box centered on screen. Tapping/clicking it triggers an opening animation.
2. **Card opens** — After the envelope opens, reveal a short animated birthday greeting (her name, "Happy Birthday", soft fade/scale-in animation, maybe some floating sparkle/leaf particles). Include a button like "Continue" or "I made you something else..." that leads to the quiz.
3. **Quiz intro screen** — A short intro explaining a mini quiz is coming, with a "Start" button.
4. **Quiz question (build ONE for now, but structure the code so more can be added easily)** — Structure all quiz questions as a JavaScript array of question objects, so I can add more later just by adding new objects to the array, e.g.:
   ```js
   const questions = [
     {
       id: 1,
       prompt: "Reyal or Fakeh?",
       choices: [
         { id: "a", image: "placeholder-a.jpg", label: "Reyal" },
         { id: "b", image: "placeholder-b.jpg", label: "Fakeh" }
       ],
       correctChoiceId: "a", // placeholder, I will confirm
       correctExplanation: "Placeholder explanation text for why this is correct.",
       wrongExplanation: "Placeholder explanation text shown when the wrong answer is picked."
     }
     // more question objects will be added here later
   ];
   ```
   For now, just wire up question #1 using placeholder images (simple colored boxes or placeholder.jpg references are fine — I will swap in real photos later) and placeholder explanation text I can edit.

   **Answer choices must be picture-based buttons** (image + short label), not plain text buttons.

5. **Feedback popup** — After she taps an answer:
   - If correct: show a "You're correct!" popup/modal with the `correctExplanation` text.
   - If wrong: show a "Not quite!" popup/modal that reveals the correct answer and shows `wrongExplanation` text.
   - Either way, after closing the popup, move to the next question if one exists, or go to the final page if this was the last question.
6. **Final page** — A heartfelt birthday message page (placeholder text for now, I will write the real message later). Soft fade-in animation, celebratory but warm tone, maybe gentle floating particles again to bookend the intro animation style.

## Visual style
- Main color: **green** (her favorite color) — use a soft sage/mint green as the primary background or accent, paired with a warm cream/off-white for contrast, so it feels soft and cute rather than "forest" or corporate. A small warm accent color (soft gold or blush) is fine for highlights/buttons.
- Overall aesthetic: cute, soft, pleasing to the eyes — rounded corners, gentle shadows, smooth transitions/animations. Not sharp or corporate.
- Typography: a soft cursive/script font for headings and emotional text (e.g. Google Font like "Dancing Script" or "Great Vibes"), paired with a clean readable sans-serif for body text/buttons.
- Include tasteful animation throughout (fade-ins, gentle scale/bounce on buttons, floating particles) but keep it lightweight and smooth, not laggy.

## Technical requirements
- Single HTML file, inline CSS and JS.
- Fully responsive — must look good on both narrow mobile screens and wide desktop screens.
- Structure the quiz questions as a data array (see above) so I can extend it later just by adding entries — do not hardcode question 1's markup separately from how future questions would render; build one reusable render function that works for any question in the array.
- Add clear comments in the code marking where I should: (a) swap in real photos, (b) edit the question text/choices, (c) edit the correct/wrong explanations, (d) edit the final birthday message.
- Keep the code clean and organized so it's easy for me to hand you a new question object later and have you slot it in.

Build this now as a complete, working single HTML file.
