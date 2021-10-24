from PIL import Image
import matplotlib.pyplot as plt
import os

# input
runs = [{"day": 12, "run": 0}, {"day": 12, "run": 6},
        {"day": 12, "run": 12}, {"day": 12, "run": 18},
        {"day": 13, "run": 0}, {"day": 13, "run": 6},
        {"day": 13, "run": 12}, {"day": 13, "run": 18}]

# init
l, nxl, nnl, labels = [], [], [], []
l100, l150, l200 = [], [], []

colors = [{"color": (240, 240, 240), "value": 0},
          {"color": (222, 222, 242), "value": 0.5},
          {"color": (180, 215, 255), "value": 1.5},
          {"color": (117, 186, 255), "value": 2.5},
          {"color": (53, 154, 255), "value": 4},
          {"color": (4, 130, 255), "value": 6},
          {"color": (0, 105, 210), "value": 8.5},
          {"color": (0, 54, 127), "value": 12.5},
          {"color": (20, 143, 27), "value": 17.5},
          {"color": (26, 207, 5), "value": 22.5},
          {"color": (99, 237, 7), "value": 27.5},
          {"color": (255, 244, 43), "value": 35},
          {"color": (232, 220, 0), "value": 45},
          {"color": (240, 96, 0), "value": 55},
          {"color": (255, 127, 39), "value": 65},
          {"color": (255, 166, 106), "value": 75},
          {"color": (248, 78, 120), "value": 85},
          {"color": (247, 30, 84), "value": 95},
          {"color": (191, 0, 0), "value": 112.5},
          {"color": (136, 0, 0), "value": 137.5},
          {"color": (100, 0, 127), "value": 162.5},
          {"color": (194, 0, 251), "value": 187.5},
          {"color": (221, 102, 255), "value": 225}, ]

rowend = [586, 594, 594, 602, 594, 602, 618, 618, 618, 618, 610, 610,
          594, 594, 570, 562, 554, 554, 546, 546, 538, 538, 538, 538]

for run in runs:
    modell, modelnxl, modelnnl = [], [], []  # init
    model100, model150, model200 = [], [], []

    day = run["day"]
    runz = run["run"]
    pathTo = f"C:/Users/Maarten/Documents/Onderzoek/data/+48/{day}J/{runz}z"
    labels.append(f"{day}-{runz}z")

    # GFS, ECMWF (0,12), ARPEGE, SWISSHD, EC-SWISSHD, GEM (0,12), HARMONIE
    for filename in os.listdir(pathTo):
        im = Image.open(f"{pathTo}/{filename}").load()

        navg = []
        nx, nn, count100, count150, count200 = 0, 1000, 0, 0, 0
        points = 0
        y = 244

        for row in range(24):
            end = rowend[row]
            x = 434
            y += 8

            while x <= end:
                # check for invalid pixels
                pix = im[x, y]
                if pix != (0, 0, 0) or pix != (170, 170, 170) or pix != (255, 255, 255):
                    # compare pixel with list
                    for color in colors:
                        if pix == color["color"]:
                            n = color["value"]
                            navg.append(n)
                            nn = n if n < nn else nn
                            nx = n if n > nx else nx
                            count100 += 1 if n > 100 else 0
                            count150 += 1 if n > 150 else 0
                            count200 += 1 if n > 200 else 0
                            points += 1

                    x += 8

        modell.append(sum(navg) / len(navg))
        modelnxl.append(nx)
        modelnnl.append(nn)
        model100.append(count100/points)
        model150.append(count150/points)
        model200.append(count200/points)

    l.append(modell)
    nxl.append(modelnxl)
    nnl.append(modelnnl)
    l100.append(model100)
    l150.append(model150)
    l200.append(model200)

# style
medianprops = {"linestyle": '-', "linewidth": 2, "color": 'black'}
flierprops = {"marker": "o", "markerfacecolor": "black", "markersize": 4}

plt.title(f"average area precipitation over +48h")
plt.ylabel("precipitation (mm)")

# Choose var: l = avg, nxl = max, nnl = min, l100 = percentage points with > 100mm
plt.boxplot(l, labels=labels, medianprops=medianprops,
            flierprops=flierprops)
plt.show()
