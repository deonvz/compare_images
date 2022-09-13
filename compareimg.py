# compare images
# Created by: Deon van Zyl
# https://github.com/deonvz/compare_images
# MIT License
# Note: Place your images in the same directory as this script

from PIL import Image ,ImageChops, ImageEnhance

# Select the images to compare. Place these images in the same folder as this script.
img1=Image.open(r'1.jpg')
img2=Image.open(r'2.jpg')
gray_image = Image.open(r'1.jpg')

# Grey scale of the image missing parts 
gray_image =img2.convert("L") #return 8Bit
# Now lets darken this image so we can see the differences as overlay in color
enhancer = ImageEnhance.Brightness(gray_image)
# to reduce brightness by 50%, use factor 0.5
gray_image = enhancer.enhance(0.5) 
#gray_image.show() # Uncomment to see the darkness

# --- Get the Sizes of the images
print('The two images that are being compared should be the same dimensions,size and not at different angles')
print('img1 size:', img1.size)
print('img2 size:', img2.size)

# ==== Start Differences =====
# --- Make a new image based on the differences & open a windows to show it
diff=ImageChops.difference(img1,img2)

#Make the background transparent for the Differences image

def convertImage():
    imgdiff = diff.convert("RGBA")
 
    datas = imgdiff.getdata()
 
    newData = []
 
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((0, 0, 0, 0))
        else:
            newData.append(item)
 
    imgdiff.putdata(newData)
    imgdiff.paste(img1, (0,0),imgdiff) # Place the differences over the original image
    #imgdiff.paste(gray_image, (0,0), imgdiff)# Place it over grayscale
    imgdiff.save("./New.png", "PNG", quality=100)
	
    print("Successful")
 
convertImage()

#if diff.getbbox():
	#diff.show()

# Print the size for the difference image
print('Differences image size',diff.size)

# ==== End Differences =====

# Make a new image that has the differences shown on a grayscale image
imagdiffwithbackgroundchange=Image.open(r'New.png')
#imagdiffwithbackgroundchange.show()
imagdiffwithbackgroundchange2 =Image.open(r'New.png')
imagdiffwithbackgroundchange2.paste(gray_image, (0,0), gray_image)
#imagdiffwithbackgroundchange2.show()



# Make a new image with a merge of the images above
new_im = Image.new('RGB', (2*img1.size[0],2*img1.size[1]), (250,250,250))

new_im.paste(img1, (0,0))
new_im.paste(img2, (img1.size[0],0))
new_im.paste(imagdiffwithbackgroundchange, (0,img1.size[1]))
new_im.paste(imagdiffwithbackgroundchange2, (img1.size[0],img1.size[1]))
 
new_im.save("merged_images.png", "PNG")
new_im.show()

