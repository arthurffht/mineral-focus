# Maintenance policy

## Versioning

Mineral Focus uses semantic-style project versions:
- patch: documentation, metadata, or non-breaking visual fixes
- minor: meaningful visual changes or new supported COSMIC capabilities
- major: intentional design-system break or incompatible theme schema migration

## Upstream COSMIC updates

For every significant COSMIC/libcosmic theming update:

1. Check the current `ThemeBuilder` version and field set.
2. Export a fresh Dark and Light theme from COSMIC Settings.
3. Compare the exported structure with `themes/`.
4. Update both variants when schema compatibility requires it.
5. Run static checks.
6. Perform the full runtime test matrix.
7. Update `docs/UPSTREAM.md` with the new checked date/release.
8. Record compatibility changes in `CHANGELOG.md`.

## Contributor attribution

- `AUTHORS.md` records the original creator and maintainers.
- `CONTRIBUTORS.md` records additional contributors.
- Never remove historical creator attribution as part of routine maintenance.

## Design stability

Do not churn the palette to follow trends. A change should solve a documented usability, compatibility, or identity problem.
