from ps_constants import *
from ps_music_theory import invert_chord
import re

class Parser:
    def __init__(self):
        # Resulting timetable (MIDI-like)
        # Structure: [time, pitch, on = 0 | off = 1]
        self.timetable = list()

        # State variable
        self.time = 0
        self.current = list()
        self.octave = STD_OCTAVE

        # Flags
        self.overwrite = False

    """
    Getter for ordered timetable
    """
    def get_timetable(self):
        return sorted(self.timetable)

    """
    Beautify timetable (remove redundancies and dead actions)
    """
    def beautify_timetable(self):
        new_timetable = list()
        active = set()
        for t in sorted(self.timetable):
            _, status, pitch = t
            # Check if legal input
            if status == ON:
                new_timetable.append(t)
                if pitch not in active:
                    active.add(pitch)
            elif status == OFF and pitch in active:
                new_timetable.append(t)
                active.remove(pitch)
        self.timetable = new_timetable

    """
    Handles command tokens
    """
    def handle_command(self, token):
        # Check if single character command
        if len(token) == 1:
            cmd, arg = token, 0
        elif len(token) > 1:
            cmd, arg = token[0], int(token[1:])
        else:
            raise SyntaxError("Illegal command")

        # Executing commands
        # If notes are supposed to be played
        if (cmd == PLAY_WHILE or cmd == PLAY_FOR) and arg != 0:
            for pitch in self.current:
                _on = [self.time, ON, pitch]
                _off = [self.time + arg, OFF, pitch]
                if _on not in self.timetable:
                    self.timetable.append(_on)
                if _off not in self.timetable:
                    self.timetable.append(_off)
        # If time is supposed to be advanced
        if cmd == ADVANCE_TIME or cmd == PLAY_FOR:
            self.time += arg
        # If the reference octave is supposed to be changed
        if cmd == SET_OCTAVE:
            self.octave = arg
        
        # Check for group breaking
        if cmd in TRIGGER_OVERWRITE:
            self.overwrite = True
    
    """
    Handles pitch (sub-)tokens
    """
    def handle_pitches(self, root, increment, sci, shape, inv, invincr):
        # Translating subtokens
        _root = NOTE_DICT.get(root, 0)
        _increment = INCREMENT_DICT.get(increment, 0)
        _sci = int(sci) if sci else self.octave

        # Creating absolute pitch list
        root_pitch = _root + _increment + _sci * OCTAVE
        pitches = [root_pitch]

        # Handling chord shapes
        if shape:
            pitches += [
                s + root_pitch for s in SHAPE_DICT.get(shape[1:], SHAPE_STD)
                ]
        if inv:
            pivot_pitch = NOTE_DICT.get(inv[1:], _root) + INCREMENT_DICT.get(invincr, 0) + _sci
            pitches = invert_chord(pitches, pivot_pitch)
        
        if self.overwrite:
            self.current = list()
            self.overwrite = False
        
        self.current += pitches
    
    """
    Parses script and writes it to the timetable
    """
    def write(self, script, reset_time=True, reset_timetable=True):
        # Possible resets
        if reset_time:
            self.time = 0
        if reset_timetable:
            self.timetable = list()

        # Parsing
        tokens = re.finditer(TOKEN_RE, script)

        # Reading tokens
        for t in tokens:
            tags = t.groupdict()

            if tags["command"]:
                self.handle_command(tags["command"])
            elif tags["root"]:
                self.handle_pitches(
                    tags["root"],
                    tags["increment"],
                    tags["sci"],
                    tags["shape"],
                    tags["inv"],
                    tags["invincr"]
                    )
        
        self.current = list()