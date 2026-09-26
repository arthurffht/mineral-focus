# Contributing to Mineral Focus

Contributions are welcome, but theme changes must preserve the project's design and compatibility rules.

## Before changing a `.ron` file

1. Start from the canonical file in `themes/`.
2. Do not add fields that are not part of the current COSMIC ThemeBuilder schema.
3. Keep the Dark/Light variants structurally aligned unless an upstream COSMIC difference requires otherwise.
4. Run `python3 tools/static_check.py`.
5. Import the changed file into COSMIC Settings.
6. Test the relevant surfaces listed in `docs/TESTING.md`.
7. Document visible behavior changes in `CHANGELOG.md`.

## Design requirements

Changes should preserve:
- strong surface hierarchy;
- readable text and controls;
- restrained use of the mint accent;
- opaque content-heavy application windows;
- Frosted Glass primarily for system chrome;
- user control over fonts and interface density.

## Pull request expectations

A pull request that changes colors or geometry should include:
- what changed;
- why it changed;
- screenshots before/after when possible;
- affected COSMIC version;
- runtime test results.

## Credits

Merged contributors should be added to `CONTRIBUTORS.md` using their chosen public name or handle.
