# release/ — the path to production

Root `AGENTS.md` applies, and sections 3, 4 and 5 are the relevant ones.

Model: **frontier tier, read-only** (`codex -p safety` — `gpt-5.6-sol` with
`sandbox_mode = "read-only"`). Mistakes here are expensive and hard to reverse,
so the sandbox enforces what instructions only ask for.

**Do not read `contract.json` or `contract.example.json`.** They are 832 KB
between them — roughly 208,000 tokens of generated URL manifest. Query them:

    python3 -c "import json;d=json.load(open('release/contract.json'));print(len(d['acceptance']['checks']))"

## What actually goes wrong here

- **Port and subnet allocation is a human decision and must not be automated.**
  The host wrapper owns its Compose template. The contract uses the already-onboarded
  shared-private-edge values: internal port 8080, network `platform-private-edge`,
  and private IPv4 `10.89.2.22`. There is no repository loopback allocation.
- **Digests, not tags.** A deployment references `@sha256:<manifest digest>`.
  Layer digests scraped from a build log are NOT the manifest digest. The package
  is public, so an anonymous ghcr pull token is enough — "blocked on credentials"
  is almost always the wrong conclusion.
- **The release workflow deploys through `platform-deploy-static`.** Green build and
  metadata gates precede the protected production environment approval and cutover.
- **Key run queries to the head SHA.** Listing "the latest runs" returns the
  previous commit's results before the new ones appear, and reads as green.
- Some invariants live only in `.github/workflows/ci.yml`. Run the workflow's own
  steps locally before concluding a change is safe.

The normative contract is in `dmedellin/platform-ops`, and the root-owned host
registry wins over anything written here. Read the real document rather than
reconstructing it from this summary.
