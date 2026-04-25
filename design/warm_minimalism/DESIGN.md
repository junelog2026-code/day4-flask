---
name: Warm Minimalism
colors:
  surface: '#faf9f6'
  surface-dim: '#dbdad7'
  surface-bright: '#faf9f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f1'
  surface-container: '#efeeeb'
  surface-container-high: '#e9e8e5'
  surface-container-highest: '#e3e2e0'
  on-surface: '#1a1c1a'
  on-surface-variant: '#504440'
  inverse-surface: '#2f312f'
  inverse-on-surface: '#f2f1ee'
  outline: '#82746f'
  outline-variant: '#d4c3bd'
  surface-tint: '#77574b'
  primary: '#715246'
  on-primary: '#ffffff'
  primary-container: '#8c6a5d'
  on-primary-container: '#fff6f3'
  inverse-primary: '#e7beae'
  secondary: '#675d54'
  on-secondary: '#ffffff'
  secondary-container: '#ebddd2'
  on-secondary-container: '#6b6158'
  tertiary: '#5f5950'
  on-tertiary: '#ffffff'
  tertiary-container: '#787168'
  on-tertiary-container: '#fff7f0'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbce'
  primary-fixed-dim: '#e7beae'
  on-primary-fixed: '#2c160c'
  on-primary-fixed-variant: '#5d4034'
  secondary-fixed: '#eee0d5'
  secondary-fixed-dim: '#d2c4b9'
  on-secondary-fixed: '#211a14'
  on-secondary-fixed-variant: '#4e453d'
  tertiary-fixed: '#ebe1d6'
  tertiary-fixed-dim: '#cec5bb'
  on-tertiary-fixed: '#1f1b14'
  on-tertiary-fixed-variant: '#4c463e'
  background: '#faf9f6'
  on-background: '#1a1c1a'
  surface-variant: '#e3e2e0'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.25'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  container-max: 1200px
  gutter: 20px
---

## Brand & Style

The design system is anchored in the concept of "Digital Hygge"—creating a sense of comfort, clarity, and approachability. It is designed for a blog board where content takes center stage within a serene, welcoming environment. 

The style combines **Minimalism** with a **Tactile** warmth. By stripping away unnecessary ornamentation and focusing on high-quality whitespace and soft tonal transitions, the system evokes an emotional response of calm and focus. It avoids the coldness of traditional tech interfaces by using organic, sun-drenched neutrals and deep, earthy accents to ground the experience.

## Colors

The palette is derived from natural, earthy materials to ensure a warm and inviting reading experience.

- **Primary (#8C6A5D):** A soft, muted brown used for primary actions, active states, and key brand identifiers. It provides enough contrast for accessibility while maintaining the warm theme.
- **Secondary (#E3D5CA):** A "Soft Sand" tone used for secondary buttons, chips, and subtle borders.
- **Tertiary (#F5EBE0):** A "Cream" shade used for card backgrounds and container surfaces to separate content from the main page.
- **Neutral (#FAF9F6):** A "Bone White" used as the primary background color for the entire application to reduce eye strain compared to pure white.

Accent colors for success, warning, and error should be muted versions of green, amber, and terracotta to remain harmonious with the warm beige base.

## Typography

This design system utilizes **Plus Jakarta Sans** for its modern, friendly, and geometric characteristics. The typeface’s open apertures and soft curves complement the rounded UI elements.

- **Headlines:** Use a tighter letter-spacing and heavier weights to create a strong visual hierarchy against the light backgrounds.
- **Body Text:** Optimized for long-form reading with a generous 1.6 line-height. Use the 'Primary' color at 80% opacity for body text to soften the contrast against the cream background.
- **Labels:** Utilized for categories, tags, and button text, often in uppercase or semi-bold to distinguish them from editorial content.

## Layout & Spacing

The layout follows a **responsive mobile-first approach** with a fluid grid system that transitions into a centered fixed-width container on larger screens.

- **Grid:** On mobile, use a single-column layout with 20px side margins. On desktop, utilize a 12-column grid with 24px gutters.
- **Rhythm:** All spacing (padding, margins) is based on a 4px baseline unit. 
- **Density:** The design system prioritizes "Negative Space" to ensure the blog doesn't feel cluttered. Cards and sections should utilize the 'xl' (48px) spacing for vertical separation to allow the content to breathe.

## Elevation & Depth

Visual hierarchy in this design system is achieved through **Ambient Shadows** and **Tonal Layering** rather than heavy borders.

- **Surface Levels:** The background is the lowest level (#FAF9F6). Cards and input fields sit on Level 1 (#F5EBE0 or white).
- **Shadows:** Use extremely diffused, low-opacity shadows. The shadow color should be tinted with the primary brown (e.g., `rgba(140, 106, 93, 0.08)`) rather than pure black to maintain the warmth of the palette.
- **Depth:** Hover states on interactive cards should subtly increase the shadow spread and lift the element by 2px to provide tactile feedback.

## Shapes

The shape language is consistently **Rounded**, reinforcing the friendly and approachable brand personality.

- **Base Radius:** 0.5rem (8px) for standard components like buttons and small input fields.
- **Large Radius:** 1rem (16px) for cards, modals, and large container elements.
- **Full Radius:** Used exclusively for tags, chips, and search bars to create a "pill" look that stands out from the rectangular grid of blog posts.

## Components

The components within the design system focus on simplicity and ease of interaction.

- **Action Buttons:** Primary buttons use the Primary brown with white text. Secondary buttons use a transparent background with a 1px border of the Secondary sand color. All buttons feature a 0.2s transition on hover.
- **Cards:** Blog cards are the primary container. They feature a white or tertiary background, 16px rounded corners, and a soft ambient shadow. Images within cards should always have the top corners clipped to match the card radius.
- **Input Fields:** Search and comment inputs use a subtle "Soft Sand" background rather than a white background, making them feel integrated into the page. Focus states are indicated by a 2px Primary brown border.
- **Lists:** Used for "Recent Posts" or "Categories." Lists should avoid dividers; use vertical spacing (12px to 16px) and subtle hover-state background shifts to define items.
- **Chips/Tags:** Small, pill-shaped elements used for categorization. They use the Secondary sand color as a background with slightly darker text for legibility.