from PIL import Image
import numpy as np
import os


folder = 'HDR 02'

images = []

for i in os.listdir(folder):
    im = Image.open(folder + "/" + i)
    im_rgb = np.asarray(im.convert("RGB"))
    images.append(im_rgb)



sum = np.zeros(images[0].shape)
for image in images:
    sum = np.add(sum,image)

sum = np.asarray(sum / len(images), dtype=np.uint8)

result_image = Image.fromarray(sum)

result_image.save("result.png","PNG")

result_image.show()

