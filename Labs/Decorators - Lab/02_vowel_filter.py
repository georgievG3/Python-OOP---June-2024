def vowel_filter(function):
    VOWELS = ["a", "e", "i", "o", "u"]

    def wrapper():

        letters = function()
        vowel_letters = [el for el in letters if el in VOWELS]
        return vowel_letters

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())