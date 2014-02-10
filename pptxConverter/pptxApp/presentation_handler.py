import os
from PIL import Image

from time import time
from pptxConverter.settings import PRESENTATION_PATH
from pptxConverter.settings import PRESENTATION_STATIC_PATH
from pptxConverter.settings import CMD_COMMANDS


class PresentationHandler(object):
    def __init__(self, post_data, files):
        self.presentation_temp = files['presentation']
        self.title = u'{0}_{1}'.format(post_data['title'], unicode(time()))
        self.path = self.convert_to_images()

    def convert_to_images(self):
        result = {'presentation': '',
                  'images': [],
                  'thumbnail': []}
        os.makedirs('{0}{1}'.format(PRESENTATION_PATH, self.title))
        with open('{0}{1}/{1}.pptx'.format(PRESENTATION_PATH, self.title), 'w+') as pres:
            pres.write(self.presentation_temp.read())
        for i in CMD_COMMANDS:
            os.system(i.replace('{presentation_name}',
                           '{0}{1}/{1}'.format(PRESENTATION_PATH, self.title))\
                .replace('{image_name}',
                         '{0}{1}/{1}_%03d.jpg'.format(PRESENTATION_PATH, self.title)))
        os.remove('{0}{1}/{1}.pdf'.format(PRESENTATION_PATH, self.title))
        del self.presentation_temp
        for i in os.listdir('{0}{1}'.format(PRESENTATION_PATH, self.title)):
            if 'ppt' not in i.split('.')[-1]:
                image = Image.open('{0}{1}/{2}'.format(PRESENTATION_PATH, self.title, i))
                image.thumbnail((300, 300), Image.ANTIALIAS)
                image.save('{0}{1}/{2}'.format(PRESENTATION_PATH, self.title, '.'.join(i.split('.')[:-1]) + '_min.jpg'),
                           'JPEG')
                result['images'].append('{0}{1}/{2}'.format(PRESENTATION_STATIC_PATH,
                                                            self.title,
                                                            i))
                result['thumbnail'].append('{0}{1}/{2}'.format(PRESENTATION_STATIC_PATH,
                                                            self.title,
                                                            '.'.join(i.split('.')[:-1]) + '_min.jpg'))
            else:
                result['presentation'] = '{0}{1}/{2}'.format(PRESENTATION_STATIC_PATH,
                                                             self.title,
                                                             i)
        files = ['/static/media/{0}/{1}'.format(self.title, f)
                 for f in os.listdir('{0}{1}'.format(PRESENTATION_PATH, self.title))]
        return result
