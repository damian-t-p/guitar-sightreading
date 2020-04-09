from PIL import Image
import os

# Directories of note and string numbering symbols
notepath = os.path.join(os.path.dirname(__file__), 'resources', 'staff-symbols')
stringpath = os.path.join(os.path.dirname(__file__), 'resources', 'string-numbers')

# Load all staff images from component directories
notepics = {}
for note in os.listdir(notepath):
    with Image.open(os.path.join(notepath, note), mode = 'r') as notepic:
        notepics[note[:-4]] = notepic.copy()
        
stringpics = {}
for string in os.listdir(stringpath):
    with Image.open(os.path.join(stringpath, string), mode = 'r') as stringpic:
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

"Assemble note and string image"
def get_pic(note, string_symbols):
    if type(note) == tuple:
        if string_symbols is True:
            return v_concat_img((notepics[note[0]], stringpics[note[1]]))
        else:
            return notepics[note[0]]
    
    return notepics[note]

"Assemble a list of notes into a full staff"
def staff_image(lines, string_symbols):
    line_imgs = []
    for line in lines:
        line_imgs.append(h_concat_img([get_pic(note, string_symbols) for note in line]))
    
    return v_concat_img(line_imgs)
