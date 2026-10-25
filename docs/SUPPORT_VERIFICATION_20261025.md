# Donation support hub — verification record

**2026-10-25 · public-safe, pre-release review · draft**

## Scope

Create a single QR landing page at `https://github.com/SeraphPLC/age-of-free-programming/blob/main/SUPPORT.md`, a stable README link, and optional donation-poster assets. This does not install a processor, payment service, data collection system, or automatic donation tracker.

## Checks executed

| Area | Result | Boundary |
| --- | --- | --- |
| Repository continuity | PASS | Reviewed current `main`, privacy rules, and existing empty donation branch; new work branches from the current `main` rather than rewriting earlier work |
| Central QR payload | PASS | Native QR generation and exact text comparison of decoded payload against the intended `SUPPORT.md` URL |
| Standalone exported QR PNG | PASS | Independent device image barcode recognizer: exactly one QR; exact target text matched |
| Exported poster PNG | PASS | Device image barcode recognizer: exactly one QR; exact target text matched |
| Public landing page | PENDING | GitHub link is not live on `main` until authorized merge |
| Payment recipients | BLOCKED | Provider account ownership, intended public disclosure, and live destination remain unverified |
| Individual payment QR codes | WITHHELD | Original source contains personal payment information and inconsistent identifiers; do not copy them |
| Native Sponsor configuration | DEFERRED | No compatible verified public payment URLs have been approved |
| Human publication review | PENDING | Draft PR only; no merge or automated release approval |

## Safe public content

The only QR payload is the public repository URL shown above. No direct payment identifiers are in the public text or graphics. The two generated images and poster vector file are newly created for this project, not imports of private payment screenshots. All identifiers and account names from the original payment sheet were excluded.

## Release sequence

1. Verify intended recipient ownership and explicit public-use permission for any Cash App, Venmo or PayPal destination **outside public GitHub**.
2. Compare each proposed public URL to its official provider destination and confirm the visible payee via human review. Do **not** send trial funds.
3. Review the entire PR diff, binary-image content, SVG, Git commit metadata, and rendered README/support page for unexpected disclosures.
4. Add only verified, approved destinations to `SUPPORT.md`. Add `.github/FUNDING.yml` only if provider-compatible URLs have been verified and an owner approves the GitHub Sponsors button.
5. Rerun exact QR decoding after any graphic changes. Rerun link checks **after** the support page is merged onto `main`.
6. Merge only after a separate human release decision. If not ready, keep the PR in draft.

## Explicit limitations

A scannable QR only proves a decode result, not that the intended page is live or that a future payee is verified. Static educational files do not create a transaction system, donation receipt process, or tax status. Previous QR-sheet scans and historical AI statements are not substitutes for current owner validation.

**Security note:** This report intentionally omits source computer paths, individual payment handles, contact identifiers, and sensitive QR payloads.
