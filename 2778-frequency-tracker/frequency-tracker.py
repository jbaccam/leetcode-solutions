class FrequencyTracker:

    def __init__(self):
        self.frequency = defaultdict(int) # use to map frequency to number, key will be frequency
        self.numbers = defaultdict(int) # use to map numbers to frequency, key will be number
        
    def add(self, number: int) -> None:
        # decrement the previous frequency
        prevfreq = self.numbers[number]
        self.frequency[prevfreq] -= 1

        # incremenet the numbers frequency
        self.numbers[number] += 1
        # increment how many times this frequency is in here
        freq = self.numbers[number]
        self.frequency[freq] += 1

    def deleteOne(self, number: int) -> None:
        if self.numbers[number] > 0:
            prevfreq = self.numbers[number]
            self.frequency[prevfreq] -= 1
            self.numbers[number] -= 1
            freq = self.numbers[number]
            self.frequency[freq] += 1

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.frequency and self.frequency[frequency] > 0:
            return True
        else:
            return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)