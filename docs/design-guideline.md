# Design Guidelines: 人生9割損してるサークル (C班)

_Generated: 2026-05-24_

## Design Style
The website uses a **Neubrutalist + Playful Pop Scrapbook** style. It combines the cozy, tactile, analog feel of a physical sketchbook page with the vibrant, high-contrast, bold aesthetics of modern digital pop art.

This hybrid visual system is heavily inspired by three reference websites:
1. **ikiiki-being.com** (いきいきビイング) - Pop, illustration-led layout, approachable community-driven tone, and friendly hand-drawn elements.
2. **gunze.co.jp/130th/** (グンゼ創業130周年) - High-energy U-25 target visuals, pop typography, self-deprecating yet engaging storytelling, and comic collage layouts.
3. **media.osakastationcity.com** (ドーヤ？ / do-ya?) - Conversational Kansai-style local appeal, magazine-style content blocks, and interactive widgets that feel alive.

---

## Site Structure (Page Tree)
Based on the visual map from `webデザインアイデアだし.png`, the website follows this hierarchical structure:

1. **TOP (Home Page)**
   - **Hero Section**: Main catchphrase "人生、9割損してる。" and splash entry.
   - **About Section**: Core mission and "preaching" philosophy.
   - **Members Section**: Individual profiles using Polaroid-style frames.
   - **Activities (Slides)**: Interactive CRT TV viewer for passion projects.
   - **News/Sticky Notes**: Recent updates styled as floating sticky notes.
   - **Join/Contact**: Submission form for new members with the ghost mascot.
2. **Detail Pages**
   - **Project Details**: Deep-dives into specific hobbies/preachings.
   - **Article/Blog List**: Collection of club updates and deep-dives.
   - **Article Detail**: Full view of blog posts with scrapbook aesthetics.

---

## Color Palette

### Primary Colors
- **Primary Blue**: `#2A52BE` (Royal Blue) - Used for call-to-actions, primary highlights, and headers.
- **Neon Yellow**: `#FFEB3B` (Accent Yellow) - Used for navigation backgrounds, highlight indicators, and active buttons.

### Accent Colors
- **Soft Pink**: `#FF6B6B` - Used for primary tags and active buttons.
- **Mint Green**: `#4ECDC4` - Used for success states, secondary elements, and the ghost mascot.
- **Lavender**: `#D6BCFA` - Used for secondary tags.

### Neutral Colors
- **Background**: `#faf6ee` (Warm Kraft/Cream Paper) - Gives the analog, cozy feel of sketchbooks.
- **Surface**: `#ffffff` (Pure White) - Used for card bodies and content surfaces to contrast against the cream background.
- **Border**: `#000000` (Pure Black) - Thick neubrutalist borders (`var(--border-black)` and `var(--border-black-thin)`).

### Color Psychology
- The warm cream background evokes the coziness of a physical scrapbook, while the primary blue and neon yellow provide high-energy, pop-art contrast. The combination generates a welcoming yet exciting aesthetic, perfect for a college club dedicated to passionate hobby preaching.

---

## Typography System

### Font Families
- **Primary Font**: `'BIZ UDPGothic', sans-serif` - Body text, paragraphs (extremely readable, friendly gothic style).
- **Secondary Font**: `'Dela Gothic One', sans-serif` - Impactful headings, title accents, and buttons.
- **Accent Font**: `'Outfit', sans-serif` - Emojis, English labels, and sub-headings.

### Font Hierarchy
- **Hero Title**: `2.2rem` / `900` / `1.3` - Dela Gothic (with text stroke and text shadow).
- **Section Heading**: `1.8rem` / `900` / `1.4` - Dela Gothic (centered neubrutalist box).
- **Sub Heading (H3)**: `1.25rem` / `900` / `1.4` - Outfit / BIZ UDPGothic.
- **Body Text**: `0.95rem` / `400` / `1.6` - BIZ UDPGothic.
- **Small Label / Badge**: `0.75rem` / `700` / `1.2` - Outfit.

### Typography Guidelines
- Max line length: 45 Japanese characters per paragraph line for comfortable readability.
- Letter spacing: Slight tracking (`0.05em`) for large headers to fit the neubrutalist grid perfectly.

---

## Layout Principles

### Grid System
- **Main Layout**: Max width of `1200px` for the navbar and section containers.
- **Members Grid**: Single flex column of rows (`gap: 48px`), alternating profile layouts.

### Spacing Scale
- `xs`: `8px` - Button padding, minor margins.
- `sm`: `16px` - Card header padding, minor gaps.
- `md`: `24px` - Card body padding, standard gutters.
- `lg`: `48px` - Section spacings, row gaps.
- `xl`: `80px` - Hero block vertical paddings.

### Responsive Breakpoints
- **Mobile**: `max-width: 768px` - Grid columns collapse to `1fr` and elements stack vertically. Left notebook margin aligns tightly.

---

## Component Styling

### Buttons
- **Primary**: Royal Blue background, thick black border, `box-shadow: 4px 4px 0px #000`. Translates `-2px` on hover.
- **Secondary**: Neon Yellow background, thick black border, `box-shadow: 4px 4px 0px #000`.
- **States**: Hovering shifts the element (`transform: translate(-3px, -3px)`) and increases shadow depth to simulate a physical push-button.

### Cards (Polaroids & Sticky Notes)
- **Polaroid Photo**: Pure white background, unequal bottom border padding (Polaroid format), `transform: rotate(-1.5deg)` for a chaotic collage feel.
- **Washi Tape**: Translucent pastel colors (`rgba(...)`), dashed left/right borders, rotated and placed on top of cards to simulate physical paper tape.
- **Sticky Comments**: Pastel yellow/pink/blue/mint, pinned onto the chalkboard, rotated randomly by `-3deg` to `+3deg`.

### Forms
- **Input Field**: White background, `2px solid #000` border, sharp corner radius (`0px`), focus border changes to royal blue with an offset shadow.

---

## Visual Hierarchy

### Emphasis Techniques
- **Notebook Kraft Margin Line**: A vertical red line on the left side (`body::before`) locks the eyes onto the paper-sheet boundary.
- **Floating Ghost Mascot**: Placed next to the join form. Animated floating motion directs attention to the submission block.
- **CRT Television Case**: Encases the slide deck inside a mahogany-wood TV frame to separate the interactive learning content from static text.

### Content Flow
- Uses a clear vertical flow with section dividers (dashed black borders like `.members-section`), guiding visitors from the high-energy Hero, to the Concept Board, to the Member bios, and finally to the interactive Slide Deck.

---

## Micro-Interactions

### Animation Timing
- **Fast**: `150ms` - Hover translations for buttons and neubrutalist cards.
- **Normal**: `250ms` - Splash screen fade-out, tab navigation fades.
- **Slow**: `3s` - Ghost mascot floating loop.

### Easing Curves
- `cubic-bezier(0.16, 1, 0.3, 1)` (ease-out-expo) - Used for smooth hover offsets and transitions.
- `cubic-bezier(0.85, 0, 0.15, 1)` - Used for the splash screen entry exit transition.

---

## Accessibility

### Contrast Ratios
- High contrast black text against warm cream background exceeds WCAG AAA standards (>7:1).
- All interactive controls have visible thick borders and active focus outlines.

### Touch Targets
- Interactive buttons and card click states have a minimum target size of `44x44px`.

---

## Design Highlights & Brand Alignment

### Inspiration & Rationale
- **ikiiki-being.com** inspired our **Ghost Mascot** and the friendly illustrations.
- **gunze.co.jp/130th/** inspired the playful self-deprecating tagline ("人生、9割損してる。") and bright pop-art layout.
- **media.osakastationcity.com** inspired our **Sticky Blackboard** feedback forum, using Kansai-dialect and local friendly dialogue cards.

---

## Resources
- **Design Guidelines**: [design-guideline.md](file:///Users/yasutakairino/luna-website/docs/design-guideline.md)
- **Design Story**: [design-story.md](file:///Users/yasutakairino/luna-website/docs/design-story.md)
- **Source Code**: [index.html](file:///Users/yasutakairino/luna-website/index.html) | [style.css](file:///Users/yasutakairino/luna-website/style.css)
