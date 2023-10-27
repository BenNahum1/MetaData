import glob
from PIL import Image
from PIL.ExifTags import TAGS

def finedMetaData(filePath):
    for filename in glob.glob(filePath+"/*.jpg"):#Searches all jpg files in the folder.
        im=Image.open(filename)#open image
        print('file path: ',filename , "\n")

        exifdata = im.getexif()#opens image metadata
        for tagid in exifdata:#run on the meta data of im
            tagname = TAGS.get(tagid, tagid)
            value = exifdata.get(tagid)
            print(f"{tagname:60}: {value}")

        im.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filePath = input("enter file path")
    finedMetaData(filePath)

