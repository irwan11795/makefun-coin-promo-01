# TOPFUN logo — original robot artwork drawn with PIL in this session.
# Renamed from TOPBOT (user order 17:07 WIB); adds a gold "make.fun" banner
# across the top. Same design otherwise: a chunky robot standing on the #1
# step of a leaderboard podium, holding a gold "#1" flag, with a smaller
# robot climbing the steps beside it. Flat vector style, bold outlines,
# readable at thumbnail size.
from PIL import Image, ImageDraw, ImageFont

S = 2  # supersample factor
W = 1024 * S
img = Image.new("RGB", (W, W), (11, 16, 38))  # deep navy
d = ImageDraw.Draw(img, "RGBA")

NAVY = (11, 16, 38)
PANEL = (17, 26, 58)
PANEL2 = (14, 21, 48)
GOLD = (245, 179, 1)
GOLD_D = (201, 138, 0)
TEAL = (25, 184, 216)
TEAL_D = (13, 122, 148)
OUTLINE = (4, 32, 44)
CORAL = (255, 122, 89)
CORAL_D = (198, 74, 48)
WHITE = (255, 255, 255)
EYE = (190, 245, 255)
MUTED = (96, 116, 160)

try:
    FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    def font(n):
        return ImageFont.truetype(FB, int(n * S))
except Exception:
    def font(n):
        return ImageFont.load_default()


def rr(x0, y0, x1, y1, r, fill, outline=None, width=0):
    d.rounded_rectangle([x0 * S, y0 * S, x1 * S, y1 * S],
                        radius=r * S, fill=fill, outline=outline, width=int(width * S))


def circ(cx, cy, r, fill, outline=None, width=0):
    d.ellipse([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S],
              fill=fill, outline=outline, width=int(width * S))


def text_c(cx, y, s, f, fill):
    tb = d.textbbox((0, 0), s, font=f)
    w = tb[2] - tb[0]
    d.text(((cx - w / 2) * S, y * S), s, font=f, fill=fill)


# ---- leaderboard rows behind (subtle) ----
for i, y in enumerate(range(90, 700, 86)):
    d.rectangle([60 * S, y * S, 964 * S, (y + 58) * S],
                fill=PANEL if i % 2 == 0 else PANEL2)
    text_c(110, y + 8, str(i + 2), font(30), MUTED)
    # little score bars on the right of each row
    bw = [300, 260, 220, 180, 150, 120, 100, 90][i]
    rr(700, y + 18, 700 + bw, y + 40, 11, (38, 54, 96))

# ---- glow disc behind the hero robot ----
circ(512, 480, 300, (22, 34, 79))
circ(512, 480, 262, (26, 40, 92))

# ---- podium steps ----
# step 3 (left), step 1 (middle, tallest), step 2 (right)
rr(90, 844, 330, 1024, 14, (27, 35, 64), outline=GOLD_D, width=4)
rr(90, 844, 330, 884, 14, GOLD)
rr(360, 724, 664, 1024, 14, (27, 35, 64), outline=GOLD_D, width=4)
rr(360, 724, 664, 764, 14, GOLD)
rr(694, 784, 934, 1024, 14, (27, 35, 64), outline=GOLD_D, width=4)
rr(694, 784, 934, 824, 14, GOLD)
text_c(210, 898, "3", font(100), (150, 168, 210))
text_c(512, 830, "1", font(150), GOLD)
text_c(814, 880, "2", font(120), (150, 168, 210))

# ---- small climbing robot (right step) ----
sx, sy, sc = 814, 784, 0.52  # base position + scale
# body
rr(sx - 52 * sc, sy - 118 * sc, sx + 52 * sc, sy - 8 * sc, 22 * sc, CORAL,
   outline=OUTLINE, width=5 * sc)
# head
rr(sx - 46 * sc, sy - 196 * sc, sx + 46 * sc, sy - 118 * sc, 20 * sc, CORAL,
   outline=OUTLINE, width=5 * sc)
# antenna
d.line([(sx) * S, (sy - 196 * sc) * S, (sx + 26 * sc) * S, (sy - 232 * sc) * S],
       fill=GOLD, width=int(8 * sc * S))
circ(sx + 26 * sc, sy - 236 * sc, 11 * sc, GOLD, outline=OUTLINE, width=3 * sc)
# eyes + smile
rr(sx - 30 * sc, sy - 176 * sc, sx - 8 * sc, sy - 152 * sc, 8 * sc, EYE)
rr(sx + 8 * sc, sy - 176 * sc, sx + 30 * sc, sy - 152 * sc, 8 * sc, EYE)
d.arc([(sx - 16 * sc) * S, (sy - 146 * sc) * S, (sx + 16 * sc) * S,
       (sy - 124 * sc) * S], 15, 165, fill=OUTLINE, width=int(6 * sc * S))
