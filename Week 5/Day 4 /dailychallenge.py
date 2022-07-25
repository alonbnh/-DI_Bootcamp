class Text:
    def __init__(self, text):
        self.text=text

    def freq(self):
            counts = dict()
            words = self.split()

            for word in words:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1

            return counts


Text.freq("A good book would sometimes cost as much as a good house.")



