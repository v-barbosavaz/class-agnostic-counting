from PIL import Image
import numpy
import scipy.io
import math

"""
Generate dot annotated-files

This program run for the specific case of the UCF_CC_50 dataset.
Since there is no standards to create datasets with images and
locations of objects, you should adapt the code for your dataset. 
"""

# for each image
for i in range(1, 51):
    im = Image.open(str("../../UCF_CC_50/"+ str(i) +".jpg"))
    width, height = im.size
    print(i, width, height)

    #img = Image.new('RGB', (width, height), color = (0, 0, 0))
    #img.save(str("../../UCF_CC_50/dot_"+ str(i) +".jpg"))

    # we create a black image
    data = numpy.zeros((height, width, 3), dtype=numpy.uint8)

    # add a red pixel at (0,0)
    #data[0, 0] = [255, 0, 0]

    err_count = 0
    mat = scipy.io.loadmat(str("../../UCF_CC_50/"+ str(i) +"_ann.mat"))
    for point in mat['annPoints']:
        x, y = point

        # mat file can be corrupted...
        try:
            data[math.floor(y)-1, math.floor(x)-1] = [255, 0, 0]
        except:
            err_count += 1
    print(err_count)

    img = Image.fromarray(data)
    img.save(str("../../UCF_CC_50/dot_"+ str(i) +".png"))
    #img.show()
