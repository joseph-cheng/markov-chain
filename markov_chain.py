import random
import numpy.random as np
import re

class MarkovChain:
    def __init__(self):
        self.state = {}

    def train(self, data):
        self.state = {item:{} for item in set(data)}
        for i, x in enumerate(data):
            if i+1 == len(data):
                self.state[x][None] = self.state[x].get(None, 0)+1
                break
            self.state[x][data[i+1]] = self.state[x].get(data[i+1], 0) + 1

        for item in self.state:
            counts = self.state[item]
            total_count = sum(counts.values())
            for i in counts:
                self.state[item][i] = self.state[item][i]/total_count



    def generate(self):
        final = [random.choice(list(self.state.keys()))]

        i=0
        while True:
            values = list(self.state[final[i]].keys())
            distribution = [self.state[final[i]][x] for x in values]
            final.append(np.choice(values, p=distribution))
            if final[-1] == None:
                return final[:-1]
            i+=1

    def clean_state(self):
        self.state = {}



m = MarkovChain()
c = """
As he spoke the gleam of the sidelights of a carriage came round the curve of the avenue. It was a smart little landau which rattled up to the door of Briony Lodge. As it pulled up, one of the loafing men at the corner dashed forward to open the door in the hope of earning a copper, but was elbowed away by another loafer, who had rushed up with the same intention. A fierce quarrel broke out, which was increased by the two guardsmen, who took sides with one of the loungers, and by the scissors-grinder, who was equally hot upon the other side. A blow was struck, and in an instant the lady, who had stepped from her carriage, was the centre of a little knot of flushed and struggling men, who struck savagely at each other with their fists and sticks. Holmes dashed into the crowd to protect the lady; but, just as he reached her, he gave a cry and dropped to the ground, with the blood running freely down his face. At his fall the guardsmen took to their heels in one direction and the loungers in the other, while a number of better dressed people, who had watched the scuffle without taking part in it, crowded in to help the lady and to attend to the injured man. Irene Adler, as I will still call her, had hurried up the steps; but she stood at the top with her superb figure outlined against the lights of the hall, looking back into the street.
"""
c = re.split("(\W)", c)
m.train(c)
print("".join(m.generate()))