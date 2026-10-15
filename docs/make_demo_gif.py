"""Generate docs/demo.gif — deterministic terminal-style A-Z demo.

Verified pipeline per 2026 GIF guidance (agg/VHS alternative when no TTY):
script -> frames -> optimized GIF, <=30s equivalent, title card first,
one workflow per GIF, alt text supplied in README (accessibility).
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 900, 520
BG = (40, 42, 54)      # Dracula background
FG = (248, 248, 242)
GREEN = (80, 250, 123)
CYAN = (139, 233, 253)
RED = (255, 85, 85)
YELLOW = (241, 250, 140)

FRAMES = [
    (CYAN, "Stale Secrets — A-Z in 25 seconds"),
    (FG, "$ git clone <public repo> && cd demo"),
    (FG, "$ gitleaks git --redact .   # scans HISTORY"),
    (RED, "Finding: .env @ b44832f  RuleID: api-token"),
    (FG, "$ git show b44832f:.env  # deleted != erased"),
    (YELLOW, "API_TOKEN=ds_live_*** (REDACTED)"),
    (FG, '$ curl -H "Authorization: Bearer ..." /api/customers'),
    (GREEN, "200 OK  3 customers (ids, company, headcount)"),
    (CYAN, "FIX: rotate FIRST (old -> 401)"),
    (FG, "$ git filter-repo --replace-text pw.txt --force"),
    (GREEN, "rescan: 0 findings   old token: 401  PASS"),
]

try:
    FONT = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 20)
    BIG = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", 24)
except Exception:
    FONT = BIG = ImageFont.load_default()

imgs = []
history = []
for color, line in FRAMES:
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 56], fill=(68, 71, 90))
    d.text((20, 14), "lab — stale-secrets demo (synthetic tokens only)", font=FONT, fill=CYAN)
    history = (history + [line])[-9:]
    y = 80
    for h in history:
        last = h == line
        d.text((24, y), ("$ " if h.startswith("$") else "  ") + h.lstrip("$ "),
               font=BIG if last else FONT, fill=color if last else (150, 150, 150))
        y += 44
    imgs.append(img)

out = "/home/md/src/secrets-leakage-gitleaks-phd-2026/docs/demo.gif"
imgs[0].save(out, save_all=True, append_images=imgs[1:], duration=900, loop=0,
             optimize=True, colors=128)
print("wrote", out)
