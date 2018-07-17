from itertools import cycle, islice

class Scales(object):
    def __init__(self):
        pass
        # self.major = [2,2,1,2,2,2,1]


# major = [1,2,3,4,5,6,7,8]

# scale = Scales()

def mode(scale, degree, intervals=7):
    notes = cycle(scale)
    degree -= 1
    new_scale = [i for i in islice(notes, degree, intervals + degree)]
    return new_scale


def keymap(intervals):
    note = 36 # offset
    notes = [note]

    pattern = [i for i in islice(cycle(intervals), 0, 88)]
    # print(pattern)

    for p in pattern:
        # print(p, note)
        note = p + note
        notes.append(note)

    return [i for i in enumerate(notes, 1)]

def make_files(scales):
    for name,scale in scales.items():
        print(name, scale)
        print(name, keymap(scale))
        with open(name,'w') as f:
            mappings = keymap(scale)
            for k,v in mappings:
                f.write('{}, {};\n'.format(k,v))

if __name__ == '__main__':
    ionian1 = [2, 2, 1, 2, 2, 2, 1]

    scales = {
    'ionian1' : ionian1,
    'dorian2' : mode(ionian1, 2),
    'phrygian3' : mode(ionian1, 3),
    'lydian4' : mode(ionian1, 4),
    'mixolydian5' : mode(ionian1, 5),
    'aeolian6' : mode(ionian1, 6),
    'locrian7' : mode(ionian1, 7)
    }

    make_files(scales)
        # x = keymap(scales[scale])
