def fibonacci():
    first_num = 0
    second_num = 1

    yield first_num
    yield second_num

    while True:
        current_num = first_num + second_num
        yield current_num
        first_num = second_num
        second_num = current_num


generator = fibonacci()
for i in range(1):
    print(next(generator))