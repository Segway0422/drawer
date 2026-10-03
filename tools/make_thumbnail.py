#!/usr/bin/env python3
"""
Etsy/Payhip listing thumbnail generator — house style.

Style spec (agreed 2026-10-03):
  - Square canvas, 1200x1200px.
  - 3 colorways shown side by side as equal vertical bands
    (each band = a center-cropped vertical strip of that colorway,
    scaled to fill its band height-to-height).
  - No divider between bands — they sit flush against each other,
    whether built from separate source images or from an already
    pre-composited 3-panel image. (Revised 2026-10-03: an earlier
    version added a 6px white divider when building from separate
    images, but that broke visual consistency with the no-divider
    composites — don't reintroduce it.)
  - Bottom label bar: solid near-black (20, 20, 20), 150px tall,
    spanning the full width.
  - Title: Liberation Serif Bold, white, centered, starts at 64pt
    and auto-shrinks (in 2pt steps, floor 28pt) to fit within
    CANVAS - 80px. Example: "KIKU CHRYSANTHEMUM".
  - Subtitle: Liberation Sans Regular, 32pt, warm gold
    (220, 195, 150), centered, below the title. Convention:
    "SEAMLESS PATTERN · 3 COLORWAYS" (or "· 3 DESIGNS" when the
    3 files differ by motif rather than just color).

Usage:
  # Build a 3-band thumbnail from 3 separate colorway images:
  python3 make_thumbnail.py --out out.jpg --title "KIKU CHRYSANTHEMUM" \
      --subtitle "SEAMLESS PATTERN · 3 COLORWAYS" \
      --bands white.jpg black.jpg indigo.jpg

  # Add the label bar to an already-composited 3-panel image:
  python3 make_thumbnail.py --out out.jpg --title "SHIPPO" \
      --subtitle "SEAMLESS PATTERN · 3 COLORWAYS" \
      --composite shippo_3panel.webp
"""
import argparse
from PIL import Image, ImageDraw, ImageFont

CANVAS = 1200
BAR_H = 150
FONT_TITLE = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
FONT_SUB = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
GOLD = (220, 195, 150)


def build_from_bands(paths):
    band_w = CANVAS // len(paths)
    canvas = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    for i, p in enumerate(paths):
        im = Image.open(p).convert("RGB")
        w, h = im.size
        target_ratio = band_w / CANVAS
        crop_w = int(h * target_ratio)
        left = (w - crop_w) // 2
        strip = im.crop((left, 0, left + crop_w, h)).resize((band_w, CANVAS), Image.LANCZOS)
        canvas.paste(strip, (i * band_w, 0))
    return canvas


def build_from_composite(path):
    im = Image.open(path).convert("RGB")
    w, h = im.size
    side = min(w, h)
    left = (w - side) // 2
    top = (h - side) // 2
    return im.crop((left, top, left + side, top + side)).resize((CANVAS, CANVAS), Image.LANCZOS)


def add_label_bar(canvas, title, subtitle):
    draw = ImageDraw.Draw(canvas)
    draw.rectangle([0, CANVAS - BAR_H, CANVAS, CANVAS], fill=(20, 20, 20))

    size = 64
    font_title = ImageFont.truetype(FONT_TITLE, size)
    max_w = CANVAS - 80
    while True:
        bbox = draw.textbbox((0, 0), title, font=font_title)
        tw = bbox[2] - bbox[0]
        if tw <= max_w or size <= 28:
            break
        size -= 2
        font_title = ImageFont.truetype(FONT_TITLE, size)
    bbox = draw.textbbox((0, 0), title, font=font_title)
    tw = bbox[2] - bbox[0]
    draw.text(((CANVAS - tw) // 2, CANVAS - BAR_H + 18), title, font=font_title, fill=(255, 255, 255))

    font_sub = ImageFont.truetype(FONT_SUB, 32)
    sbbox = draw.textbbox((0, 0), subtitle, font=font_sub)
    sw = sbbox[2] - sbbox[0]
    draw.text(((CANVAS - sw) // 2, CANVAS - BAR_H + 95), subtitle, font=font_sub, fill=GOLD)
    return canvas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--subtitle", required=True)
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--bands", nargs="+", help="2+ separate colorway images to lay out as bands")
    group.add_argument("--composite", help="an already 3-panel composited image")
    args = ap.parse_args()

    canvas = build_from_bands(args.bands) if args.bands else build_from_composite(args.composite)
    canvas = add_label_bar(canvas, args.title, args.subtitle)
    canvas.save(args.out, quality=92)
    print("saved", args.out)


if __name__ == "__main__":
    main()
