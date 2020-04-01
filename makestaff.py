import random
from PIL import Image
import os
from math import ceil
from collections import namedtuple
import sys, getopt

# Directories of note and string numbering symbols
notepath = 'individual/'
stringpath = 'string-numbers/'

# Load all staff images from component directories
notepics = {}
for note in os.listdir(notepath):
    with Image.open(notepath + note, mode = 'r') as notepic:
        notepics[note[:-4]] = notepic.copy()
        
stringpics = {}
for string in os.listdir(stringpath):
    with Image.open(stringpath + string, mode = 'r') as stringpic:
        stringpics[int(string[:-4])] = stringpic.copy()

"Split a list into sublists of size n, leaving last sublist smaller"
def divide_chunks(l, n): 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 

"Concatenate a list of images horiizontally"
def h_concat_img(imgs):
    width = sum(img.width for img in imgs)
    height = max(img.height for img in imgs)
    
    concat = Image.new('RGB', (width, height), color=(249,249,249,0))
    
    run_width = 0
    for img in imgs:
        concat.paste(img, (run_width, 0))
        run_width += img.width
    
    return(concat)

"Concatenate a list of images vertically"
def v_concat_img(imgs):
    width = max(img.width for img in imgs)
    height = sum(img.height for img in imgs)
    
    concat = Image.new('RGB', (width, height), color=(249,249,249,0))
    
    run_height = 0
    for img in imgs:
        concat.paste(img, (0, run_height))
        run_height += img.height
    
    return(concat)

"Turn a list of note names into staff components"
def pad_line(chosen_notes, start=False, end=False):

    n = len(chosen_notes)
    phrase_len = 4 * ceil(n/4)

    chosen_notes.extend((phrase_len - n) * ["rest"])

    for i in range(1, phrase_len//4):
        chosen_notes.insert(5*i - 1, "bar")

    chosen_notes.insert(0, "treble-clef")
    
    if start is True:
        chosen_notes.insert(1, "time-signature")   
    else:
        chosen_notes.insert(1, "space")   
    
    if end is True:
        chosen_notes.append("double-bar")
    else:
        chosen_notes.append("end-bar")

"Assemble note and string image"
def get_pic(note):
    if type(note) == tuple:
        return v_concat_img((notepics[note[0]], stringpics[note[1]]))
    
    return notepics[note]

"Assemble a list of notes into a full staff"
def staff_image(notes, bars_per_line):
    lines = list(divide_chunks(notes, 4 * bars_per_line))
    line_imgs = []
    for (i, line) in enumerate(lines):
        padded_line = pad_line(line, i==0, i==len(lines)-1)
        line_imgs.append(h_concat_img([get_pic(note) for note in line]))
    
    return v_concat_img(line_imgs)

### Guitar information

Note = namedtuple("Note", ['octave', 'halfsteps'])

openstrings = {
    6: Note(2, 4),
    5: Note(2, 9),
    4: Note(3, 2),
    3: Note(3, 7),
    2: Note(3, 11),
    1: Note(4, 4)
}

octave_list = [["C"], ["C#", "Db"], ["D"], ["D#", "Eb"], ["E"], ["F"], ["F#", "Gb"], ["G"], ["G#", "Ab"], ["A"], ["A#", "Bb"], ["B"]]

"Get name of note on a given fret of the guitar"
def fretnote(string, fret):
    halfsteps = openstrings[string].halfsteps + fret
    octave = openstrings[string].octave
    
    octave, halfsteps = octave + halfsteps//12, halfsteps % 12
    
    return [note + str(octave) for note in  octave_list[halfsteps]]

"Create a random staff according to specifications"
def make_staff(strings, frets, repeats, bars_per_fret, **kwargs):
    full_notes = []
    
    for _  in range(repeats):
        notes = [(random.choice(fretnote(string, fret)), string)  for string in strings for fret in frets]
        random.shuffle(notes)
        full_notes.extend(notes)
    
    return staff_image(full_notes, bars_per_fret)

### Main

def range_parse(ran):
    if ':' in ran:
        limits = [int(n) for n in ran.split(':')]
        a = limits[0]
        b = limits[1]
        return range(min(a,b), max(a,b) + 1)
    else:
        return [int(n) for n in ran if n in '123456']

def parse():

    # defaults
    args = {
        'strings' : range(1, 7),
        'frets' : range(13),
        'bars_per_fret' : 5,
        'repeats' : 1,
        'output' : 'staff.png'
    }

    options = 's:f:p:b:r:o:'
    long_options = ['strings=', 'frets=', 'position=', 'bars=', 'repeats=', 'filename=']
    
    options, arguments = getopt.getopt(sys.argv[1:], options, long_options)
    
    for o, a in options:
        if o in ('-s', '--strings'):
            args['strings'] = range_parse(a)
        if o in ('-f', '--frets'):
            args['frets'] = range_parse(a)
        if o in ('-p', '--position'):
            args['frets'] = range(int(a), int(a)+4)
        if o in ('-b', '--bars'):
            args['bars_per_fret'] = int(a)
        if o in ('-r', '--repeats'):
            args['repeats'] = int(a)
        if o in ('-o', '--output'):
            args['filename'] = a + '.png'
            

    return args

if __name__ == "__main__":
    args = parse()
    img = make_staff(**args)
    img.save(args['filename'])
