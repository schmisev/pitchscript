from ps_parsing import Parser
from ps_output import print_timetable, play_timetable
import sys

"""
Command-line reply function
Exit: $
"""
def repl():
    p = Parser()
    while True:
        chars = input(">> ")
        if chars == "$":
            return
        p.write(chars)
        p.beautify_timetable()
        print_timetable(p.get_timetable())
        play_timetable(p.get_timetable())

"""
Compiler function
"""
def comp(argv):
    f = open(argv[1])
    p = Parser()
    p.write(f.read())
    p.beautify_timetable()
    print_timetable(p.get_timetable())
    play_timetable(p.get_timetable())

if __name__ == "__main__":
    if len(sys.argv) > 1:
        comp(sys.argv)
    else:
        repl()