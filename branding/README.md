# CINCTRA Brand

Logo and brand assets for CINCTRA.

## Layout

```
logo/
  cinctra-icon-light.svg          Gray ring + purple gradient feather (use on light backgrounds)
  cinctra-icon-dark.svg           White ring + purple gradient feather (use on dark backgrounds)
  cinctra-icon-mono.svg           Solid black (single-color reproduction)
  cinctra-icon-glyph.svg          Solid purple (compact use, app icon glyph)
  cinctra-icon-favicon-light.svg  Favicon variant for light browser chrome
  cinctra-icon-favicon-dark.svg   Favicon variant for dark browser chrome
  png/                            Pre-rendered PNGs at standard sizes

source/
  cinctra-icon-simplified.svg     Master/base SVG. All variants derive from this.

scripts/
  build-pngs.py                   Regenerate the PNG renders from the SVG variants
```

## Color spec

| Token            | Hex       | Used in                           |
| ---------------- | --------- | --------------------------------- |
| Heather Gray     | `#9CA3AF` | Ring (light variant)              |
| White            | `#FFFFFF` | Ring (dark variant)               |
| Black            | `#000000` | Mono variant (ring + feather)     |
| Deep Indigo      | `#4C2AE8` | Feather gradient start            |
| Bright Purple    | `#7C3AED` | Feather gradient end, glyph fill  |

The feather uses a linear gradient from Deep Indigo (`#4C2AE8`) to Bright Purple (`#7C3AED`) in the light, dark, and favicon variants. Mono and glyph use a solid fill.

## Design tenets

- Feather always sits inside the ring boundary.
- The rachis (white spine down the feather) is preserved via `fill-rule="evenodd"` — do not flatten this.
- Variants share identical geometry so they overlay pixel-for-pixel.

## Regenerating PNGs

Requires Python 3 and `cairosvg`:

```bash
pip install cairosvg
python scripts/build-pngs.py
```

PNG sizes per variant:

| Variant         | Sizes                          |
| --------------- | ------------------------------ |
| light, dark     | 1024, 512, 256, 128            |
| mono, glyph     | 1024, 512, 256, 128, 64, 32, 16 |
| favicon-light, favicon-dark | 256, 128, 64, 32, 16 |

## Provenance

The master SVG in `source/` was hand-traced from a raster reference, then simplified to two paths (ring + feather) with a clipping circle to constrain the feather inside the ring. See commit history for the full evolution.

## License

Internal use. Do not redistribute outside CINCTRA without permission.
