# Finish last lesson
закончим предидущюю проблему!
```python
with open('./static/model/imagenet_classes.json') as file:
  labelInfo = file.read()

import json

labelInfo = json.loads(labelInfo)

from keras.models import load_model

model = load_model('./static/model/MobileNet.h5')

from keras.preprocessing import image

img_height = img_width = 224

img_url = '.' + imageURL

img = image.load_img(img_url, target_size=(img_height, img_width))

x = image.img_to_array(img)
x - x/255
x = x.reshape(1,img_height, img_width, 3)

predi = model.predict(x)

import numpy as np
num = np.argmax(predi[0])

prediction = labelInfo[str(num)][1]
```
