###################### IMPORT #################################

from PIL import Image

###################### MAIN ###################################

while True:
    try:
        image = Image.open(input("Please input the location of the file to be converted: "))
        break
    except:
        print("Failed! Please enter a valid file-path!")
width, height = image.size
n = input("Please enter the height for the resulting Image: ")
x = width//(height/int(n))
image = image.resize((int(n), int(x)))
image.save("/Users/langma/Documents/working.png")