from __future__ import print_function
from PIL import Image
from random import randint
import sys
import os
from utils import KMeans


class PageMaster():
    def make_index(template, args):
        return "not implimented yet"

class Bruce():
    def __init__(self, filenames = []):
        ''' Bruce object init method. Sets the list of input filenames'''
        if isinstance(filenames, basestring):
            self.filenames = [filenames]
        else:
            self.filenames = filenames
    
    def make_palette(self, infile, num_colors):
        '''The make_palette function takes an input file and a number of
        colors, and returns a list of (image, color) tuples where
        color is a string of six hexadecimal digits prefixed with '#'

        '''
        
        src_im = Image.open(infile)
        # The following line of code needs to be changed!
        # Resizing to a square (regardless of input dimensions)
        # totally fucks with color densities.
        # TBH this never should have happened...
        src_im = src_im.resize((100, 100), Image.ANTIALIAS) 

        data_points = []        # There's a better way to do this
        for (count, color) in src_im.getcolors(257*257):
            for n in range(count):
                data_points.append(color)

        # Here we instantiate a bruce object with our data
        # and call the run() method to calculate centroids
        colormeans = KMeans(data_points, num_colors)
        result = [vec for vec in colormeans.run()]

        pal = Image.new('RGB', (100*num_colors, 100))
        for n, color in enumerate(result):
            sqr = Image.new('RGB', (100, 100), tuple(color))
            pal.paste(sqr, (100*n, 0, 100*n+100, 100))
        color_strings = []
        for mean in result:
            color_strings.append(str(mean))
        return (pal, color_strings)


    def make_banner(self, filename, square_base, factor):
        src_im = Image.open(filename)
        banner_im = Image.new("RGB", (factor*square_base, square_base))
        for i in range(0, factor):
            crop_center = (randint(0, src_im.size[0]-square_base),
                           randint(0, src_im.size[1]-square_base))
            crop_area = (crop_center[0], crop_center[1],
                         crop_center[0]+square_base, crop_center[1]+square_base)
            region = src_im.crop(crop_area)
            src_im.paste(region, crop_area)
            banner_im.paste(region, (square_base*i,  0,
                                    square_base+square_base*i, square_base))
        return banner_im



if __name__ == "__main__":
    square_base = int(sys.argv[1])
    factor = int(sys.argv[2])
    filenames = sys.argv[3:]
    for infile in filenames:
        filename, file_ext = os.path.splitext(infile)
        im1 = make_banner(infile, square_base, factor)
        im1.save(filename + '_banner' + '.jpg',
                 format="JPEG", subsampling=0, quality=100 )
    # im2 = composite_image(filenames, square_base, factor)
    # im2.save(filename + '_banner_composite' + '.jpg',
    #          format="JPEG", subsampling=0, quality=100 )
