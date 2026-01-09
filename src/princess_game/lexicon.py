class Lexicon(object):
    def __init__(self):
        self.directions = ["north","south","east","west","up","down","left","right","back"]
        self.verbs = ["go","stop","move","kill","pick","take","quit","help"]
        self.items = ["crown","map","key"]

    def classify_word(self,word):
        word = word.lower()
        if word in self.directions:
            return ("direction", word)
        elif word in self.verbs:
            return ("verb", word)
        elif word in self.items:
            return ("item", word)
        else:
            return ("error", word)
        
    def scan(self, command):
        return ([self.classify_word(word) for word in command.split()])