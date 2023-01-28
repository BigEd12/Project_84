from tkinter import *
from tkinter import filedialog
from PIL import Image


#---------- UPLOAD FILES ----------#
def upload_original():
    global original
    file_dir = filedialog.askopenfilename()
    original = Image.open(file_dir)


def upload_watermark():
    global watermark
    file_dir = filedialog.askopenfilename()
    watermark = Image.open(file_dir)
    watermark.show()

#---------- APPLY WATERMARK ----------#
def apply_watermark():
    global original
    original.paste(watermark, (-80, -80), mask=watermark)
    original.show()

#---------- SAVE IMAGE ----------#
def save_image():
    global original
    file_dir = filedialog.asksaveasfilename(defaultextension=".png")
    original.save(file_dir)


#---------- UI SETUP ----------#
window = Tk()
window.title("Watermark")
window.config(padx=150, pady=150, bg="light yellow")

#---------- IMAGE CANVAS ----------#
canvas = Canvas(width=450, height=450, bg="light yellow")
bg = PhotoImage(file="bg.png")
canvas.create_image(225, 225, image=bg)
canvas.create_text(225, 225, text="Upload your image:", fill="black", font=("courier", 15, "bold"))
canvas.grid(column=1, row=1)

#---------- TITLE ----------#
title = Label(text="Add a watermark to your image", fg="black", bg="light yellow", font=("courier", 25, "bold"))
title.grid(column=1, row=0)

#---------- BUTTONS ----------#
button = Button(text="Upload original image", command=upload_original)
button.grid(column=1, row=2)

button = Button(text="Upload watermark", command=upload_watermark)
button.grid(column=1, row=3)

button = Button(text="View image", command=apply_watermark)
button.grid(column=1, row=4)

button = Button(text="Save image", command=save_image)
button.grid(column=1, row=5)



window.mainloop()