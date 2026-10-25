# Public support QR verification — R4

**October 25, 2026 · static educational support notice · no recurring campaign**

## Authorized scope

Add a prominent README support section, an informational GitHub support page and one reusable social graphic for the Seraph IM & PLC public page. Keep the educational material free. This does **not** establish any financial or merchant service, recurring solicitation, payment receipt system, or business account.

## Exactly which links are encoded

| Image label | QR decoded destination | Destination class |
| --- | --- | --- |
| Cash App | `https://cash.app/$SeraphPLC?qr=1` | Public Cash App handle shown in owner-supplied screenshot |
| Venmo | `https://venmo.com/code?user_id=3164971651301376557&created=1792913852.040818` | Public Venmo code shown alongside @Michael-Burdge-4 |
| PayPal | `https://www.paypal.com/qrcodes/p2pqrc/3XHYCY3JZG3AC` | Public PayPal payment code shown with Michael Burdge |
| GitHub | `https://github.com/SeraphPLC/age-of-free-programming/blob/main/SUPPORT.md` | Official public documentation/support page |

These exact URLs were compared to the decoded owner-provided source images. They were independently re-encoded using native QR generation to avoid image-generation distortion. QR patterns were not recreated by image synthesis or artistic interpolation.

## Executed image QA

| Test | Result |
| --- | --- |
| Cash App exported standalone PNG | **PASS** — exactly one QR, exact text payload |
| Venmo exported standalone PNG | **PASS** — exactly one QR, exact text payload |
| PayPal exported standalone PNG | **PASS** — exactly one QR, exact text payload |
| GitHub exported standalone PNG | **PASS** — exactly one QR, exact text payload |
| Exported combined Facebook PNG | **PASS** — exactly four QRs, all four expected destinations |
| Hidden personal email / Zelle QR included | **NO** — excluded entirely |

The raster validation was performed on **exported PNG files**, not merely the vector source. Each exported QR is original software-generated geometry for the same public link. Exact URL decoding does not independently prove current receiving-account ownership, transaction eligibility, or successful transfer of money.

## Privacy and disclosure

The original Zelle QR's payload includes a personal payment email; **it cannot be made privacy-safe by removing only visible text**. No Zelle image or payload is included. No bank digits, account credentials, passwords, private network/machine routes, other household account QR codes, or private Seraph infrastructure are included.

The three published payment destinations are treated as **personal receiving options**, not business-verified payment accounts. Stay Golden Enterprises LLC has not been independently verified as the recipient of these codes. The supporter should verify the intended payee inside the provider's official app before any money is sent. The public document makes no charitable tax-deductibility claim.

## Publication gate and continuity

- Keep one Facebook post scoped to the named Seraph IM & PLC page rather than the owner's personal profile.
- Link the README graphic to `SUPPORT.md` and display the support options clearly near the beginning of the README.
- Verify the final GitHub `main` page and images through a live readback after the approved PR merges.
- A Facebook post must have a separately confirmed result and link; drafting or displaying the composer is not proof of successful publication.
- Avoid repeating an existing Facebook post if a browser operation times out; verify the page feed before retrying.

**Get Seraphed. The mission outlives the model.**
