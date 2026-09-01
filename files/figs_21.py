# -*- coding: utf-8 -*-
"""Chapter 21's two non-map figures.

  svg_partition.txt  the 1544 division of the duchies: revenue split three ways
                     over one undivided territory
  svg_tollgame.txt   the Sound toll after 1567: declare a value, and risk being
                     taken at your word

Both deliberately carry what the prose cannot. The partition figure exists
because "the revenue was divided and the territory was not" is a sentence people
read past; seeing the same outline speckled three ways makes it land. The toll
figure exists because an incentive mechanism is a shape, not a narrative.

Run: python3 figs_21.py   -> writes both .txt and rasterises both to look_*.png
"""
import mapspine as M

INK = "#3C3E36"
PAPER = "#F0F2EE"
RULE = "#C9CDC4"
OX = "#8A2B2B"          # part F colour, used for the king's share and for loss
VERD = "#2E6B5E"
AMBER = "#A9601C"
MUTED = "#5F6157"

# The three shares of 1544. Adolf chose first, being youngest.
SHARES = [("Royal share", "Christian 3.", OX),
          ("Haderslev", "Hans the Elder", VERD),
          ("Gottorp", "Adolf \u2014 chose first", AMBER)]


# --------------------------------------------------------------- figure 2
def partition():
    W, H = 700, 428
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Diagram of the 1544 partition of Schleswig and Holstein. On the left, '
         'the territorial division the knighthood refused: three contiguous blocks. On the '
         'right, what was done instead: one undivided territory whose districts are assigned '
         'to three roughly equal revenue shares, interleaved so that no share forms a '
         'contiguous block, under a joint government.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))

    # a schematic duchy outline, reused on both sides: Eider country, wide north,
    # narrowing south. Not a map - deliberately, so nobody measures it.
    def outline(ox, oy):
        return ("M %d %d L %d %d L %d %d L %d %d L %d %d L %d %d Z"
                % (ox + 18, oy, ox + 190, oy, ox + 206, oy + 74,
                   ox + 166, oy + 168, ox + 54, oy + 168, ox + 2, oy + 78))

    o.append('<text x="26" y="30" class="mapl">WHAT THE KNIGHTHOOD REFUSED</text>')
    o.append('<text x="382" y="30" class="mapl">WHAT WAS DONE INSTEAD</text>')
    o.append('<text x="26" y="46" class="mapt">three contiguous duchies</text>')
    o.append('<text x="382" y="46" class="mapt">one territory, three purses</text>')

    # ---- left: contiguous blocks, struck through
    lx, ly = 30, 62
    o.append('<clipPath id="cl"><path d="%s"/></clipPath>' % outline(lx, ly))
    for i, (name, who, col) in enumerate(SHARES):
        y = ly + i * 56
        o.append('<rect x="%d" y="%d" width="230" height="56" fill="%s" opacity=".45" '
                 'clip-path="url(#cl)"/>' % (lx - 2, y, col))
    # the strike goes UNDER the outline and the labels, or it obscures them
    for a, b in (((lx - 6, ly - 6), (lx + 214, ly + 176)),
                 ((lx + 214, ly - 6), (lx - 6, ly + 176))):
        o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2" '
                 'opacity=".5"/>' % (a[0], a[1], b[0], b[1], MUTED))
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="1.4"/>'
             % (outline(lx, ly), INK))
    for i, (name, who, col) in enumerate(SHARES):
        o.append('<text x="%d" y="%d" class="mapl" text-anchor="middle">%s</text>'
                 % (lx + 104, ly + 34 + i * 56, name.upper()))
    o.append('<text x="%d" y="%d" class="mapt" text-anchor="middle">a divided '
             'Schleswig-Holstein would be two</text>' % (lx + 104, ly + 200))
    o.append('<text x="%d" y="%d" class="mapt" text-anchor="middle">nobilities and two sets of '
             'privileges</text>' % (lx + 104, ly + 213))

    # ---- right: one outline, districts speckled three ways
    rx, ry = 386, 62
    o.append('<clipPath id="cr"><path d="%s"/></clipPath>' % outline(rx, ry))
    o.append('<path d="%s" fill="#E4E7DE" clip-path="url(#cr)"/>' % outline(rx, ry))
    # 40 districts on a jittered grid, cycled through the three shares so that no
    # two neighbours reliably match - the interleaving IS the argument
    order = [0, 2, 1, 2, 0, 1, 1, 0, 2, 1, 2, 0, 2, 1, 0, 0, 2, 1,
             1, 2, 0, 2, 0, 1, 0, 1, 2, 1, 0, 2, 2, 0, 1, 0, 1, 2]
    k = 0
    for row in range(6):
        for col in range(6):
            x = rx + 14 + col * 31 + (6 if row % 2 else 0)
            y = ry + 10 + row * 26
            c = SHARES[order[k % len(order)]][2]
            k += 1
            o.append('<rect x="%d" y="%d" width="26" height="21" rx="2" fill="%s" '
                     'opacity=".62" clip-path="url(#cr)"/>' % (x, y, c))
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="1.4"/>'
             % (outline(rx, ry), INK))
    o.append('<text x="%d" y="%d" class="mapt" text-anchor="middle">every district assigned to a '
             'share; no share contiguous;</text>' % (rx + 104, ry + 200))
    o.append('<text x="%d" y="%d" class="mapt" text-anchor="middle">courts, defence and the Empire '
             'governed jointly</text>' % (rx + 104, ry + 213))

    # ---- the three purses, equal by construction
    py = 300
    o.append('<line x1="26" y1="%d" x2="674" y2="%d" stroke="%s" stroke-width="1"/>'
             % (py - 14, py - 14, RULE))
    o.append('<text x="26" y="%d" class="mapl">THREE SHARES, VALUED EQUAL</text>' % (py + 2))
    for i, (name, who, col) in enumerate(SHARES):
        x = 26 + i * 218
        o.append('<rect x="%d" y="%d" width="196" height="15" fill="%s" opacity=".62"/>'
                 % (x, py + 14, col))
        o.append('<text x="%d" y="%d" class="mapx">%s</text>' % (x, py + 44, name))
        o.append('<text x="%d" y="%d" class="mapt">%s</text>' % (x, py + 58, who))
    o.append('<text x="26" y="%d" class="mapt">The estates would not let the land be cut, so the '
             'income was cut instead. The parcels making up</text>' % (py + 82))
    o.append('<text x="26" y="%d" class="mapt">each third lay scattered the length of both '
             'duchies, and could not be untangled again until 1773.</text>' % (py + 95))
    o.append('</svg>')
    return "\n  ".join(o)


