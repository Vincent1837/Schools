from pymongo import MongoClient
from PIL import Image
import io
import matplotlib.pyplot as plt

client = MongoClient()
db = client.demo
images = db.images

im = Image.open("C:\\Users\\Liu\\Desktop\\2024 Python\\Mongo DB\\image.jpg")

image_bytes = io.BytesIO()
im.save(image_bytes, format='JPEG')

image = {
    'data': image_bytes.getvalue()
}

image_id = images.insert_one(image).inserted_id
print(image_id)

ST1= { "Name": "XXX", "age": 40, "photo": image_id}

db.STUDENT.insert_one(ST1) 

allimages = db.images.find()
for ig in allimages:
    pil_img = Image.open(io.BytesIO(ig['data']))
    plt.imshow(pil_img)
    plt.show()

