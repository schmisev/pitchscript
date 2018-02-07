"""
COMMAND CHARACTERS
"""
ADVANCE_TIME = "_"
PLAY_FOR = "."
PLAY_WHILE = ","
SET_OCTAVE = '"'

TRIGGER_OVERWRITE = {ADVANCE_TIME, PLAY_FOR, PLAY_WHILE}

"""
OTHER CONSTANTS
"""
OCTAVE = 12
STD_OCTAVE = 4
ON = 1
OFF = 0

"""
OUTPUT
"""
PITCH_DICT = {
    0: "C",
    1: "C#/Db",
    2: "D",
    3: "D#/Eb",
    4: "E",
    5: "F",
    6: "F#/Gb",
    7: "G",
    8: "G#/Ab",
    9: "A",
    10: "A#/Bb",
    11: "B",
}

STATUS_DICT = {
    ON: 'on',
    OFF: "off"
}

"""
NOTES AND INCREMENTS
"""
NOTE_DICT = {
    "c": 0,
    "d": 2,
    "e": 4,
    "f": 5,
    "g": 7,
    "a": 9,
    "b": 11,
}

INCREMENT_STD = 0
INCREMENT_DICT = {
    "#": 1,
    "&": -1,
}

"""
CHORDS SHAPES
"""
SHAPE_STD = [4, 7]
SHAPE_DICT = {
    "m": [3, 7],
    "dim": [3, 6],
    "aug": [4, 8],
    "sus2": [2, 7],
    "sus4": [5, 7],
    "7": [4, 7, 10],
    "6": [4, 7, 9],
    "m7": [3, 7, 10],
    "m6": [3, 7, 9],
    "maj7": [4, 7, 11],
    "add9": [4, 7, 14],
    "madd9": [3, 7, 10],
    "7sus4": [5, 7, 10],
}

"""
HELPER FUNCTION for OR-regular-expressions
"""
def create_or_re(keys: list) -> str:
    return "({})".format("|".join(sorted(keys)[::-1]))

"""
REGULAR EXPRESSIONS
"""
NOTE_OR = create_or_re(NOTE_DICT.keys())
INCREMENT_OR = create_or_re(INCREMENT_DICT.keys())
SHAPE_OR = create_or_re(SHAPE_DICT.keys())
COMMAND_OR = "[{}]".format(ADVANCE_TIME + PLAY_FOR + PLAY_WHILE + SET_OCTAVE)

"""
TOKEN EXPRESSIONS
"""
TOKEN_RE =\
r"(?P<command>{}[0-9]*)|(?P<root>{})(?P<increment>{})?(?P<sci>[0-9]+)?((?P<shape>\'{}?)((?P<inv>[/]{})(?P<invincr>{})?)?)?".format(COMMAND_OR, NOTE_OR, INCREMENT_OR, SHAPE_OR, NOTE_OR, INCREMENT_OR)

"""
MACRO EXPRESSIONS
"""
MACRO_RE =\
r"(?P<expr>.*?)[ ](?P<sub>.*?)\n"