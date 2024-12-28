# import pytesseract as pyro
# from PIL import Image
# # import cv2
# #pyro.pytesseract.tesseract_cmd=r'C:\Users\v.vimal\AppData\Local\Programs\Tesseract-OCR\pytesseract.exe'
# #pyro.pytesseract.tesseract_cmd = r"C:\\Users\\v.vimal\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\pytesseract.exe"
# image = Image.open(r'E:\Camcode-master\Camcode-master\upload\preprocessed_image.png')

# # Use pytesseract to extract text from the image
# extracted_text = pyro.image_to_string(image)

# # Print the extracted text
# print(extracted_text)



# import subprocess

# try:
#     result = subprocess.run(["tesseract", "--version"], stdout=subprocess.PIPE)
#     print("Tesseract executable found")
# except FileNotFoundError:
#     print("Tesseract executable not found")

import os.path

file_path = "./a.out"  # Change this to the actual path of your file
if os.path.isfile(file_path):
    print("a.out exists in the current directory.")
else:
    print("a.out does not exist in the current directory.")




