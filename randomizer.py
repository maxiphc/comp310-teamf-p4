import time
import math

class PseudoRandom:
    
    def __init__(self):
        self.seed = -1
        self.prev = 0
        self.a = 25214903917
        self.c = 11
        self.m = 2**31

    def get_seed(self):
        seed = time.monotonic() 
        self.seed = int(str(seed)[-3:])  # taking the 3 decimal places at the end of what is returned by time.monotonic()

    def generate_random(self, prev_random, range):
        """
        Returns a pseudorandom number between 1 and range.
        """
        # if first value, then get the seed to determine starting point
        if self.seed == -1:
            self.get_seed()
            self.prev = raw_num = (self.a * self.seed + self.c) % self.m
        # use previous value to determine next number
        else:
            self.prev = raw_num = (self.a * prev_random + self.c) % self.m
        
        return math.ceil((raw_num / self.m) * range)

if __name__ == "__main__":
    test = PseudoRandom()
    for i in range(10):
        rand = test.generate_random(test.prev, 10)
        print(rand)