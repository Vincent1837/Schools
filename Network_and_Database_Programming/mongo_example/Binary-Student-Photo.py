from pymongo import MongoClient
from PIL import Image
import io
import pprint
import matplotlib.pyplot as plt

client = MongoClient()
db = client.demo

im = Image.open("C:\\Users\\Liu\\Desktop\\2024 Python\\Mongo DB\\image.jpg")

image_bytes = io.BytesIO()
im.save(image_bytes, format='JPEG')

image = {
    'data': image_bytes.getvalue()
}

image_id = db.images.insert_one(image).inserted_id

ST1= { "Name": "XXX", "age": 40, "photo": image_id}

db.STUDENT.insert_one(ST1) 

for ST in db.STUDENT.find():
    print(ST["Name"], ST["age"]) #以欄位名稱(“Name”, “age”)作為Dictionary標籤取出該學生姓名與年齡
    print(ST["photo"])#以欄位名稱(“photo”)作為Dictionary標籤取出該學生的照片images document
    ig=db.images.find_one({"_id":ST["photo"]}) #以STUDENT的photo 欄位值作為Images檔案的查詢條件 (_id=ST["photo"])
    pil_img = Image.open(io.BytesIO(ig["data"])) #取出該document的data值(就是影像本身)
    plt.imshow(pil_img) #Show出物件 
    plt.show() #Show出物件