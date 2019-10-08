"""Generate Markov text from text files."""
import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    text_file = open(file_path).read()

    # file_path.close()

    return text_file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    #text_string = open_and_read_file('green-eggs.txt')
    chains = {}

    """pseudocode
    split on every whitespace character to get all words -> list of strings in order
    create bigram: iterate over list of words (range is length of list)
        for each index, access list[i] and list[i + 1]
        create tuple of (list[i], list[i + 1]) -> tuple

        add the tuple to the empty dictionary(chains[tuple] = chains.get(tuple, []).append(list[i + 2]))
    """

    words = text_string.split()

    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])

        if i < len(words) - 2:
            chains[bigram] = chains.get(bigram, [])
            chains[bigram].append(words[i + 2])
        
        else:
            chains[bigram] = None

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    """pseudocode
    a link is: a tuple (key) + a random word from list (value) 
    put this link in a container (our list called words)
    random.choice(chains) -> yields a random tuple for our first link
    first_word, second_word = tuple (unpacking)
    words.extend(first_word, second_word)
    get a random word from the list value: random.choice(chains[tuple])
    words.append( ^ )
    new tuple! is words[-2], words[-1]

    rinse and repeat while chains[tuple] != None
    """

    # give me a random key (bigram) from our dictionary
    link = choice(list(chains.keys()))

    words.append(link[0])
    words.append(link[1])

    while chains[link] != None:
        next_word = choice(chains[link])
        words.append(next_word)
        link = (words[-2], words[-1])


    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
