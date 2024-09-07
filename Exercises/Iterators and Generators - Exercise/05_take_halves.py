def solution():
    def integers(start=1):

        while True:
            yield start
            start += 1

    def halves():

        numbers = integers()

        for n in numbers:
            yield n / 2

    def take(n, seq):
        result = []
        step = 0

        for num in seq:
            step += 1

            if step > n:
                break

            result.append(num)

        return result

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
