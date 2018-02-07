import re
from ps_constants import MACRO_RE

class Preprocessor:
    def __init__(self):
        matches = re.finditer(MACRO_RE, open("macros.txt").read())
        self.subs = list()

        for m in matches:
            tags = m.groupdict()
            self.subs.append([tags["expr"], tags["sub"]])
        
        self.subs.sort()
        self.subs.reverse()

    
    """
    Uses extracted macro rules to rewrite input
    """
    def preprocess(self, chars: str):
        new_chars = chars
        for s in self.subs:
            new_chars = new_chars.replace(s[0], s[1])
        return new_chars