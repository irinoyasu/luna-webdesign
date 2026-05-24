# Design Story: 人生9割損してるサークル (C班)

_Generated: 2026-05-24_

## Project Context

### Purpose
This website is a group homework project for Musashino Art University students in Group C. The site presents a digital portal for a student club dedicated to sharing ("布教" / preaching) their niche passions (indie games, retro cafes, space science) with fellow students, using a warm, collaborative, and friendly tone.

### Target Audience
University students who are curious about new creative activities, seeking a cozy and accepting community of hobbyists, and wanting to escape the routine of typical study life.

### Key Objectives
1. Introduce the club members and its core principles in an engaging, human way.
2. Provide a tactile and interactive presentation slide viewer that feels physical rather than corporate.
3. Establish a friendly, open-minded chalkboard feedback platform where visitors feel safe to interact.

---

## Design Narrative

### Core Message
"There is a world of 'highest-quality' hidden gems you haven't discovered yet. Don't let your life lose out!" The design tells a story of sharing, warmth, and collective passion, presenting the club as a physical, cozy student journal.

### Emotional Journey
Visitors should feel **welcomed** by the initial splash screen and warm colors, **intrigued** by the quirky members and mascot, **nostalgic** when browsing the CRT TV slides, and **empowered** to submit comments or recommend their own passions.

### Visual Metaphor
The entire site is unified under the metaphor of a **physical student scrapbook/sketchbook**. Grid-pattern paper, tape fragments, Polaroid frames, and hand-written tags make it feel like a tactile book passed around a circle of friends.

---

## User Journey

### Entry Point
- **First Impression**: A royal blue splash screen transitions out to reveal a warm cream graph paper background. A bold neubrutalist title with a solid outline declares: "人生、9割損してる。"
- **Design Choices**: Saturated pop colors contrast against the analog paper grid, creating an immediate visual hook.

### Exploration Phase
- **User Actions**: The user scrolls down, reading the Concept Board. They explore the club members in their Polaroid frames and check the **News/Topics** section for the latest club activities.
- **Design Response**: Cards elevate on hover. Colorful washi tape strips sit on top of the cards, mimicking physical tape. The News section uses a "floating sticky note" layout that feels dynamic and fresh.
- **Micro-Interactions**: Custom tag badges tilt slightly, and icons pop under the cursor.

### Engagement Phase
- **Key Interactions**: Browsing past presentations in the Cozy Photo Album, loading a slide deck, and diving into **Project Detail Pages** for more in-depth content.
- **Visual Feedback**: The slides open inside a mahogany CRT TV screen. Antennas, dials, and a green power LED light up. Detail pages maintain the scrapbook aesthetic with large margins and collage layouts.
- **Storytelling Elements**: Navigating slides turns the channel knobs. Powering off shows static noise. The transition to detail pages feels like turning a page in a physical journal.

### Peak Moment
- **Highlight**: Posting feedback on the dark green Blackboard and seeing the sticky note appear instantly with a random rotational tilt, a colored tape segment, and an offset drop shadow.
- **Technical Implementation**: Dynamically calculated angles and values stored in local storage, rendering custom inline styles.
- **Purpose**: Fully realizes the physical scrapbook metaphor, allowing users to leave their mark.

---

## Thematic Elements & Inspiration

### Visual Theme
A curated blend of three distinct references:
1. **ikiiki-being.com** (いきいきビイング) - Inspired the cute, buoyant illustration style (the green ghost mascot) and the friendly, community-centric exploration path.
2. **gunze.co.jp/130th/** (グンゼ創業130周年記念) - Inspired the self-deprecating yet highly appealing copy style, bold pop headings, and pop-art vector layout.
3. **media.osakastationcity.com** (ドーヤ？ / do-ya?) - Inspired the conversational, dialect-inclusive local charm and interactive widgets (the reaction chalkboard).

### Symbolism
- **Graph Paper Grid**: Represents structural design, homework, and student creativity.
- **Washi Tape**: Represents the temporary, handmade, and collaborative nature of student scrapbooks.
- **CRT Television**: Symbolizes nostalgia, retro gaming, and cozy childhood bedrooms.

---

## Implementation Notes
- **Vanilla CSS**: Maximum layout control without Tailwind, ensuring clean and performant style calculations.
- **SEO & Accessibility**: Semantic HTML5 elements (`<section>`, `<article>`, `<header>`) are used throughout, ensuring screen-reader accessibility and structural compliance.
