from PIL import Image

print("\033[1;31;40m Red \033[0;0m")
print("\033[1;31;40m Hallo \033[0;0m")
# Open the Image and change the high and the width
# Uncommit this line in the end
#image = Image.open(input("Please input the location of the file to be converted: "))

while True:
    try:
        image = Image.open("/Users/langma/Documents/test.png")
        break
    except:
        print("Failed! Please enter a valid file-path!")

n, m = input("Please enter the width/hight for the resulting Image: ").split()
image = image.resize((int(m), int(n)))
image.save("/Users/langma/Documents/working.png")

# Declare the Arrays
characters = ["$", "@", "B", "%", "8", "&", "W", "M", "#", "*", "o", "a", "h", "k", "b", "d", "p", "q", "w", "m", "Z", "O", "0", "Q", "L", "C", "J", "U", "Y", "X", "z", "c", "v", "u", "n", "x", "r", "j", "f", "t", "/", "\\", "|", "(", ")", "1", "{", "}", "[", "]", "?", "-", "_", "+", "~", "<", ">", "i", "!", "l", "I", ";", ":", ",", "\"", "^", "`", "'", " "]

# Main
image = Image.open("/Users/langma/Documents/working.png").convert("L")
pix = image.getdata()
results = ""

for p in pix:
    x = int(p)//3.75
    results += characters[int(x)]
    if len(results) % (int(m)) == 0:
        print(results)
        results = ""
print(results)