# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import json


Width = 1080
Height = 1080


def GenerateImage(_name: str, _meaning: str):
    Name = _name
    Meaning = _meaning

    # new = Image.new("RGB", (Width, Height), (255, 255, 255))
    bg = Image.open("./assets/bg.png")

    draw = ImageDraw.Draw(bg)

    font1 = ImageFont.truetype("Alkalami-Regular.ttf", size=128)
    font2 = ImageFont.truetype("times.ttf", size=56)
    # font = ImageFont.truetype("arial.ttf", FontSize)

    _pos = (Width / 12, Height / 3.0)
    draw.text(xy=_pos, text=Name, fill=(0, 0, 0), align="left", spacing=16, font=font1)

    _pos = (Width / 11, Height / 1.85)
    draw.multiline_text(xy=_pos, text=Meaning, fill=(0, 0, 0), align="left", spacing=16, font=font2)

    bg.save("./export/" + Name + ".png")


def main():
    with open("./assets/data.json", "r", encoding="utf-8") as f:
    # with open("data-news.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for entry in data:
        GenerateImage(entry["name"], entry["meaning"])


if __name__ == "__main__":
    main()
    # GenerateImage("Berat", "Strong")
