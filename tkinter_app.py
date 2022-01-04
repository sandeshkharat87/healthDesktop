# from tkinter import *
# from PIL import Image, ImageTk
# import tkinter as tk
# import numpy as np
# from tkinter import filedialog
# from tensorflow.keras.preprocessing.image import array_to_img, img_to_array



def prepro(IMG_FILE):
  IMG_FILE = Image.open(IMG_FILE)
  img = IMG_FILE.resize((224,224))
  img = np.array(img)
  img = img/255.0
  img = np.expand_dims(img, 0)
  result = model.predict(img)
  result = np.argmax(result)

  if result == 1:
    return "Yes"
  else:  
    return ""







# def browseFiles():
#     # filename = filedialog.askopenfilename(initialdir = "/",
#     #                                       title = "Select a File",
#     #                                       filetypes = (("Text files",
#     #                                                     "*.jpeg*"),
#     #                                                    ("all files",
#     #                                                     "*.*")))
#     path = filedialog.askopenfilename(initialdir='~/Downloads/', title='Select Photo', filetypes=(('JPEG files', '*.jpg'), ('PNG files', '*.png'),('JPEG files', '*.jpeg')   ))  

#     prepro(path)

#     TK_IMG = ImageTk.PhotoImage(file=path)
#     b2 =tk.Button(window,image=TK_IMG) # using Button 
#     b2.grid(row=3,column=1)  
                                                                                                  
# # Create the root window
# window = Tk()
  
# # Set window title
# window.title('File Explorer')
  
# # Set window size
# window.geometry("500x500")
  
# #Set window background color
# window.config(background = "white")
  
# # Create a File Explorer label
# label_file_explorer = Label(window,
#                             text = "File Explorer using Tkinter",
#                             width = 100, height = 4,
#                             fg = "white")
  
      
# button_explore = Button(window,
#                         text = "Browse Files",
#                         command = browseFiles)
  
# button_exit = Button(window,
#                      text = "Exit",
#                      command = exit)
  
# # Grid method is chosen for placing
# # the widgets at respective positions
# # in a table like structure by
# # specifying rows and columns
# label_file_explorer.grid(column = 1, row = 1)
  
# button_explore.grid(column = 1, row = 2)
  
# button_exit.grid(column = 1,row = 3)
  
# # Let the window wait for any events
# window.mainloop()


import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import numpy as np
my_w = tk.Tk()
my_w.geometry("400x300")  # Size of the window 
my_font1=('times', 18, 'bold')
l1 = tk.Label(my_w,text='Upload Image Here',width=30,font=my_font1)  
l1.grid(row=1,column=1)
b1 = tk.Button(my_w, text='Upload File', 
   width=20,command = lambda:upload_file())
b1.grid(row=2,column=1) 

def upload_file():
    # global filename
    global img
    f_types = [('jpg Files', '*.jpg'),('jpeg Files', '*.jpeg'),('PNG Files', '*.png')  ]
    filename = filedialog.askopenfilename(initialdir = "~/Downloads/" , filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)
    b2 =tk.Button(my_w,image=img) # using Button 
    b2.grid(row=3,column=1)

    cv_img = Image.open(filename)

    print(prepro(filename))





my_w.mainloop()  # Keep the window open


