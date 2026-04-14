#!/usr/bin/env python3
"""Render the SVG variants in logo/ to PNGs in logo/png/ at standard sizes.

Requires:
    pip install cairosvg
"""

from pathlib import Path
import sys

try:
    import cairosvg
except ImportError:
    sys.exit("cairosvg not installed. Run: pip install cairosvg")

ROOT = Path(__file__).resolve().parent.parent
LOGO_DIR = ROOT / "logo"
PNG_DIR = LOGO_DIR / "png"

# Sizes to render per variant
SIZES = {
    "light":         [1024, 512, 256, 128],
    "dark":          [1024, 512, 256, 128],
    "mono":          [1024, 512, 256, 128, 64, 32, 16],
    "glyph":         [1024, 512, 256, 128, 64, 32, 16],
    "favicon-light": [256, 128, 64, 32, 16],
    "favicon-dark":  [256, 128, 64, 32, 16],
}


def main() -> None:
    PNG_DIR.mkdir(parents=True, exist_ok=True)
    rendered = 0
    for variant, sizes in SIZES.items():
        svg = LOGO_DIR / f"cinctra-icon-{variant}.svg"
        if not svg.exists():
            print(f"  skip (missing): {svg.name}")
            continue
        for size in sizes:
            out = PNG_DIR / f"cinctra-icon-{variant}-{size}.png"
            cairosvg.svg2png(url=str(svg), write_to=str(out), output_width=size)
            print(f"  {out.relative_to(ROOT)}")
            rendered += 1
    print(f"\nRendered {rendered} PNGs to {PNG_DIR.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
