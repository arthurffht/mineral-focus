# Release testing

Static checks are necessary but not sufficient. Every release must be imported and tested in COSMIC.

## Required applications/surfaces

- COSMIC Settings
- COSMIC Files
- COSMIC Edit
- COSMIC Terminal
- COSMIC Store
- Launcher
- App Library
- Panel
- Dock
- Applet popups
- Notifications
- OSD
- tiling
- stacked windows
- dialogs and context menus

## Display conditions

Test at:
- 100% scale
- 125% scale when available
- 150% scale
- dark wallpaper
- bright wallpaper
- highly saturated/colorful wallpaper

## Functional checks

Reject a release if:
- focused and unfocused windows are difficult to distinguish;
- important text loses readability;
- disabled, hover, pressed, and selected states collapse visually;
- destructive/warning/success states become confusing;
- Frosted Glass makes wallpaper detail compete with content;
- accent occupies large areas without a functional reason;
- Light is produced only by mechanically inverting Dark.

## Import checks

1. Back up/export the user's current theme.
2. Import the release `.ron` through COSMIC Settings.
3. Confirm the correct Dark/Light mode is selected.
4. Log out/in only if a specific upstream component requires it; theme import itself should not be documented as requiring a reboot.
5. Exercise the UI surfaces above.

## Static checker

Run:

```bash
python3 tools/static_check.py
```

This checker verifies project invariants and expected ThemeBuilder field presence. It is **not** a complete RON parser and does not replace runtime import testing.
