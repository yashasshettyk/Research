"""Build the one-page Home Guardian summary PDF.
Run: python3 analysis/make_one_pager.py  ->  paper/drafts/home-guardian-one-pager.pdf
Content source: notes/design/home-guardian-v1.md + literature/notes/wifi-fall-detection.md
"""
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer

F = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV", F + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", F + "DejaVuSans-Bold.ttf"))
for b, i, name in [(0, 0, "DV"), (1, 0, "DVB"), (0, 1, "DV"), (1, 1, "DVB")]:
    addMapping("DV", b, i, name)

NAVY = colors.HexColor("#1F3A5F")
TEAL = colors.HexColor("#1B7F6B")
TEAL_BG = colors.HexColor("#E7F5F1")
RED = colors.HexColor("#B03A2E")
RED_BG = colors.HexColor("#FBECEA")
GREY_BG = colors.HexColor("#F3F5F8")
LINE = colors.HexColor("#C9D2DD")

W, H = A4
M = 26  # page margin
OUT = "paper/drafts/home-guardian-one-pager.pdf"

def S(name, size=8, lead=None, color=colors.black, font="DV", **kw):
    return ParagraphStyle(name, fontName=font, fontSize=size, leading=lead or size * 1.28,
                          textColor=color, **kw)

body = S("body", 8.4)
small = S("small", 7.2)
tiny = S("tiny", 6.0, color=colors.HexColor("#444444"))
h = S("h", 10.2, font="DVB", color=NAVY, spaceAfter=1.5)
cell = S("cell", 7.3, alignment=TA_CENTER)
cellL = S("cellL", 7.3)
flow = S("flow", 7.6, alignment=TA_CENTER)

def P(t, st=body):
    return Paragraph(t, st)

def box(items, bg=GREY_BG, border=LINE, width=None):
    t = Table([[items]], colWidths=[width])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg), ("BOX", (0, 0), (-1, -1), 0.7, border),
        ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    return t

def two(left, right, gap=8):
    cw = (W - 2 * M - gap) / 2
    t = Table([[box(left, width=cw) if isinstance(left, list) else left, "",
                box(right, width=cw) if isinstance(right, list) else right]],
              colWidths=[cw, gap, cw])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                           ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    return t

