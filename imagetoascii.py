# In order to get the program to work, you must install:
#    requests 
#    beatifulsoup4
#    lmxl
#    pillow

# This project works with web scraping and image libraries to convert any user input into ascii art. 
# The user input is taken, put into a google search query, and then the webpage is scraped to find the first image result. 
# This image is then converted into ascii. The image is resized and converted into grayscale.
# Next, each pixel in the picture is converted to a pixel in a character array. This array is then printed to display the ascii art. 

import requests
from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image
import PIL.Image

# character list corresponding with pixels from darkest to lightest
chars = ["@", "%", "#", "*", "+", ":", ".", " "]
brightscalar = 35
nwidth = 144

# scrape image url from web
def geturl(itm):
    url = 'https://www.google.com/search?q={0}&tbm=isch'.format(itm)
    htmlcode = BeautifulSoup(requests.get(url).content,'lxml')
    images = htmlcode.findAll('img')
    imgurl = images[1].get('src')
    return imgurl

# change image size so output ascii art fits in terminal
def resize(image):
    width, height = image.size
    ratio = height / width / 1.65 #ascii character has a 1:1.65 ratio
    nheight = int(nwidth*ratio)
    resizeval = (nwidth, nheight)
    newsize = (resizeval)
    nimage = image.resize(newsize)
    return nimage

# change image to grayscale so pixel brightness can be converted into an ascii character
def grayscale(image):
    gsimage = image.convert("L")
    return(gsimage)

# get image from input 
itm = input("Enter item: ")
itm = itm + " white background "
itmurl = geturl(itm)
urllib.request.urlretrieve(itmurl, "blah.png")
img = Image.open("blah.png")

#prepare image for ascii conversion
nimg = grayscale(resize(img))

#get pixels of image
pixels = nimg.getdata()

#convert pixel of image to ascii character 
npixels = [chars[pixel//brightscalar] for pixel in pixels]
npixels = ''.join(npixels)

#format and print asciiart
npixelslen = len(npixels)
asciiart = [npixels[i:i + nwidth] for i in range(0, npixelslen, nwidth)]
asciiart = "\n".join(asciiart)
print(asciiart)