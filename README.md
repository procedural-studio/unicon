# UniCon

A minimalist, text-based icon set built with ASCII and Unicode characters, available as SVG and PNG files. Perfect for terminals, web, and apps.

### Buy me a Coffee

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/silverdragon02)

## Features
- **149,813 Icons**: Every Unicode character (v15.1) in SVG and PNG formats.
- **Categories**: Organized by Unicode blocks (e.g., Arrows, Shapes, Emojis).
- **Light/Dark Modes**: Pre-rendered variants.
- **Customizable**: Generate your own with provided scripts.
- **Lightweight**: SVGs ~200 bytes, PNGs ~400 bytes (1x).

## Installation

Use the jsDelivr CDN to include icons directly in your project. Files are hosted at `github.com/yourusername/unicon`.

### Example: Arrow Right (SVG)
```html
<img src="https://cdn.jsdelivr.net/gh/procedural-studio/unicon@main/icons/Latin-1%20Supplement/dark/c3b7_dark.svg" alt="Arrow Right" width="24" height="24">
```

![div](https://cdn.jsdelivr.net/gh/procedural-studio/unicon@main/icons/Latin-1%20Supplement/dark/c3b7_dark.svg)

## Usage

- **Browse Icons**: Check unicode_icons.json for code points (e.g., U+2192 for →).
- **CDN Path**: Replace 2192_light with the desired icon’s hex code and mode (light, dark, custom).
- **Custom Builds**: Run generate_svg_icons.py to create your own set.


## Contributing

- Add new categories or scripts via pull requests.
- GNU V2 License.

## Credits

- Built with Python, Unicode 15.1, and cairosvg.
- Hosted by jsDelivr.







