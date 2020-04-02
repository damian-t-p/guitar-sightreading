import sys
import getopt

from .randnotes import rand_staff
from .showstaff import staff_image

def range_parse(ran):
    if ':' in ran:
        limits = [int(n) for n in ran.split(':')]
        a = limits[0]
        b = limits[1]
        return range(min(a,b), max(a,b) + 1)
    else:
        return [int(n) for n in ran if n in '123456']

def parse_cmd_args():

    class Args:
        def __init__(self, staff, filename):
            self.staff = staff
            self.filename = filename
    
    # defaults
    args = Args({'strings' : range(1, 7),
                 'frets' : range(13),
                 'bars_per_line' : 5,
                 'repeats' : 1},
                'staff.png')


    options = 's:f:p:b:r:o:'
    long_options = ['strings=', 'frets=', 'position=', 'bars=', 'repeats=', 'output=']
    
    options, arguments = getopt.getopt(sys.argv[1:], options, long_options)
    
    for o, a in options:
        if o in ('-s', '--strings'):
            args.staff['strings'] = range_parse(a)
        if o in ('-f', '--frets'):
            args.staff['frets'] = range_parse(a)
        if o in ('-p', '--position'):
            args.staff['frets'] = range(int(a), int(a)+4)
        if o in ('-b', '--bars'):
            args.staff['bars_per_line'] = int(a)
        if o in ('-r', '--repeats'):
            args.staff['repeats'] = int(a)
        if o in ('-o', '--output'):
            args.filename = a + '.png'

    return args

def main():
#if __name__ == "__main__":
    args = parse_cmd_args()

    staffspec = rand_staff(**args.staff)
    staffimg = staff_image(staffspec)
    
    staffimg.save(args.filename)
