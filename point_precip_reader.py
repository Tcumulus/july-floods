from PIL import Image
import matplotlib.pyplot as plt
import os

# input
runs = [{"day": 12, "run": 12}, {"day": 12, "run": 18},
        {"day": 13, "run": 0}, {"day": 13, "run": 6}]

x, y = 578, 287
l, labels = [], []

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

for run in runs:
    navg = []  # init

    day = run["day"]
    runz = run["run"]
    pathTo = f"C:/Users/Maarten/Documents/Onderzoek/data/+48/{day}J/{runz}z"
    labels.append(f"{day}.07 {runz}UTC")

    # GFS, ECMWF (0,12), ARPEGE, SWISSHD, EC-SWISSHD, GEM (0,12), HARMONIE
    for filename in os.listdir(pathTo):
        im = Image.open(f"{pathTo}/{filename}").load()

        # check for invalid pixels
        while im[x, y] == (0, 0, 0) or im[x, y] == (170, 170, 170) or im[x, y] == (255, 255, 255):
            x += 1
            y += 1

        pix = im[x, y]
        # compare pixel with list
        for color in colors:
            if pix == color["color"]:
                navg.append(color["value"])  # avg

    l.append(navg)

# style
# meanlineprops = {"linestyle": '--', "linewidth": 2, "color": '#128ba3'}
medianprops = {"linestyle": '-', "linewidth": 2, "color": 'black'}
flierprops = {"marker": "o", "markerfacecolor": "black", "markersize": 4}

plt.title(f"+48h precipitation prevision for {x}, {y}")
plt.ylabel("precipitation (mm)")
plt.boxplot(
    l, labels=labels, medianprops=medianprops, flierprops=flierprops)
# showmeans=True, meanprops=meanlineprops, meanline=True)
plt.show()
