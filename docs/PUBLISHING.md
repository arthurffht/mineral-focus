# Publishing Mineral Focus

## Current community distribution path

As of 2026-09-26, System76's official COSMIC theming page points users to the community COSMIC Themes project for downloading and adding themes.

The COSMIC Themes submission page currently instructs users to export from:

`COSMIC Settings → Desktop → Appearance → Export`

and accepts:
- Name
- Author
- Link
- Theme `.ron` file

Submissions are reviewed for spam.

## Mineral Focus submission

### Main
- Name: `Mineral Focus`
- Author: `Arthur`
- Link: public repository URL
- File: `themes/Mineral-Focus.ron`

### Companion
- Name: `Mineral Focus Light`
- Author: `Arthur`
- Link: same public repository URL
- File: `themes/Mineral-Focus-Light.ron`

## Before uploading

- Run `python3 tools/static_check.py`
- Complete `docs/TESTING.md`
- Update `CHANGELOG.md`
- Confirm `VERSION`
- Regenerate `SHA256SUMS`
- Tag the repository release
- Upload only the canonical `.ron` from `themes/`

## Updating/removing a COSMIC Themes listing

The COSMIC Themes project README currently tells authors who want an uploaded theme removed or changed to open an issue in the site's repository.

## Important

COSMIC Themes is a community project referenced by System76; do not describe Mineral Focus itself as an official System76 theme.
