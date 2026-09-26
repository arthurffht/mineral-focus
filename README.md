# Mineral Focus

**A focused graphite theme family for the COSMIC desktop.**

**Original creator:** Arthur  
**Current release:** 1.0.0  
**License:** MIT  
**Target:** COSMIC Epoch 1.9.x / `libcosmic` ThemeBuilder v2

Mineral Focus is designed for long daily use: graphite surfaces, a restrained mineral-mint accent, strong visual hierarchy, and Frosted Glass where it adds identity without interfering with content.

> Mineral Focus is an independent community project. It is not an official System76 theme and is not endorsed or maintained by System76.

## Themes

| File | Role |
| --- | --- |
| `themes/Mineral-Focus.ron` | Main dark release |
| `themes/Mineral-Focus-Light.ron` | Matching light companion |

## Design rules

- Accent is a focus/state signal, not a decoration layer.
- Normal application windows remain opaque.
- Frosted Glass is limited to system interface, panel, and applets.
- COSMIC's spacing scale is preserved.
- Tiling gaps stay at the current ThemeBuilder default `(0, 8)`.
- Active window hint is `3 px`, matching the current ThemeBuilder default.
- The theme does not force fonts or interface density.
- Dark and Light are designed independently; Light is not a simple color inversion.

## Install

1. Open **COSMIC Settings**.
2. Go to **Desktop → Appearance**.
3. Click **Import**.
4. Select a `.ron` file from `themes/`.

## Public attribution

For the COSMIC Themes submission, use:

- **Name:** Mineral Focus
- **Author:** Arthur
- **Link:** the public project repository
- **Theme file:** `themes/Mineral-Focus.ron`

The official ThemeBuilder v2 schema does not contain author/version/contributor fields. Do **not** add custom fields to the `.ron` file. Authorship belongs in the repository metadata and in the COSMIC Themes `Author` field.

## Documentation

- [`AUTHORS.md`](AUTHORS.md) — permanent original-author credit
- [`CONTRIBUTORS.md`](CONTRIBUTORS.md) — community contributors
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution rules
- [`docs/SCHEMA.md`](docs/SCHEMA.md) — ThemeBuilder v2 mapping
- [`docs/PALETTE.md`](docs/PALETTE.md) — visual system
- [`docs/TESTING.md`](docs/TESTING.md) — release test matrix
- [`docs/PUBLISHING.md`](docs/PUBLISHING.md) — COSMIC Themes release procedure
- [`docs/UPSTREAM.md`](docs/UPSTREAM.md) — official upstream references
- [`docs/MAINTENANCE.md`](docs/MAINTENANCE.md) — update policy
- [`CHANGELOG.md`](CHANGELOG.md) — release history

## Source of truth

The source `.ron` files in `themes/` are the canonical theme files. Generated downloads, mirrors, or re-exports should never replace them without review.

## Status

The files are statically checked against the ThemeBuilder v2 field set used by current COSMIC. Runtime import and visual testing in COSMIC are still required before every public release.