def header(c, doc):
    c.saveState()
    c.setFillColor(NAVY)
    c.rect(0, H - 62, W, 62, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("DVB", 19)
    c.drawString(M, H - 32, "Home Guardian")
    c.setFont("DV", 9.2)
    c.drawString(M, H - 49, "A self-learning Wi-Fi system that protects elders and empty homes. "
                            "No camera. Nothing to wear.")
    c.setFont("DV", 7.2)
    c.drawRightString(W - M, H - 22, "Shravya Shetty  |  M.Tech CSE project")
    c.drawRightString(W - M, H - 33, "One-page summary  |  Nov 2026 (design stage)")
    c.setFillColor(colors.HexColor("#666666"))
    c.setFont("DV", 5.8)
    c.drawCentredString(W / 2, 12, "Paper figures are the authors' own reports. Home Guardian figures are targets, "
                                   "not results yet. Uniqueness is based on our search so far.")
    c.restoreState()

story = []
CW = W - 2 * M
half = (CW - 8) / 2

# Row 1: what it is + why useful
story.append(two(
    [P("What it is", h),
     P("Small, cheap <b>ESP32 Wi-Fi boards</b> (about Rs. 400-800 each) are placed around the home. "
       "When a person moves, the Wi-Fi signal between the boards changes a little. "
       "An <b>AI model</b> reads these tiny changes (called <b>CSI</b>: the fine details of a Wi-Fi signal) "
       "and understands what is happening: walking, sitting, lying, a fall, or a stranger walking in."),
     P("It <b>learns each home's own pattern</b> and keeps getting better every night.", body)],
    [P("Why it is useful", h),
     P("&bull; About <b>684,000 people die from falls</b> every year; over 80% of them in low- and "
       "middle-income countries like India (WHO).<br/>"
       "&bull; Many elders live alone. After a fall they may lie on the floor for hours.<br/>"
       "&bull; Cameras feel like spying, and wearables get forgotten or are not charged. "
       "This needs <b>neither</b>.<br/>"
       "&bull; The <b>same boards also guard the empty house</b> against theft, so families get "
       "two products for the price of one.")]))
story.append(Spacer(1, 6))

# Row 2: two modes
g = [P("<font color='#1B7F6B'>GUARDIAN MODE</font>  (family at home)", S("gh", 8.6, font="DVB")),
     P("&bull; Detects a <b>fall</b>, a <b>very long stillness</b> (e.g. 40 min in the bathroom) and an "
       "<b>unusual routine</b> (e.g. no movement by 9 am).<br/>"
       "&bull; Speaker asks <b>\"Are you OK?\"</b>. If there is no reply, it calls or sends an SMS to the family.")]
t = [P("<font color='#B03A2E'>THEFT MODE</font>  (house empty or at night)", S("th", 8.6, font="DVB")),
     P("&bull; Detects <b>any person moving</b> and tells <b>which floor and room</b>.<br/>"
       "&bull; Ignores pets, fans and curtains. Knows <b>family from stranger</b> (phones + walking style). "
       "If it's a stranger: alarm + phone alert.")]
story.append(P("What it does: two modes, one system", h))
story.append(two(box(g, TEAL_BG, TEAL, half), box(t, RED_BG, RED, half)))
story.append(Spacer(1, 2))
story.append(P("<b>Auto switch:</b> when every family phone leaves the home Wi-Fi it switches to Theft mode; "
               "when a known phone comes back it switches to Guardian mode. Night mode can use both.", small))
story.append(Spacer(1, 6))

# Row 3: how it works (flow)
story.append(P("How it works", h))
steps = [("1. Sense", "Boards record the Wi-Fi signal 100 times a second"),
         ("2. Clean", "Remove noise and sudden spikes"),
         ("3. AI brain", "Turns each 2-sec clip into a \"movement fingerprint\""),
         ("4. Three answers", "What is happening? Is it normal for this home? Where and who?"),
         ("5. Double check", "2 boards must agree, then the voice check"),
         ("6. Alert + live map", "Phone alert; live house map with moving dots")]
row, widths = [], []
bw, aw = (CW - 5 * 11) / 6, 11
for i, (a, b) in enumerate(steps):
    row.append(Paragraph(f"<b>{a}</b><br/>{b}", flow))
    widths.append(bw)
    if i < 5:
        row.append(Paragraph("<b>&rarr;</b>", S("ar", 11, color=NAVY, alignment=TA_CENTER)))
        widths.append(aw)
ft = Table([row], colWidths=widths)
st = [("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 3),
      ("RIGHTPADDING", (0, 0), (-1, -1), 3), ("TOPPADDING", (0, 0), (-1, -1), 4),
      ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]
for i in range(0, 11, 2):
    st += [("BACKGROUND", (i, 0), (i, 0), GREY_BG), ("BOX", (i, 0), (i, 0), 0.7, LINE)]
st += [("LEFTPADDING", (i, 0), (i, 0), 0) for i in range(1, 11, 2)]
st += [("RIGHTPADDING", (i, 0), (i, 0), 0) for i in range(1, 11, 2)]
ft.setStyle(TableStyle(st))
story.append(ft)
story.append(Spacer(1, 3))
story.append(P("<b>Self-learning:</b> every night the model re-trains on the day's data. Each reply "
               "(\"I'm OK\", \"only the cat\") becomes a lesson, and old examples are replayed so it does not "
               "forget. Starts from a public ESP32 dataset (UIT-ESP32) + our own recorded data. "
               "Everything runs at home: <b>no cloud, no camera</b>.", small))
story.append(Spacer(1, 6))

# Row 4: comparison table
story.append(P("How it is better than published work", h))
Y, N = "✓", "–"
hdr = ["", "WiFall\n2017", "DeFall\n2022", "XFall\n2024", "SiFall\n2022", "AR-Alarm\n2017", "UIT-ESP32\n2026",
       "Home Guardian\n(ours)"]
rows = [
    ["Detects falls", Y, Y, Y, Y, N, Y, Y],
    ["Detects intruders / theft", N, N, N, N, Y, N, Y],
    ["Keeps learning the home's routine", N, N, N, Y + "*", N, N, Y],
    ["Knows family vs stranger", N, N, N, N, N, N, Y],
    ["\"Are you OK?\" voice check", N, N, N, N, N, N, Y],
    ["Cheap ESP32 boards", N, N, N, N, N, Y, Y],
    ["Which floor and room (2+ floors)", N, N, N, N, N, "room", Y],
    ["Reported result", "94% precision,\n13% false alarms", ">95% caught,\n<1.5% false", "96.8%\naccuracy",
     "94.1% caught,\n1 false / 3 days", "intruders only;\nsee paper", ">99%\nprecision",
     "Target: >=95%,\n<1 false / week"],
]
data = [[Paragraph(f"<b>{x}</b>".replace("\n", "<br/>"), cell) for x in hdr]]
for r in rows:
    data.append([Paragraph(r[0], cellL)] + [Paragraph(x.replace("\n", "<br/>"), cell) for x in r[1:]])
first = 112
cws = [first] + [(CW - first - 70) / 6] * 6 + [70]
ct = Table(data, colWidths=cws)
cst = [("GRID", (0, 0), (-1, -1), 0.5, LINE), ("BACKGROUND", (0, 0), (-1, 0), NAVY),
       ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("TOPPADDING", (0, 0), (-1, -1), 1.6),
       ("BOTTOMPADDING", (0, 0), (-1, -1), 2), ("LEFTPADDING", (0, 0), (-1, -1), 3),
       ("RIGHTPADDING", (0, 0), (-1, -1), 3), ("BACKGROUND", (-1, 1), (-1, -1), TEAL_BG)]
for c in range(8):
    data[0][c].style = S("hc", 6.9, font="DVB", color=colors.white, alignment=TA_CENTER)
ct.setStyle(TableStyle(cst))
story.append(ct)
story.append(P("* SiFall self-learns for falls only.  – = not reported in that paper.  "
               "In our search of 11 papers, <b>no single system combines all seven rows</b>.", tiny))
story.append(Spacer(1, 6))

# Row 5: features + cost/target
story.append(two(
    [P("6 features that make it stand out", h),
     P("1. <b>Two modes, one system</b>: fall alert + theft alarm on the same boards.<br/>"
       "2. <b>Learns the home's routine</b> by itself, every night, without labels.<br/>"
       "3. <b>Family vs stranger</b> using phones + walking style: no false theft alarm when a son comes home early.<br/>"
       "4. <b>\"Are you OK?\" voice check</b>: fewer false alarms, and every answer teaches the model.<br/>"
       "5. <b>Cheap multi-floor setup</b> that tells floor and room.<br/>"
       "6. <b>Live dashboard</b>: house map, current mode, confidence meter and alerts on a phone.")],
    [P("Cost and honest goal", h),
     P("<b>Prototype for a 2-floor home: about Rs. 3,000-6,000</b><br/>"
       "&bull; 6 ESP32 boards (1 sender + 2 receivers per floor)<br/>"
       "&bull; A laptop as the hub now; a Raspberry Pi later<br/>"
       "&bull; Small speaker + mic (or an old phone)<br/>"
       "<b>Goal:</b> catch at least 95% of falls and intruders with less than 1 false alarm a week after "
       "learning. No system is 100%; the voice check covers the rest.<br/>"
       "<b>Tests:</b> acted falls on a mattress, 1-3 people, 2 floors, 2-4 weeks of live use, "
       "compared with WiFall-style and SiFall-style methods.")]))
story.append(Spacer(1, 5))
story.append(P("<b>Build plan:</b> 1. Live dashboard on simulated data &rarr; 2. Record Wi-Fi data with 3 ESP32 boards in one room "
               "&rarr; 3. Train the first model (falls + empty/motion) &rarr; 4. Add Theft mode, 2 floors and night learning "
               "&rarr; 5. Full tests and write the paper.", small))
story.append(Spacer(1, 5))

refs = ("<b>References:</b> WHO, \"Falls\" fact sheet. | Wang, Wu, Ni, \"WiFall\", IEEE TMC 16(2), 2017. | "
        "Hu et al., \"DeFall\", IEEE IoT-J 9, 2022. | Chi et al., \"XFall\", IEEE JSAC 42(9), 2024. | "
        "Ji, Xie, Li, \"SiFall\", ACM SenSys 2022. | Li et al., \"AR-Alarm\", ICOST 2017, LNCS 10461. | "
        "Do et al., \"Human Fall Detection and Indoor Localization Using WiFi Sensing\" (UIT-ESP32), LNNS 1581, 2026. | "
        "Yang et al., \"AutoFi\", IEEE IoT-J 10(8), 2023. Full list with links: literature/notes/wifi-fall-detection.md")
story.append(P(refs, tiny))

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=72, bottomMargin=22,
                        title="Home Guardian - one-page summary", author="Shravya Shetty")
doc.build(story, onFirstPage=header, onLaterPages=header)
print("wrote", OUT)
