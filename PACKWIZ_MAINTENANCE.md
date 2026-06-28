Packwiz maintenance rules:

1. Keep mod jar paths stable across releases.
2. Never commit jar names with suffixes like `(1)`.
3. Prefer `mods/*.pw.toml` with `metafile = true` for upstream-managed mods.
4. If a CurseForge metadata download is flaky, vendor the jar and point the `.pw.toml` at a stable URL.
5. Remove obsolete mods from `index.toml` instead of leaving old paths around.
6. Avoid manual client-side jar drops into `mods/` for published instances.

Why this matters:

- Packwiz removes old files by path tracking.
- Renamed jars look like new files, so stale old jars are harder to clean up predictably.
- Stable filenames make upgrades and removals deterministic.
