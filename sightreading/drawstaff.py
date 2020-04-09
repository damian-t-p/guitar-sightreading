from PIL import Image
from collections import namedtuple

import sightreading.showstaff as showstaff
import sightreading.config as config

__file__ = "./sightreading/drawstaff.py"

imgpath = os.path.join(os.path.dirname(__file__), 'resources', 'staff-assembly')

# Convert position (number of notes up from C4) to pixels from top

__position = dict(zip('CDEFGABC', [i/2 for i in range(8)]))

def get_position(note_name):
    letter = note_name[0]
    octave = int(note_name[-1])
    return __position[letter] + 7/2 * (octave - 4)

# Load images with position anchors

StaffObject = namedtuple('StaffObject', ['img', 'anchor'])

with Image.open(os.path.join(imgpath, 'upnote.png'), mode = 'r') as note:
    upnote = StaffObject(note.copy(), config.upnote_pixels['head_bottom'])

with Image.open(os.path.join(imgpath, 'downnote.png'), mode = 'r') as note:
    downnote = StaffObject(note.copy(), config.downnote_pixels['head_bottom'])

class Staff:
    def __init__(self, length, note_spacing = config.upnote_pixels['width']):
        with Image.open(os.path.join(imgpath, 'staff-blank.png'), mode = 'r') as bg:
            self.img = showstaff.h_concat_img([bg] * length)
            self.cursor = 10
            self.note_spacing = note_spacing

    def addnote(self, note_name):
        position = get_position(note_name)

        if position <= get_position('B3'):
            self.addobject(upnote, position)
        else:
            self.addobject(downnote, position)
            
    def addobject(self, staffobject, position):
        
        pixels_down = int(config.staff_pixels['c_line'] - staffobject.anchor - position * config.staff_pixels['line_spacing'])
        
        self.img.paste(staffobject.img, box = (self.cursor, pixels_down), mask = staffobject.img)
        self.cursor += staffobject.img.width + self.note_spacing

    def show(self):
        self.img.show()


staff = Staff(200)

staff.addnote('F3')
staff.addnote('F4')
staff.addnote('C2')
staff.addnote('D3')
staff.show()
