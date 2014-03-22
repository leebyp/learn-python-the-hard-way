def break_words(stuff):
    """This function will break up words for us."""     #documentation comments, check with help(ex25.break_words)
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# python
# import ex25      (import module into console)
# from ex25 import *        (import everything from module, use function without ex25.)

# sentence = "All good things come to those who wait."
# words = ex25.break_words(sentence)        (run the function within the module)

# sorted_words = ex25.sort_words(words)

# ex25.print_first_word(words)

# ex25.print_last_word(words)

# sorted_words = ex25.sort_sentence(sentence)

# ex25.print_first_and_last(sentence)

# ex25.print_first_and_last_sorted(sentence)