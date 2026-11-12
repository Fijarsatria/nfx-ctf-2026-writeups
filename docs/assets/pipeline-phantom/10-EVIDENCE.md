# Pipeline Phantom — bukti publik (2026-11-13)

Repo: https://github.com/netmetrics-net/c2-deploy-pipeline

## Yang berhasil diambil tanpa login

| Artefak | Isi |
|---|---|
| Repo API | repo publik, default branch `main` |
| Run | `40221200390` — "Deploy C2 Infrastructure", `workflow_dispatch`, success |
| Job | `121252951677` — "Build & Edge Deployment", success |
| Issue #1 | "[SECURITY AUDIT] Reverted temporary branch: Credential leak prevented" |
| Commit reverted | `62d3ad55d0cd1d95c64fc0168e317b928b0b4d95` |
| File di commit itu | `config/c2_endpoint.json` |

Issue #1 menyebut branch `feature/credential-cleanup` sudah dihapus dan
commit `62d3ad55...` sudah di-revert.

## Fragmen dari commit yang di-revert

`config/c2_endpoint.json` pada commit `62d3ad55...`:

```json
{
  "endpoint": "https://c2.veloxphantom.net/gate",
  "backup_key_fragment": "4nd_0rph4n_c0mm1t_l34k_9f82}",
  "cluster_auth": "bearer-velox-staging-token",
  "last_verified_utc": "2026-10-25T14:30:00Z"
}
```

## Mekanisme kebocoran di workflow

`.github/workflows/deploy.yml` (main) memuat:

```yaml
- name: Validate Deployment Secrets
  env:
    C2_KEY: ${{ secrets.C2_API_KEY }}
  run: |
    echo "[*] Initializing automated infrastructure sync..."
    echo "[*] Authenticating with regional telemetry clusters..."
    # Debug step: print transformed string (bypasses GitHub exact-match secret masking)
    echo -n "[DEBUG_PAYLOAD]: "
    echo "$C2_KEY" | sed 's/./& /g'
```

`sed 's/./& /g'` memberi spasi di antara karakter, sehingga GitHub tidak
mencocokkan exact-match secret dan nilai asli muncul di log. Inilah sumber
fragmen pertama:

```text
NFX{gh_4ct10ns_m4sk_byp4ss_
```

## Kenapa log mentah tidak ada di sini

Endpoint log resmi:

```text
GET /repos/netmetrics-net/c2-deploy-pipeline/actions/runs/40221200390/logs
```

dijawab:

```json
{"message":"Must have admin rights to Repository.","status":403}
```

Jadi log mentah butuh hak admin repo. Yang bisa dibuktikan publik adalah
workflow source (mekanisme), issue (commit reverted), dan isi file di commit
itu (fragmen kedua). Fragmen pertama hanya ada di report arsip
`Pipeline_Phantom.report.txt`.

## Flag

```text
NFX{gh_4ct10ns_m4sk_byp4ss_4nd_0rph4n_c0mm1t_l34k_9f82}
```

Status bukti: **kuat untuk mekanisme dan fragmen kedua; fragmen pertama
berasal dari report arsip, bukan log mentah yang bisa diunduh publik.**
