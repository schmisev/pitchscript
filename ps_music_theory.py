from ps_constants import OCTAVE

"""
Inversion function for a chord and an inversion pivot
- Pivot in chord: inverts chord by up-shifting by an octave
- Pivot not in chord: down-shifts pivot by an octave
  and adds it to the chord
"""
def invert_chord(chord, pivot):
    if pivot in chord:
        return [c + OCTAVE if c < pivot else c for c in chord]
    else: return chord + [pivot - OCTAVE]