Pitchscript
===========

Pitchscript is a simple music notation system that translates to midi-like data.

Pitchscript uses a sort of "write head", in which pitches (notes and/or chords) are stored. They can then be "written" to the midi-like datastructure with the help of some commands.

There are thus only TWO basic types of commands
- Update/overwrite pitches in write head
- Single-character prefix commands for adding notes, rests and adjusting the global pitch/octave

Grammar
-------
Note/chord syntax:

- Notes/chords are written with
- a root note (lowercase letters a-g)
- opt: increments sharp (#) or flat (&)
- opt: absolute octave (ignores global reference octave) (numbers [0-9]+)
- opt: chord prefix (') and chord shape (e.g. maj7)
- opt: inversion prefix (/) and inversion pivot (lowercase letters a-g) (when the pivot is in the chord, the chord is inverted so the pivot becomes the lowest note; when it is not, it is shifted one octave down,making it a bass note)

In order to add notes and chords to the writehead, they are just written in sequence without being interupted by timing commands. Else the writehead is overwritten.

Examples:
- c4        adds pitch value 48 to the write head
- c e g     adds pitch values 0, 4, 7 to the write head for global octave 0
- c'm/a#    adds pitch values 46, 48, 51, 55 for global octave 4, the a#
            has been made a bass note (46)

Single-character prefix commands:

- "[0-9]+     set global octave

- _[0-9]+     advance time by / rest for given number of beats
- .[0-9]+     play for and advance time by ...
- ,[0-9]+     play for, but do not advance time ...

Note: Unneccesary characters such as spaces are ignored.

Full example:

"4 c3'm7,8 c.2 e&.2_2 g.2 a#.2

Run-through:
- "4        sets global ovtave to 4
- c3'm7     adds pitches of a Cm7 in the 3rd octave to the write head
- ,8        plays chord for 8 beats, without advancing time
- c         overwrites pitches in writehead with C4
- .2        plays C4 for 2 beats and advances time
and so on...
