#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
THEMES = [
    ("Dark", ROOT / "themes" / "Mineral-Focus.ron"),
    ("Light", ROOT / "themes" / "Mineral-Focus-Light.ron"),
]

REQUIRED_FIELDS = [
    "palette:", "spacing:", "corner_radii:", "neutral_tint:", "bg_color:",
    "primary_container_bg:", "secondary_container_bg:", "text_tint:", "accent:",
    "success:", "warning:", "destructive:", "frosted:", "gaps:", "active_hint:",
    "window_hint:", "frosted_windows:", "frosted_system_interface:",
    "frosted_panel:", "frosted_applets:", "frosted_maximized_apps:", "alpha_map:",
]

ALPHA_KEYS = [
    "extremely_low", "extremely_low_2", "very_low", "very_low_2",
    "low", "low_2", "medium", "medium_2", "high", "high_2",
    "very_high", "very_high_2", "extremely_high", "extremely_high_2",
]

failed = False

for variant, path in THEMES:
    text = path.read_text(encoding="utf-8")
    checks = {}

    checks["variant wrapper"] = f"palette: {variant}((" in text
    checks["balanced parentheses"] = text.count("(") == text.count(")")
    checks["required ThemeBuilder fields"] = all(field in text for field in REQUIRED_FIELDS)
    checks["default gaps (0, 8)"] = "gaps: (0, 8)" in text
    checks["active hint 3"] = "active_hint: 3" in text

    rgba = re.findall(r'#[0-9A-Fa-f]{8}', text)
    checks["RGBA colors"] = len(rgba) >= 30 and all(len(v) == 9 for v in rgba)

    alpha_values = {}
    for key in ALPHA_KEYS:
        match = re.search(rf"\b{re.escape(key)}:\s*([0-9.]+)", text)
        if match:
            alpha_values[key] = float(match.group(1))
    checks["14 alpha-map entries"] = len(alpha_values) == 14
    checks["alpha values 0..1"] = len(alpha_values) == 14 and all(0.0 <= v <= 1.0 for v in alpha_values.values())

    print(f"\n{path.name}")
    for label, ok in checks.items():
        print(f"  {'PASS' if ok else 'FAIL'}  {label}")
        if not ok:
            failed = True

if failed:
    print("\nStatic checks failed.")
    sys.exit(1)

print("\nAll static project checks passed.")
print("Note: this is not a full RON parser. Runtime import in COSMIC Settings is still required.")
