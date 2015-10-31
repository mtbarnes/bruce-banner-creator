import os
import sys
from bottle import Bottle
from bottle import run
from bottle import template
from bottle import static_file
from bottle import redirect
from bruce import Bruce
from PIL import Image

import cStringIO


class BruceApp(Bottle):
    def __init__(self):
        super(BruceApp, self).__init__()
        self.path = os.path.dirname(__file__)
        self.route('/', callback=self.landing_index)
        self.route('/demo/<number>', callback=self.make_banner_and_pal)
        self.route('/derp', callback=self.derp)
        # self.route('/static/<filename:path>', callback=self.send_static)
        self.bruce = Bruce("test.jpg")

    # def send_static(self, filename):
    #     return static_file(filename, self.staticpath)

    def derp(self):
        return "four oh four"


    def make_banner_and_pal(self, number):
        path = self.path #os.path.join(self.path, 'static')
        # f = cStringIO.StringIO()
        # bruce = Bruce()
        image = self.bruce.make_banner(path+'/static/in'+number+'.jpg', 300, 5)
        orig_b = Image.open(path+'/static/banner.jpg')
        orig_p = Image.open(path+'/static/pal.jpg')
        orig_p.save(path+'/static/prev_pal.jpg', "JPEG")
        orig_b.save(path+'/static/prev_banner.jpg', "JPEG")
        image.save(path+"/static/banner.jpg", "JPEG")
        palette = self.bruce.make_palette(path+'/static/banner.jpg', 5)
        palette[0].save(path+'/static/pal.jpg', "JPEG")

        # image.save(f, "PNG")
        # f.seek(0)

        redirect('/')
        # imdata = f.getvalue().encode('base64')
        # return template(sendimage, imdata = imdata)

    def landing_index(self):
        indexfile = os.path.join(os.path.dirname(__file__), "index.tpl")
        return template(indexfile, version='0.1')


if __name__ == "__main__":
    #os.chdir(os.path.dirname(__file__))
    application = BruceApp()
    application.run(host='0.0.0.0')

