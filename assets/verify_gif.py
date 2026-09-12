from PIL import Image
import os

im = Image.open("assets/social-preview.gif")
sz = os.path.getsize("assets/social-preview.gif")
print("dims:", im.size, "| frames:", im.n_frames, "| bytes:", sz, "| under 1MB:", sz < 1_000_000)

# Verify 50px top/bottom padding: scan every frame for non-background pixels
# in the padding bands y in [0,50) and (270,320). Background is animated, so
# sample the local background per frame; also tolerance-check to ignore the
# smooth gradient (only flag rows that deviate strongly from the band's own bg).
def row_dev(rgb, y):
    # Real elements (cyan border/bubbles/text) differ from the dark bg by
    # ~500 in summed channel distance; GIF dither noise is far smaller.
    # Flag rows with >=5 pixels deviating by >150 from the row's modal color.
    from collections import Counter
    px = [rgb.getpixel((x, y)) for x in range(0, 640, 2)]
    ref = Counter(px).most_common(1)[0][0]
    return sum(1 for p in px if sum(abs(a - b) for a, b in zip(p, ref)) > 150) >= 5

worst_top, worst_bot = 999, 999
worst_dev = 0
for i in range(im.n_frames):
    im.seek(i)
    rgb = im.convert("RGB")
    for y in list(range(0, 50)) + list(range(271, 320)):
        from collections import Counter
        px = [rgb.getpixel((x, y)) for x in range(0, 640, 2)]
        ref = Counter(px).most_common(1)[0][0]
        dev = max(sum(abs(a - b) for a, b in zip(p, ref)) for p in px)
        worst_dev = max(worst_dev, dev)
        if sum(1 for p in px if sum(abs(a - b) for a, b in zip(p, ref)) > 150) >= 5:
            if y < 50:
                worst_top = min(worst_top, y)
            else:
                worst_bot = min(worst_bot, 320 - y)
print("max deviation in padding bands (dither noise if <150):", worst_dev)
print("clear padding top:", (str(worst_top) + " px (FAIL)") if worst_top < 999 else ">= 50 px OK")
print("clear padding bottom:", (str(worst_bot) + " px (FAIL)") if worst_bot < 999 else ">= 50 px OK")
