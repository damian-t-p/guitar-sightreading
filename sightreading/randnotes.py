import random
from collections import namedtuple
from math import ceil

"Split a list into sublists of size n, leaving last sublist smaller"
def divide_chunks(l, n): 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 

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

def is_sharp(note):
    return '#' in note[0]

def is_flat(note):
    return 'b' in note[0]
        
"Create a random staff according to specifications"
def rand_staff(strings, frets, repeats, bars_per_line, diatonic):
    full_notes = []
    
    for _  in range(repeats):
        notes = [(random.choice(fretnote(string, fret)), string)  for string in strings for fret in frets]

        if diatonic is True:
            notes = [note for note in notes if not is_sharp(note) and not is_flat(note)]
        
        random.shuffle(notes)
        full_notes.extend(notes)

    lines = list(divide_chunks(full_notes, 4 * bars_per_line))

    for (i, line) in enumerate(lines):
        pad_line(line, i==0, i==len(lines)-1)
    
    return lines
