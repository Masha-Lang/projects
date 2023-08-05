### Beschreibung

Convert an png Image to Ascii Art.

### Solution

1. n, m = input {wie viel Pixel soll das Bild haben}
2.  resize image to n, m pixels
3. array with all special characters to be used (sorted)
4. empty string for the results
5. open image in black/white mode
6. for every pixel in image {
	1. x = how bright is it
	2. find suitable character from array and set it in the "result array"
7. }
8. convert the "result array" into an image

### Code

```python
from PIL import Image
# Open the Image and change the high and the width 

#image = Image.open(input("Please input the location of the file to be converted: "))
while True:
	try: 
		image = Image.open("/Users/langma/Documents/test.png")
		break
	except:
		print("Failed! Please enter a valid file-path!")

n, m = input("Please enter the width/hight for the resulting Image: ").split()
image = image.resize((int(m), int(n))) image.save("/Users/langma/Documents/working.png")
# Declare the Arrays
characters = ["$", "@", "B", "%", "8", "&", "W", "M", "#", "*", "o", "a", "h", "k", "b", "d", "p", "q", "w", "m", "Z", "O", "0", "Q", "L", "C", "J", "U", "Y", "X", "z", "c", "v", "u", "n", "x", "r", "j", "f", "t", "/", "\\", "|", "(", ")", "1", "{", "}", "[", "]", "?", "-", "_", "+", "~", "<", ">", "i", "!", "l", "I", ";", ":", ",", "\"", "^", "`", "'", " "]
# Main
image = Image.open("/Users/langma/Documents/working.png").convert("L") pix = image.getdata()
results = ""

for p in pix:
	x = int(p)//3.75
	results += characters[int(x)]
	if len(results) % (int(m)) == 0:
		print(results)
		results = ""

print(results)
```
