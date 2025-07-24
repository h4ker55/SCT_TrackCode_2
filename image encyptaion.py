from tkinter import *
from tkinter import filedialog, messagebox

root = Tk()
root.geometry("250x200")
root.title("Image Encrypt/Decrypt")

KEY = 123  # Simple XOR key

def xor_image(file_path, key):
    with open(file_path, 'rb') as f:
        data = bytearray(f.read())
    for i in range(len(data)):
        data[i] ^= key
    with open(file_path, 'wb') as f:
        f.write(data)

def encrypt_image():
    file_path = filedialog.askopenfilename(title="Select Image")
    if file_path:
        xor_image(file_path, KEY)
        messagebox.showinfo("Success", "Image encrypted!")

def decrypt_image():
    file_path = filedialog.askopenfilename(title="Select Image")
    if file_path:
        xor_image(file_path, KEY)
        messagebox.showinfo("Success", "Image decrypted!")

b1 = Button(root, text="Encrypt Image", command=encrypt_image)
b1.place(x=60, y=40)

b2 = Button(root, text="Decrypt Image", command=decrypt_image)
b2.place(x=60, y=90)

root.mainloop()