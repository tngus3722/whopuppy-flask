from flask import Flask
from tensorflow.keras.models import load_model
from urllib import request
from flask import request as fr
import time
from io import BytesIO
from PIL import Image
import os, glob, numpy as np


app = Flask("api_test")
model = load_model('./model') # 학습된 모델
@app.route('/')
def hello():
    categories = ["Beagle"
        , "bichon"
        , "BorderCollie"
        , "Bulldog"
        , "chihuaua"
        , "ChowChow"
        , "cocaspaniel"
        , "Dachshund"
        , "Dalmatian"
        , "Husky"
        , "jindogae"
        , "Maltese"
        , "Miniature Pinscher"
        , "Miniature Schnauzer"
        , "Pome"
        , "Poodle"
        , "Pug"
        , "Retriever"
        , "Saint Bernard"
        , "ShibaInu"
        , "ShihTzu"
        , "Vizsla"
        , "WelshiCorgi"
        , "Yorkshireterrier"]
    image_w = 160
    image_h = 160
    url = fr.args.get('url', "")
    print(url)
    res = request.urlopen(url).read()
    img = Image.open(BytesIO(res))
    img = img.convert("RGB")
    img = img.resize((image_w, image_h))
    data = np.asarray(img)
    array = []
    array.append(data)
    array = np.array(array)
    array = array.astype(float) / 255
    prediction = model.predict(array)
    answer = []
    length = len(prediction[0])

    for i in range(length):
        tmp = prediction[0][i]
        answer.append([tmp * 100, categories[i]])

    answer = sorted(answer, reverse=True, key=lambda x: x[0])

    result = []
    count = 0
    for i in answer:
        result.append(i)
        count += 1
        if (count == 5):
            break

    b = dict()
    for i in result:
        b[i[1]] = i[0]
    return b

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)