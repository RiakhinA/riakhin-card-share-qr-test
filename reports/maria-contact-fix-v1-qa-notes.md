# Maria Contact Fix V1 — NONPROD QA, 2026-10-10

## Verified source
- Live Vercel project production deployment: dpl_Ch9JU9dPYorgmvDzAofRtdqBW7CD
- GitHub repository: RiakhinA/riakhin-card-share-qr-test
- Branch: main (read-only baseline)
- Source commit: ab9dd3f9cb161a769341dc2fe8a41e0f0e4cd474
- The live deployed HTML, config and portrait each matched the exact byte contents of this commit.
- Live HTML SHA256 e9f5897f83538543ac4f270078c28690bbad2a4926c873950e9a4d209604dc3e.
- Live portrait SHA256 6b5729b2c958a0eec33ece35c4b27fb1e4ee4eb94953459f8063c4dd68a7806b.

## Static QA
PASS: two localized vCards (vCard 3.0) contain explicit interim canonical URL, correct FN/N/TEL, Instagram/Telegram/WhatsApp/Viber, intact identical 113256-byte JPEG PHOTO. Physical folding <=75 bytes per line, CRLF syntax, valid base64. VCF sizes: RU 157897 bytes; UK 157907 bytes.
PASS: all five JS blocks passed node --check. CSS source unchanged; portrait unchanged. No window.location.href fallback.
PASS: proposed Wrangler config points to only the Maria assets root; no deployment executed.

## Real Chrome / Puppeteer against isolated local static server
See maria-contact-fix-v1-browser-qa.json.
20 PASS, 1 strict screenshot-difference threshold FAIL; test process completed with exit code 0.
PASS: real download RU/UA with exact VCF hashes.
PASS: Web Share files mocked via browser API and exact byte hash matches same locale VCF.
PASS: fallback downloaded same full locale VCF.
PASS: contact QR SVG path payload matches rendered QR for both languages; its vCard contains VERSION/FN/TEL/URL and no PHOTO.
PASS: original regular QR encodes interim canonical link in both locales.
PASS: RU/UA text, no horizontal overflow mobile/desktop, zero browser JS exceptions.
PASS: CSS exact match to live original.
VISUAL REVIEW NEEDED: strict screenshot test threshold failed (2923 RGB channels different from 913500). A separate image comparison of the latest captured pair found differences on 977 pixels confined to rows y=108..121 on a 375x812 screenshot; the original CSS and portrait remain byte-identical, with no DOM redesign. Owner visual acceptance remains required; this is not claimed as pixel-perfect identical.

## Not tested / limits
- Physical iOS/Android import and native camera QR scanning: NOT_TESTED.
- Real system share sheet: NOT_TESTED. Browser mock validated bytes submitted to Web Share API.
- Proposed Cloudflare Worker name returned HTTP 404, but name availability/ownership cannot be confirmed without account-level inspection. Status: UNVERIFIED.
- Wrangler binary was not found in the inspected local existing tool paths; deploy dry-run: NOT_TESTED.
- NO Cloudflare worker creation, deploy, Vercel production update, main merge, or existing Anton/Iryna Worker mutation performed.

PRODUCTION_DEPLOY=FORBIDDEN; OWNER_REVIEW=REQUIRED.
