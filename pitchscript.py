from ps_parsing import Parser
from ps_macros import Preprocessor
from ps_output import print_timetable, play_timetable
import sys

"""
Command-line reply function
Exit: $
"""
def repl():
    p = Parser()
    pp = Preprocessor()
    while True:
        chars = input(">> ")
        if chars == "$":
            return
        pp_chars = pp.preprocess(chars)
        p.write(pp_chars)
        p.beautify_timetable()
        print_timetable(p.get_timetable())
        play_timetable(p.get_timetable())

"""
Compiler function
"""
def comp(argv):
    f = open(argv[1])
    p = Parser()
    pp = Preprocessor()
    pp_chars = pp.preprocess(f.read())
    p.write(pp_chars)
    p.beautify_timetable()
    print_timetable(p.get_timetable())
    play_timetable(p.get_timetable())

if __name__ == "__main__":
    if len(sys.argv) > 1:
        comp(sys.argv)
    else:
        repl()