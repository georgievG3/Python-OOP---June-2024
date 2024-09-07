def logged(func):

    def warpper(*args, **kwargs):
        return f"you called {func.__name__}{args}\nit returned {func(*args)}"

    return warpper


@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))