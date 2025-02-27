import json
import os

# Default settings
SVG_SIZE = 24  # Width and height in pixels (standard icon size)
FONT_SIZE = 20  # Font size for text in SVG
FONT_FAMILY = "monospace"  # Ensures consistent rendering of ASCII/Unicode

# Color schemes
COLORS = {
    "light": {"fg": "#000000", "bg": "#FFFFFF"},  # Black on white
    "dark": {"fg": "#FFFFFF", "bg": "#000000"},   # White on black
}

def load_icons(file_path="icons.json"):
    with open(file_path, "r") as f:
        return json.load(f)

def create_svg(icon_char, category, mode="light", custom_fg=None, custom_bg=None, output_dir="icons"):
    # Determine colors
    fg = custom_fg if custom_fg else COLORS[mode]["fg"]
    bg = custom_bg if custom_bg else COLORS[mode]["bg"]

    # SVG template
    svg_content = f"""<svg width="{SVG_SIZE}" height="{SVG_SIZE}" xmlns="http://www.w3.org/2000/svg">
    <rect x="0" y="0" width="{SVG_SIZE}" height="{SVG_SIZE}" fill="{bg}"/>
    <text x="50%" y="50%" font-family="{FONT_FAMILY}" font-size="{FONT_SIZE}" fill="{fg}" 
          text-anchor="middle" dominant-baseline="middle">{icon_char}</text>
</svg>"""

    # Create output directory
    mode_dir = os.path.join(output_dir, category, mode if not custom_fg else "custom")
    os.makedirs(mode_dir, exist_ok=True)

    # Sanitize filename (replace special chars if needed)
    filename = f"{icon_char.encode('utf-8').hex()}.svg" if custom_fg else f"{icon_char.encode('utf-8').hex()}_{mode}.svg"
    filepath = os.path.join(mode_dir, filename)

    # Write SVG file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content)
    
    return filepath

def generate_all_icons(icons, output_dir="icons"):
    for name, char in icons.items():
        # Light mode
        light_path = create_svg(char, "light", output_dir=output_dir)
        print(f"Generated: {light_path}")

        # Dark mode
        dark_path = create_svg(char, "dark", output_dir=output_dir)
        print(f"Generated: {dark_path}")

        # Custom color example (e.g., Red FG, Blue BG)
        custom_fg = "#FF0000"  # Red
        custom_bg = "#0000FF"  # Blue
        custom_path = create_svg(char, "custom", custom_fg, custom_bg, output_dir=output_dir)
        print(f"Generated: {custom_path}")

def main():
    # Sample icons (could be loaded from JSON)
    icons_sample = {
        "file": "📄",
        "folder": "📁",
        "arrow-right": "→",
        "checkmark": "✓",
        "gear": "⚙"
    }

    icons = {}

    with open("data/unicode_icons.json", "r", encoding="utf-8") as f:
        icons = json.load(f)
    
    for category, info in icons.items():
        for char in info["characters"]:
            create_svg(char["character"], category, "light")  # From earlier script

    '''
    with open('data/unicode_icons.json') as f:
        icons = json.load(f)
        # Generate SVG icons
        generate_all_icons(icons)
    '''

if __name__ == "__main__":
    main()