# --------------------------------------------------------------- figure 3
def tollgame():
    W, H = 700, 356
    o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Diagram of the Sound toll mechanism introduced in 1567. A skipper at '
         'Helsingoer declares the value of his cargo. The toll is one to two per cent of that '
         'declared value, but the crown reserves the right to buy the cargo outright at the '
         'price declared. Declaring low risks losing the cargo cheaply; declaring high means '
         'paying toll on an invented figure.">' % (W, H)]
    o.append('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, H, PAPER))
    o.append('<text x="26" y="30" class="mapl">HELSING\u00d8R, AFTER 1567</text>')
    o.append('<text x="26" y="46" class="mapt">the skipper is asked one question, and both '
             'answers cost him</text>')

    # the question
    o.append('<rect x="252" y="64" width="196" height="42" rx="3" fill="none" stroke="%s" '
             'stroke-width="1.2"/>' % INK)
    o.append('<text x="350" y="82" class="mapl" text-anchor="middle">What is the cargo</text>')
    o.append('<text x="350" y="97" class="mapl" text-anchor="middle">worth?</text>')

    # two branches
    for x0, x1, lab, col in [(350, 158, "DECLARE LOW", OX), (350, 542, "DECLARE HIGH", VERD)]:
        o.append('<path d="M %d 106 C %d 130, %d 130, %d 152" fill="none" stroke="%s" '
                 'stroke-width="1.2" opacity=".8"/>' % (x0, x0, x1, x1, col))
        o.append('<text x="%d" y="170" class="mapl" text-anchor="middle" fill="%s">%s</text>'
                 % (x1, col, lab))

    boxes = [(158, OX, "The crown may buy the cargo",
              "at the price you just named.", "You lose the goods for a",
              "fraction of their worth."),
             (542, VERD, "The toll is a percentage of",
              "the figure you just named.", "You pay on a value you",
              "invented.")]
    for cx, col, a, b, c, d in boxes:
        o.append('<rect x="%d" y="182" width="260" height="86" rx="3" fill="%s" opacity=".10"/>'
                 % (cx - 130, col))
        o.append('<rect x="%d" y="182" width="260" height="86" rx="3" fill="none" stroke="%s" '
                 'stroke-width="1" opacity=".55"/>' % (cx - 130, col))
        for i, t in enumerate((a, b, c, d)):
            cls = "mapx" if i < 2 else "mapt"
            o.append('<text x="%d" y="%d" class="%s" text-anchor="middle">%s</text>'
                     % (cx, 202 + i * 17, cls, t))

    o.append('<line x1="26" y1="288" x2="674" y2="288" stroke="%s" stroke-width="1"/>' % RULE)
    o.append('<text x="26" y="306" class="mapx">Rate from 1567: roughly 1\u20132 per cent of '
             'declared value, varying by goods, decade and flag.</text>')
    o.append('<text x="26" y="322" class="mapt">Modern work in mechanism design finds the rule '
             'does not actually make honesty optimal \u2014</text>')
    o.append('<text x="26" y="336" class="mapt">only that it lets the crown implement whatever '
             'effective rate it is aiming at.</text>')
    o.append('</svg>')
    return "\n  ".join(o)


if __name__ == "__main__":
    for name, fn in (("svg_partition.txt", partition), ("svg_tollgame.txt", tollgame)):
        svg = fn()
        open(name, "w", encoding="utf-8").write(svg)
        M.rasterise(svg, "look_" + name.replace("svg_", "").replace(".txt", ".png"))
        print("wrote %s (%d chars)" % (name, len(svg)))
