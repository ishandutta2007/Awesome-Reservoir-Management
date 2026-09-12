"""Generate the 640x320 animated GIF social preview (requires Pillow).

Content is inset 50px top and bottom so GitHub's social preview crop
never clips the artwork. Output: assets/social-preview.gif (< 1 MB).
"""
from PIL import Image, ImageDraw, ImageFont
import math
import os

W, H, TOP, BOT = 640, 320, 50, 270


def load(sz, bold=True):
    names = ["arialbd.ttf", "segoeuib.ttf", "DejaVuSans-Bold.ttf"] if bold else ["arial.ttf", "segoeui.ttf", "DejaVuSans.ttf"]
    for n in names:
        try:
            return ImageFont.truetype(n, sz)
        except Exception:
            pass
    return ImageFont.load_default()


fT, fS, fK = load(40), load(18), load(12)


def phase(i, N, span):
    return (1 + math.sin(2 * math.pi * i / N - math.pi / 2)) / 2 * span


def gen(N, colors, duration):
    frames = []
    for i in range(N):
        t = i / N
        p = phase(i, N, 1)
        r, g, b = int(7 + 7 * p), int(24 + 16 * p), int(43 + 21 * p)
        im = Image.new("RGB", (W, H), (r, g, b))
        d = ImageDraw.Draw(im)
        gy = int(140 + 25 * p)
        d.rectangle([0, gy - 22, W, gy + 22], fill=(min(r + 4, 255), min(g + 8, 255), min(b + 10, 255)))
        d.rounded_rectangle([3, 3, W - 4, H - 4], radius=9, outline=(103, 232, 249), width=1)

        def strata(y0, a1, a2, sp, drift, color):
            pts = [(-12, H + 12)]
            x = -12
            while x <= W + 12:
                y = (y0 + a1 * math.sin(x * sp + 2 * math.pi * t * drift)
                     + a2 * math.sin(x * sp * 0.53 + 1.2 + 2 * math.pi * t * drift * 0.7))
                pts.append((x, y))
                x += 14
            pts.append((W + 12, H + 12))
            d.polygon(pts, fill=color)

        strata(236, 5, 3, 0.020, 1.0, (18, 96, 116))
        strata(248, 4, 3, 0.024, -1.3, (15, 118, 138))
        strata(259, 3, 2, 0.030, 0.8, (19, 142, 152))

        bubbles = [(75, 5, 11.0, 0.0), (150, 4, 8.0, 1.5), (235, 6, 13.0, 0.8), (330, 4, 7.0, 2.6),
                   (410, 5, 10.0, 4.2), (490, 4, 9.0, 3.1), (565, 6, 12.0, 5.5), (610, 3, 6.5, 0.4)]
        for bx, br, dur, beg in bubbles:
            u = ((t * 40 * (80 / duration) - beg) % dur) / dur
            y = 262 - u * (262 - (TOP + 22 + br))
            a = min(u / 0.35, 1.0) * (1 - u)
            col = tuple(int(c * 0.55 * a) for c in (103, 232, 249))
            d.ellipse([bx - br, y - br, bx + br, y + br], fill=col)

        d.text((W / 2 + 2, 96 + 2), "Awesome Reservoir Management", font=fT, fill=(0, 0, 0), anchor="mm")
        d.text((W / 2, 96), "Awesome Reservoir Management", font=fT, fill=(240, 249, 255), anchor="mm")
        x0 = int(W * 0.5 + W * 0.5 * p) - 150
        d.rectangle([x0, 126, min(x0 + 300, W - 40), 129], fill=(34, 211, 238))
        d.text((W / 2, 156), "Commercial Platforms & Open-Source Subsurface Software", font=fS, fill=(159, 211, 232), anchor="mm")
        d.text((W / 2, 186), "RESERVOIR SIMULATION  \u2022  GEOMODELING  \u2022  OIL & GAS  \u2022  GEOTHERMAL  \u2022  CO2 STORAGE", font=fK, fill=(123, 169, 194), anchor="mm")
        for k in range(7):
            dx = 200 + k * 40
            a = 0.5 + 0.5 * math.sin(2 * math.pi * t + k)
            col = tuple(int(c * a) for c in (103, 232, 249))
            d.ellipse([dx - 2, 212 - 2, dx + 2, 212 + 2], fill=col)
        frames.append(im)

    pal = frames[0].quantize(colors=colors, method=Image.MEDIANCUT)
    qframes = [f.quantize(palette=pal, dither=Image.FLOYDSTEINBERG) for f in frames]
    out = "assets/social-preview.gif"
    qframes[0].save(out, save_all=True, append_images=qframes[1:], duration=duration, loop=0, optimize=True)
    return os.path.getsize(out)


if __name__ == "__main__":
    size = gen(40, 32, 80)
    if size > 950_000:
        size = gen(24, 24, 110)
    print("GIF bytes:", size, "| KB:", round(size / 1024, 1), "| dims:", Image.open("assets/social-preview.gif").size)
