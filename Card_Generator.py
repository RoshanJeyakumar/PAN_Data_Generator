import pandas as pd
from PIL import Image, ImageDraw, ImageFont
df = pd.read_csv("PAN_data.csv")
records = df.to_dict(orient='records')
font = ImageFont.truetype("OpenSans-Semibold.ttf", size=17)


def generate_card(data):
    template = Image.open("Pan_final.jpg")
    draw = ImageDraw.Draw(template)
    draw.text((26,283), str(data['Name']), font=font, fill='black')
    draw.text((29,374), data['Date of Birth'], font=font, fill='black')
    return template


i = 0
for record in records:
    i+=1
    card = generate_card(record)
    card.save("Record" + str(i) + ".jpg")

