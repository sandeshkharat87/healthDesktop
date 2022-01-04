from vit_keras import vit, utils
import matplotlib.pyplot as plt
from vit_keras import vit, utils, visualize
import tensorflow as tf
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import numpy as np
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, array_to_img


my_w = tk.Tk()
my_w.geometry("1200x600")  # Size of the window 
my_font1=('times', 18, 'bold')
l1 = tk.Label(my_w,text='Upload Image Here',width=30,font=my_font1)  
l1.grid(row=1,column=1)
b1 = tk.Button(my_w, text='Upload File', 
   width=20,command = lambda:upload_file())
b1.grid(row=2,column=1) 



model = model = tf.keras.models.load_model('newBT_V6.h5')


def prepro(IMG_FILE):
  IMG_FILE = Image.open(IMG_FILE)
  img = IMG_FILE.resize((224,224))
  img = np.array(img)
  img = img/255.0
  img = np.expand_dims(img, 0)
  # result = model.predict(img)
  # result = np.argmax(result)
  result = 1
  if result == 1:
    return "Yes"
  else:  
    return ""

def upload_file():
    # global filename
    global img
    f_types = [('jpg Files', '*.jpg'),('jpeg Files', '*.jpeg'),('PNG Files', '*.png')  ]
    filename = filedialog.askopenfilename(initialdir = "~/Downloads/" , filetypes=f_types)
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img.resize((300,300)))
    
    if prepro() !=1:
        b2 =tk.Button(my_w,image=img) # using Button 
        b2.grid(row=5,column=1)
    else:    
        # vit_img = visualize.attention_map(model, img)
        # keras_img = array_to_img(vit_img)
        # keras_img = load_img(keras_img, target_size=(300,300))
        b2 =tk.Button(my_w,image=img) # using Button 
        b2.grid(row=5,column=1)
        b3 =tk.Button(my_w,image=keras_img) # using Button 
        b3.grid(row=5,column=2)
    
my_w.mainloop()  # Keep the window open







