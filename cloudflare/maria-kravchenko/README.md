# Maria — Cloudflare Worker preparation, NOT deployed

Baseline: RiakhinA/riakhin-card-share-qr-test commit ab9dd3f9cb161a769341dc2fe8a41e0f0e4cd474; isolated NONPROD implementation only.

* Proposed Worker name maria-kravchenko (unreserved/unapproved).
* Proposed URL https://maria-kravchenko.my-webcard.workers.dev/ (NOT live or canonical until approved and verified).
* Current interim canonical URL in maria/site-config.json: https://riakhin-card-preview.vercel.app/maria/.
* Local assets root: maria/. This becomes / (site root) on the dedicated Worker, unlike Vercel's /maria/.
* maria/contact-ru.vcf and maria/contact-uk.vcf are generated from that config and the existing JPEG via python3 scripts/build_maria_vcf.py.
* The contact QR (vCard with only VERSION/FN/TEL/URL) and regular QR both use publicCardUrl, not location.href.
* Share sends the same localized static VCF bytes as Save. Unsupported Web Share file flow falls back to the same VCF download.

## Authorized release procedure — only after separate Owner approval

1. Freeze the accepted NONPROD commit, verify its parent and absence of unrelated diffs. Recheck linked Vercel production source. Never merge automatically.
2. Verify Cloudflare account, subdomain, name availability, and whether another Worker named maria-kravchenko exists; STOP on any ambiguity. Don't touch Anton/Iryna.
3. Make and hash backup of current Vercel /maria/ assets and the NONPROD candidate.
4. After explicit approval of the actual new URL, change only maria/site-config.json.publicCardUrl to https://maria-kravchenko.my-webcard.workers.dev/ (if that is really the confirmed account/address). Run python3 scripts/build_maria_vcf.py. Confirm portrait hash, phone and channel URLs unchanged.
5. Using the existing local Wrangler, from cloudflare/maria-kravchenko execute a dry run and inspect the asset manifest. Confirm exact deploy target/account and no other Worker scope.
6. With separate Owner authorization only, deploy this Worker and test HTTP/SHA, contact VCF PHOTO JPEG decoding, URL fields, Save/Share, both QR contents, RU/UA, desktop/mobile browser. The QR and both VCF should now use the approved Worker URL.
7. Keep the Vercel /maria/ alias alive during rollout. If the new Worker fails, cease promoting the Worker link, return people to the known-good Vercel alias; if an older Maria Worker version was present, rollback to its verified backed-up version. Never delete or replace Anton/Iryna Workers.

No production action is authorized by these instructions.
