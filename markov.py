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


def make_chains(text_string, n=2):
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

    for i in range(len(words) - n + 1):
        #pseudocode update:
        # iterate over a new range using n 
        # keep rebinding our tuple to have +1 entry at the end from our text string
        # 
        # bigram = (words[i], words[i + 1])
        n_gram = (words[i], )

        for sub_idx in range(1, n):
            n_gram += (words[i + sub_idx],)

        if i < len(words) - n:
            chains[n_gram] = chains.get(n_gram, [])
            chains[n_gram].append(words[i + n])
        
        else:
            chains[n_gram] = None

    return chains


def make_text(chains, n=2, sentence_limit=5):
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
    #link = choice(list(chains.keys()))
    
    # modified: give me a bigram iff choice(list(chains.keys()))[0][0].upper == choice(list(chains.keys()))[0][0]
    # what does that mean?? 
    # if the upper version of4the first letter of the first tuple object is the
    # same as the current first letter of the first tuple, it's a capital letter
    # and can start our markov text.
    end_punctuation = ".?!"
    link = choice(list(chains.keys()))
    starting_letter = link[0][0]
    num_of_sentences = 0

    while starting_letter != starting_letter.upper() or not starting_letter.isalpha():
        # if starting letter ('a') is different than upper ('A') 
        # or
        # if starting letter is not alpha ('-', '.', etc.) 
        link = choice(list(chains.keys()))
        starting_letter = link[0][0]

    for i in range(n):
        words.append(link[i])

    while chains[link] != None and num_of_sentences < sentence_limit:
        next_word = choice(chains[link])
        # num_of_sentences += 1 if (next_word[-1] in end_punctuation)
        if next_word[-1] in end_punctuation:
            num_of_sentences += 1
        words.append(next_word)
        link = tuple(words[-n:])        

    return " ".join(words)


input_path = sys.argv[1]

n = int(sys.argv[2])

sentence_limit = int(sys.argv[3])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n)

# Produce random text
random_text = make_text(chains, n)

print(random_text)
