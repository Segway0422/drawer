# Etsy/Payhip listing style guide

House conventions agreed on 2026-10-03. Reuse these for every new pattern
listing instead of improvising a new format each time.

## Thumbnail image

See `tools/make_thumbnail.py` for the generator. Summary:

- Square canvas, 1200x1200px.
- The 3 colorways (or 3 designs) shown side by side as equal vertical
  bands, each a center-cropped strip of that pattern.
- 6px white divider between bands (only needed when building bands from
  separate source images; skip it when starting from an already
  pre-composited 3-panel image).
- Bottom label bar: solid near-black (20, 20, 20), 150px tall, full width.
- Title: Liberation Serif Bold, white, centered, auto-shrinks from 64pt
  (floor 28pt) to fit. Short product name, e.g. "KIKU CHRYSANTHEMUM".
- Subtitle: Liberation Sans Regular, 32pt, warm gold (220, 195, 150),
  centered below the title. Convention: "SEAMLESS PATTERN · 3 COLORWAYS"
  (use "· 3 DESIGNS" when the 3 files differ by motif, not just color).

## Description text

Template (fill in the bracketed parts):

```
[One sentence: "This set features 3 ... seamless patterns ... — perfect
for scrapbooking, gift wrapping, stationery, packaging design, and more."]

Includes 3 colorways:
- [Name 1]
- [Name 2]
- [Name 3]

What you'll get:
- 3 high-resolution JPG files (3600x3600px / 300 DPI, 12x12 inches)
- 3 high-resolution PNG files
- Seamless, tileable design
- Instant digital download

For personal and commercial use. Please note this is a digital product;
no physical item will be shipped.
```

Rules learned from review so far:

- Use "Includes 3 colorways:" when the 3 files are the same motif in
  different colors; use "Includes 3 designs:" when they differ by motif
  (e.g. different florals on a shared indigo style).
- State "no physical item will be shipped" **once**, in the closing
  sentence — don't repeat it in the "What you'll get" bullets too.
- Give each colorway/design a name distinct from the others — don't let
  two items share the same label (e.g. not two "Navy & Gold" entries;
  differentiate as "Navy & Gold" vs "Navy, Gold & Teal").
- Keep the whole description under 800 characters (counting newlines).
- Keep "Seamless, tileable design" as its own bullet — don't pad it with
  a redundant clause like "— perfect for continuous patterns".
- File spec (JPG + PNG, 3600x3600px / 300 DPI, 12x12in) is the shop's
  standard deliverable — confirm the actual files match this resolution
  before publishing; don't claim it if the real export is still lower-res.