# reaching arm up toward the #1 step
d.line([(sx - 52 * sc) * S, (sy - 84 * sc) * S, (sx - 108 * sc) * S,
        (sy - 168 * sc) * S], fill=CORAL_D, width=int(20 * sc * S))
circ(sx - 108 * sc, sy - 168 * sc, 14 * sc, CORAL, outline=OUTLINE, width=4 * sc)
# legs
rr(sx - 34 * sc, sy - 8 * sc, sx - 8 * sc, sy + 2 * sc, 6 * sc, CORAL_D)
rr(sx + 8 * sc, sy - 8 * sc, sx + 34 * sc, sy + 2 * sc, 6 * sc, CORAL_D)

# ---- hero robot (centre, on the #1 step) ----
hx, hy = 512, 724  # feet baseline
# legs
rr(hx - 62, hy - 74, hx - 16, hy, 10, TEAL_D)
rr(hx + 16, hy - 74, hx + 62, hy, 10, TEAL_D)
# left arm raised in victory
d.line([(hx - 82) * S, (hy - 190) * S, (hx - 148) * S, (hy - 330) * S],
       fill=TEAL_D, width=int(34 * S))
circ(hx - 148, hy - 330, 26, TEAL, outline=OUTLINE, width=6)
# body
rr(hx - 82, hy - 224, hx + 82, hy - 74, 30, TEAL, outline=OUTLINE, width=7)
# chest plate with 1
rr(hx - 50, hy - 196, hx + 50, hy - 118, 16, GOLD, outline=OUTLINE, width=5)
text_c(hx, hy - 192, "1", font(56), OUTLINE)
# head
rr(hx - 74, hy - 364, hx + 74, hy - 224, 30, TEAL, outline=OUTLINE, width=7)
# antenna
d.line([hx * S, (hy - 364) * S, hx * S, (hy - 424) * S], fill=GOLD,
       width=int(10 * S))
circ(hx, hy - 436, 20, GOLD, outline=OUTLINE, width=5)
# eyes (big, glowing)
rr(hx - 54, hy - 330, hx - 10, hy - 282, 12, EYE, outline=OUTLINE, width=4)
rr(hx + 10, hy - 330, hx + 54, hy - 282, 12, EYE, outline=OUTLINE, width=4)
circ(hx - 32, hy - 306, 9, OUTLINE)
circ(hx + 32, hy - 306, 9, OUTLINE)
# smile grille
d.arc([(hx - 26) * S, (hy - 268) * S, (hx + 26) * S, (hy - 238) * S],
      15, 165, fill=OUTLINE, width=int(7 * S))
# right arm holding the flag pole
d.line([(hx + 82) * S, (hy - 190) * S, (hx + 128) * S, (hy - 300) * S],
       fill=TEAL_D, width=int(34 * S))
circ(hx + 128, hy - 300, 24, TEAL, outline=OUTLINE, width=6)
# flag pole + gold flag
d.line([(hx + 128) * S, (hy - 300) * S, (hx + 128) * S, (hy - 470) * S],
       fill=GOLD_D, width=int(10 * S))
d.polygon([(hx + 128) * S, (hy - 470) * S, (hx + 258) * S, (hy - 438) * S,
           (hx + 128) * S, (hy - 406) * S], fill=GOLD, outline=OUTLINE)
text_c(hx + 196, hy - 460, "#1", font(40), OUTLINE)

# ---- gold sparkles ----
def star(cx, cy, r, fill):
    d.polygon([(cx) * S, (cy - r) * S, (cx + r * 0.28) * S, (cy - r * 0.28) * S,
               (cx + r) * S, cy * S, (cx + r * 0.28) * S, (cy + r * 0.28) * S,
               cx * S, (cy + r) * S, (cx - r * 0.28) * S, (cy + r * 0.28) * S,
               (cx - r) * S, cy * S, (cx - r * 0.28) * S, (cy - r * 0.28) * S],
              fill=fill)

star(300, 300, 26, GOLD)
star(724, 250, 20, GOLD)
star(250, 560, 16, GOLD)
star(790, 560, 22, GOLD)
star(512, 150, 18, GOLD)

# ---- "make.fun" banner across the top (user order 17:07 WIB) ----
banner_text = "make.fun"
bf = font(48)
tb = d.textbbox((0, 0), banner_text, font=bf)
bw = tb[2] - tb[0]
bx0, bx1 = 512 - bw / 2 - 46, 512 + bw / 2 + 46
rr(bx0, 20, bx1, 82, 26, GOLD, outline=OUTLINE, width=5)
text_c(512, 27, banner_text, bf, OUTLINE)

img = img.resize((1024, 1024), Image.LANCZOS)
img.save("/home/hatch/workspace/makefun/new-bounties/makefun-coin-promo-01/logo.png",
         "PNG", optimize=True)
print("logo.png written")
