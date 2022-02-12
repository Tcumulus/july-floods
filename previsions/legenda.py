from PIL import Image

im = Image.open('C:/Users/Maarten/Documents/Onderzoek/data/calib.png')
pix = im.load()
print(pix[20, 680])  # <0.1
print(pix[40, 680])  # 0.1-1
print(pix[68, 680])  # 1-2
print(pix[96, 680])  # 2-3
print(pix[124, 680])  # 3-5
print(pix[152, 680])  # 5-7
print(pix[180, 680])  # 7-10
print(pix[208, 680])  # 10-15
print(pix[236, 680])  # 15-20
print(pix[264, 680])  # 20-25
print(pix[292, 680])  # 25-30
print(pix[320, 680])  # 30-40
print(pix[348, 680])  # 40-50
print(pix[376, 680])  # 50-60
print(pix[404, 680])  # 60-70
print(pix[432, 680])  # 70-80
print(pix[460, 680])  # 80-90
print(pix[488, 680])  # 90-100
print(pix[516, 680])  # 100-125
print(pix[544, 680])  # 125-150
print(pix[572, 680])  # 150-175
print(pix[600, 680])  # 175-200
print(pix[628, 680])  # 200-250


print(pix[485, 418])  # LINE
print(pix[694, 460])  # NUMBWHITE
print(pix[696, 460])  # NUMBBLACK
