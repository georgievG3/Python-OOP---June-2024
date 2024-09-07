class dictionary_iter:

    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.keys = [k for k in self.dictionary.keys()]
        self.step = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.step < len(self.keys):
            self.step += 1
            return (self.keys[self.step - 1], self.dictionary[self.keys[self.step - 1]])

        raise StopIteration


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
