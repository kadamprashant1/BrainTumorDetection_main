
import cv2
import os
from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split
# from keras.utils import normalize


image_directory ='datasets/'

no_tumor_images= os.listdir('E:\MRI\datasets\no\no0.jpg')
yes_tumor_images=os.listdir(image_directory+ 'yes/')
dataset=[]
lable=[]

# dataset=[]
# label=[]

print(no_tumor_images)



for i , image_name in enumerate(no_tumor_images):
    if(image_name.split('.')[1]=='jpg'):
        image = cv2.imread(image_directory+'/no' + image_name)
        image= Image.fromarray(image,'RGB')
        image.resize((64,64))
        dataset.append(np.array(image))
        label.append(0)

for i , image_name in enumerate(no_tumor_images):
    if(image_name.split('.')[1]=='jpg'):
        image = cv2.imread(image_directory+'/no' + image_name)
        image= Image.fromarray(image,'RGB')
        image.resize((64,64))
        dataset.append(np.array(image))
        label.append(1)        

print(dataset)
print(lable)   

# x_train, x_text, y_train, y_test= train_test_split(dataset, lable, test_size=0.2, random_state=0)

# print(x_train.shape)