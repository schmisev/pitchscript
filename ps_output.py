from ps_constants import ON, OFF, STATUS_DICT, PITCH_DICT, OCTAVE
from pygame import midi as md
import time as dt

"""
Simple printing for timetable
expects sorted timetable
"""
def print_timetable(timetable):
    for t in timetable:
        time, status, pitch = t
        out_str = "{}{}: {}{} -> {}".format(
            "\t" if status == OFF else "",
            str(time),
            PITCH_DICT.get(pitch % 12, "???"),
            str(pitch // OCTAVE),
            STATUS_DICT.get(status, "???")
        )
        print(out_str)

"""
Pretty printing for timetable
expects sorted, cleaned timetable
"""
...

"""
Midi player
expects sorted timetable
"""
def play_timetable(timetable, velocity=127, bpm=200):
    md.init()
    out_id = md.get_default_output_id()
    midi_out = md.Output(out_id)

    bps = bpm / 60
    clock = 0

    for t in timetable:
        time, status, pitch = t
        if time > clock:
            dt.sleep((time - clock) / bps)
            clock = time
        if status == ON:
            midi_out.note_on(pitch, velocity)
        elif status == OFF:
            midi_out.note_off(pitch, velocity)
    
    midi_out.close()
    md.quit()

"""
Midi player
expects channels
"""
def play_channels(channels, velocity=64, bpm=200, instruments=[0]):
    # Prepare channels
    merged = list()
    for i in range(len(channels)):
        for c in channels[i]:
            merged.append(c + [i])
    merged.sort()

    # Prepare output
    md.init()
    out_id = md.get_default_output_id()
    midi_out = md.Output(out_id)

    for i in range(len(instruments)):
        midi_out.set_instrument(instruments[i], i)

    bps = bpm / 60
    clock = 0

    for t in merged:
        time, status, pitch, channel = t
        if time > clock:
            dt.sleep((time - clock) / bps)
            clock = time
        if status == ON:
            midi_out.note_on(pitch, velocity, channel)
        elif status == OFF:
            midi_out.note_off(pitch, velocity, channel)
    
    midi_out.close()
    md.quit()