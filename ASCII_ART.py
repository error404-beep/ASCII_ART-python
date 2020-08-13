from PIL import Image

def roll_img(original_img):
    return original_img.transpose(Image.ROTATE_90)

try:
  IMAGE_PATH = input("Please specify IMAGE PATH")
  img = Image.open(IMAGE_PATH)
  print('Image was loaded')
  print('Size of Image: ', img.size)
  print('Format of the Image: ',img.format)
  print('Mode of the Image: ', img.mode)
except:
  print('Image couldnt be loaded')
  exit()
while(True):
  ans = input('Do you want to rotate the image?[Y/N]')
  if(ans == 'Y'):
      im = roll_img(img)
      break
  elif(ans == 'N'):
      im = img
      break
  else:
      print('Please type Y or N')

width = im.size[0]
height = im.size[1]
#Create a 2-d Matrix to store all the RGB Values for each pixel

data = []
#Get all the RGB values for each pixel.
for i in range(width):
  col = []
  for j in range(height):
    col.append(im.getpixel((i, j)))
  data.append(col)

# print(len(data))

#Transfor each tuple to a Brightness Value. This time we will use Averae Method, i.e bright = (R + B +G) / 3

# print("Printing the Brightness of each pixel ...")

for i in range(width):
  for j in range(height):
    r = data[i][j][0]
    b = data[i][j][1]
    g = data[i][j][2]
    data[i][j] = round((r + b + g) / 3)
    # print(data[i][j])

#Converting/Mapping brightness values to ascii chars provided. 

ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
# print(len(ascii_chars))
'''There are 65 unique chars avaialbe and total 0-255 values to map with. To make this possible we get 256/65 = 3.9.. for each ASCII char. To map them we divide the value of brightness by 4 and then replace it with the charecter in the position in ascii_chars'''

for i in range(width):
  for j in range(height):
    num = data[i][j] // 4
    data[i][j] = ascii_chars[num]
    # print(data[i][j])

#Now to print our ASCII art
for i in range(width):
  for j in range(height):
    print(data[i][j], end='')
  print()