import json
import os

# Embedded Unicode 15.1 Blocks (simplified; full list parsed from Blocks.txt)
# For brevity, I'll include a subset here and explain how to fetch the full list.
UNICODE_BLOCKS = {
    "Basic Latin": {"range": (0x0000, 0x007F), "desc": "ASCII and control characters"},
    "Latin-1 Supplement": {"range": (0x0080, 0x00FF), "desc": "Additional Latin characters"},
    "Latin Extended-A": {"range": (0x0100, 0x017F), "desc": "Extended Latin characters"},
    # ... (329 blocks total)
    "CJK Unified Ideographs": {"range": (0x4E00, 0x9FFF), "desc": "Chinese, Japanese, Korean ideographs"},
    "Hangul Syllables": {"range": (0xAC00, 0xD7AF), "desc": "Korean syllables"},
    "Emoticons": {"range": (0x1F600, 0x1F64F), "desc": "Emoji faces"},
    # Last block in 15.1
    "Kaktovik Numerals": {"range": (0x1D2C0, 0x1D2DF), "desc": "Inupiaq numerals"}
}

# Full blocks will be loaded dynamically below if Blocks.txt is available

def load_unicode_blocks(blocks_file="Blocks-15.1.0.txt"):
    """Load all Unicode blocks from Blocks.txt if available, otherwise use embedded subset."""
    blocks = {}
    if os.path.exists(blocks_file):
        with open(blocks_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip() and not line.startswith("#"):
                    # Format: "0000..007F; Basic Latin"
                    range_part, name = line.split(";", 1)
                    start, end = range_part.split("..")
                    blocks[name.strip()] = {
                        "range": (int(start, 16), int(end, 16)),
                        "desc": f"Unicode block: {name.strip()}"
                    }
    else:
        print("Blocks.txt not found. Using embedded subset (not exhaustive).")
        return UNICODE_BLOCKS
    return blocks

def generate_unicode_icons(blocks):
    """Generate a dictionary of all Unicode characters organized by block."""
    icons = {}
    
    for category, info in blocks.items():
        start, end = info["range"]
        icons[category] = {
            "description": info["desc"],
            "characters": []
        }
        
        for code_point in range(start, end + 1):
            try:
                char = chr(code_point)
                # Skip non-characters and unassigned (basic filter)
                if char.isprintable() and code_point not in (0xFFFE, 0xFFFF):  # Exclude U+FFFE, U+FFFF
                    icons[category]["characters"].append({
                        "code_point": f"U+{code_point:04X}",
                        "character": char,
                        "decimal": code_point,
                        "hex": hex(code_point)
                    })
            except ValueError:
                continue  # Skip invalid code points
    
    return icons

def save_to_json(data, output_file="unicode_icons.json"):
    """Save the generated icons to a JSON file."""
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved {os.path.getsize(output_file) / 1024 / 1024:.2f} MB to {output_file}")

def main():
    # Load all Unicode blocks
    print("Loading Unicode blocks...")
    blocks_file = os.getcwd() + "/data/Blocks-15.1.0.txt"
    unicode_blocks = load_unicode_blocks(blocks_file)
    
    # Generate the full Unicode icon set
    print("Generating Unicode icons (this may take a few minutes)...")
    unicode_icons = generate_unicode_icons(unicode_blocks)
    
    # Count total characters
    total_chars = sum(len(category["characters"]) for category in unicode_icons.values())
    print(f"Generated {total_chars} characters across {len(unicode_icons)} categories.")
    
    # Save to JSON
    output_file = os.getcwd() + "/data/unicode_icons.json"
    save_to_json(unicode_icons, output_file)
    
    # Print a sample from a few blocks
    sample_blocks = list(unicode_icons.keys())[:3] + list(unicode_icons.keys())[-3:]
    for category in sample_blocks:
        info = unicode_icons[category]
        sample = info["characters"][:3]  # First 3 characters
        print(f"\n{category} ({len(info['characters'])} chars):")
        for char in sample:
            print(f"  {char['code_point']}: {char['character']}")

if __name__ == "__main__":
    main()