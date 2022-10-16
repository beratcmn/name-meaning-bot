from PIL import Image, ImageDraw, ImageFont
import json


Width = 1080
Height = 1080


Name = "Berat"
Meaning = "Strong"

# new = Image.new("RGB", (Width, Height), (255, 255, 255))
bg = Image.open("./assets/bg.png")

draw = ImageDraw.Draw(bg)

font1 = ImageFont.truetype("Alkalami-Regular.ttf", size=128)
font2 = ImageFont.truetype("times.ttf", size=64)
# font = ImageFont.truetype("arial.ttf", FontSize)

_pos = (Width / 12, Height / 3.0)
draw.text(xy=_pos, text=Name, fill=(0, 0, 0), align="left", spacing=100, font=font1)

_pos = (Width / 11, Height / 1.75)
draw.text(xy=_pos, text=Meaning, fill=(0, 0, 0), align="left", spacing=100, font=font2)


bg.save("./export/" + Name + ".png")
