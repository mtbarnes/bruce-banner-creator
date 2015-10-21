import os
os.chdir(os.path.dirname(__file__))
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
    def __init__(self, version):
        super(BruceApp, self).__init__()
        self.staticpath = os.path.join(os.path.dirname(__file__), 'static')
        self.version = version
        self.route('/', callback=self.landing_index)
        self.route('/working', callback=self.make_main_banner)
        self.route('/static/<filename:path>', callback=self.send_static)
        self.bruce = Bruce("test.jpg")

    def send_static(self, filename):
        return static_file(filename, self.staticpath)

    def make_main_banner(self):
        # f = cStringIO.StringIO()
        # bruce = Bruce()
        image = self.bruce.make_banner('static/in.jpg', 300, 5)
        orig_b = Image.open('static/banner.png')
        orig_p = Image.open('static/pal.png')
        orig_p.save('static/prev_pal.png', "PNG")
        orig_b.save('static/prev_banner.png', "PNG")
        image.save("static/banner.png", "PNG")
        palette = self.bruce.make_palette('static/banner.png', 5)
        palette[0].save('static/pal.png', "PNG")

        # image.save(f, "PNG")
        # f.seek(0)

        redirect('/')
        # imdata = f.getvalue().encode('base64')
        # return template(sendimage, imdata = imdata)

    def landing_index(self):
        return template('index', version=self.version)


appliction = BruceApp("0.0 Uber-Alpha")

# if __name__ == "__main__":
#     application.run()

