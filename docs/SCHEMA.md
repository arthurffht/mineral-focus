# COSMIC ThemeBuilder v2 mapping

Checked against current `pop-os/libcosmic` on 2026-09-26.

`ThemeBuilder` is currently version 2. The portable `.ron` files in this project map only to ThemeBuilder-supported fields.

## Fields used

| Field | Mineral Focus policy |
| --- | --- |
| `palette` | Complete Dark/Light `CosmicPalette` |
| `spacing` | Keep COSMIC default spacing scale |
| `corner_radii` | 0 / 4 / 8 / 12 / 16 / pill |
| `neutral_tint` | `None` |
| `bg_color` | Explicit base surface |
| `primary_container_bg` | Explicit first container level |
| `secondary_container_bg` | Explicit second container level |
| `text_tint` | Explicit text tint |
| `accent` | Mineral-mint focus color |
| `success` | Semantic positive state |
| `warning` | Semantic warning state |
| `destructive` | Semantic destructive/error state |
| `frosted` | `Medium2` |
| `gaps` | `(0, 8)` |
| `active_hint` | `3` |
| `window_hint` | Theme accent |
| `frosted_windows` | `false` |
| `frosted_system_interface` | `true` |
| `frosted_panel` | `true` |
| `frosted_applets` | `true` |
| `frosted_maximized_apps` | `false` |
| `alpha_map` | Explicit 14-step map |

## Fields that do not exist in ThemeBuilder v2

Do not add project metadata such as:
- `author`
- `version`
- `contributors`
- `homepage`
- `license`

Those belong in repository files and the COSMIC Themes submission metadata. Adding arbitrary fields can make deserialization fail.

## Portable theme vs internal COSMIC config

The portable `.ron` file is a serialized ThemeBuilder for import/export.

COSMIC's internal configuration also uses versioned cosmic-config IDs and separate persisted fields. Editing internal files directly is not the distribution format for Mineral Focus.

## Compatibility rule

When upstream ThemeBuilder changes:
1. inspect the new upstream struct;
2. export a fresh theme from current COSMIC Settings;
3. compare the exported field set;
4. update this document and both variants together;
5. perform runtime import tests before release.
