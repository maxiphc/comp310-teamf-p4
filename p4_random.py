import time

class PseudoRandom:
    
    def __init__(self):
        self.seed = -1
        self.a = 25214903917
        self.c = 11
        self.m = 2**31

    def get_seed(self):
        seed = time.monotonic() 
        self.seed = int(str(seed)[-3:])  # taking the 3 decimal places at the end of what is returned by time.monotonic()

    def generate_random(self, prev_random):
        """
        Generate random numbers 
        """
        # if first value, then get the seed to determine starting point
        if self.seed == -1:
            self.get_seed()
            return (self.a * self.seed + self.c) % self.m
            # return ( (self.a * self.seed + self.c) % self.m ) / self.m  # use for random percent 
        # use previous value to determine next number
        else:
            return (self.a * prev_random + self.c) % self.m
            # return ( (self.a * prev_random + self.c) % self.m ) / self.m  # use for random percent

if __name__ == "__main__":
    test = PseudoRandom()
    rand = 0
    for i in range(10):
        rand = test.generate_random(rand)
        print(rand / test.m)