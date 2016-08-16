from PIL import Image
im = Image.open("earthpixel.jpg")
#im.rotate(45).show()

dark_blue = (0, 51, 76)
red = (217, 26, 33)
light_blue = (112, 150, 158)
yellow = (252, 227, 166)


pixels = im.getdata()
pixel_list = list(im.getdata())

#print(pixel_list)

new_pixels = []

for pixel in pixels:
	total = pixel[0] + pixel[1] + pixel[2]

	if total <182:
		new_pixels.append(dark_blue)
	elif total >= 182 and total <= 364:
		new_pixels.append(red)
	elif total >= 364 and total <= 546:
		new_pixels.append(light_blue)
	else:
		new_pixels.append(yellow)

new_image = Image.new(im.mode, im.size)
new_image.putdata(new_pixels)
new_image.show()
new_image.save("outputttt.jpg", "jpeg") 



