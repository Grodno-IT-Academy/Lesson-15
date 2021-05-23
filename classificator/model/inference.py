import json
from keras.models import load_model
from keras.preprocessing import image
import numpy as np


def runInference(imageURL):
    #open labels json
    with open('./static/model/imagenet_classes.json') as f:
        label_info = f.read()
    #make dictionary out of json string
    label_info = json.loads(label_info)
    #assign model
    model = load_model('./static/model/MobileNet.h5')
    #load image
    img_height = img_width = 224
    img_url = '.' + imageURL
    img = image.load_img(img_url, target_size=(img_height, img_width))
    #work with image array
    x = image.img_to_array(img)
    x = x/255
    x = x.reshape(1, img_height, img_width, 3)
    predi = model.predict(x)
    num = str(np.argmax(predi[0]))
    prediction = label_info[num][1]
    return prediction
