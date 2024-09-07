class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current_num = 0 - step

    def __iter__(self):
        return self

    def __next__(self):

        if self.count > 0:
            self.current_num += self.step
            self.count -= 1
            return self.current_num

        raise StopIteration


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
