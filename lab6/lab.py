"""6.009 Lab 6 -- Autocomplete"""

# NO ADDITIONAL IMPORTS!
from text_tokenize import tokenize_sentences

class Trie:
    def __init__(self):
        """
        Initialize an empty trie.
        """
        self.value = None
        self.children = {}
        self.type = None

    def __getitem__(self, key):
        """
        Return the value for the specified prefix.  If the given key is not in
        the trie, raise a KeyError.  If the given key is of the wrong type,
        raise a TypeError.
        """
        if not isinstance(key, self.type):
            raise TypeError
        if len(key) == 0:
            if self.value == None:
                raise KeyError
            else:
                return self.value
        letter = key[0:1]
        if letter not in self.children:
            raise KeyError
        return self.children[letter][key[1:]]


    def __setitem__(self, key, value):
        """
        Add a key with the given value to the trie, or reassign the associated
        value if it is already present in the trie.  Assume that key is an
        immutable ordered sequence.  Raise a TypeError if the given key is of
        the wrong type.
        """
        if self.type == None:
            self.type = type(key)
        if not isinstance(key, self.type):
            raise TypeError
        if len(key) == 0:
            self.value = value
        else:
            letter = key[0:1]
            if letter in self.children:
                self.children[letter][key[1:]] = value
            else:
                child = Trie()
                self.children[letter] = child
                self.children[letter][key[1:]] = value

    def __delitem__(self, key):
        """
        Delete the given key from the trie if it exists.
        """
        if len(key) == 0:
            self.value = None
        elif key[0:1] in self.children:
            letter = key[0:1]
            del self.children[letter][key[1:]]

    def __contains__(self, key):
        """
        Return True if key is in the trie and has a value, return False otherwise.
        """
        if len(key) == 0:
            if self.value != None:
                return True
            else:
                return False
        elif key[0:1] in self.children:
            letter = key[0:1]
            return key[1:] in self.children[letter]

    def __iter__(self):
        """
        Generator of (key, value) pairs for all keys/values in this trie and
        its children.  Must be a generator or iterator!
        """
        if self.value != None:
            yield(self.type(), self.value)
        for child in self.children:
            for key, val in self.children[child]:
                yield (child + key, val)

def make_word_trie(text):
    """
    Given a piece of text as a single string, return a Trie whose keys are the
    words in the text, and whose values are the number of times the associated
    word appears in the text
    """
    sentences = tokenize_sentences(text, remove_punctuation=True)
    corpus = []
    for sentence in sentences:
        corpus += sentence.split()
    t = Trie()
    for word in corpus:
        if word in t:
            t[word] += 1
        else:
            t[word] = 1
    return t


def make_phrase_trie(text):
    """
    Given a piece of text as a single string, return a Trie whose keys are the
    sentences in the text (as tuples of individual words) and whose values are
    the number of times the associated sentence appears in the text.
    """
    sentences = tokenize_sentences(text, remove_punctuation=True)
    t = Trie()
    keys = [tuple(sentence.split()) for sentence in sentences]
    for key in keys:
        if key in t:
            t[key] += 1
        else:
            t[key] = 1
    return t


def autocomplete(trie, prefix, max_count=None):
    """
    Return the list of the most-frequently occurring elements that start with
    the given prefix.  Include only the top max_count elements if max_count is
    specified, otherwise return all.

    Raise a TypeError if the given prefix is of an inappropriate type for the
    trie.

    Do not use a brute-force method that involves generating/looping over
    all the words in the trie.
    """
    if trie.type != type(prefix):
        raise TypeError
    if len(prefix) == 0:
        pairs = [pair for pair in trie]
        pairs.sort(reverse=True, key=lambda x: x[1])
        words = [pair[0] for pair in pairs]
        if max_count != None:
            words = words[:max_count]
        return words
    letter = prefix[0:1]
    try:
        suffixes = autocomplete(trie.children[letter], prefix[1:], max_count)
    except:
        return []
    return [letter + suffix for suffix in suffixes]


def autocorrect(trie, prefix, max_count=None):
    """
    Return the list of the most-frequent words that start with prefix or that
    are valid words that differ from prefix by a small edit.  Include up to
    max_count elements from the autocompletion.  If autocompletion produces
    fewer than max_count elements, include the most-frequently-occurring valid
    edits of the given word as well, up to max_count total elements.

    Do not use a brute-force method that involves generating/looping over
    all the words in the trie.
    """
    if max_count == 0:
        return []

    def edits(trie, prefix):
        corrections = []
        #insertions
        for letter in trie.children:
            if prefix in trie.children[letter]:
                 corrections.append((letter + prefix, trie[letter + prefix]))
        #deletions
        if prefix[1:] in trie:
            corrections.append((prefix[1:], trie[prefix[1:]]))
        #replacements
        for letter in trie.children:
            if prefix[1:] in trie.children[letter]:
                corrections.append((letter + prefix[1:], trie[letter + prefix[1:]]))
        #swaps
        swap = prefix[1:2] + prefix[0:1] + prefix[2:]
        if swap in trie:
            corrections.append((swap, trie[swap]))

        try:
            if prefix[0] in trie.children:
                corrections += [(prefix[0]+key,val) for key,val in edits(trie.children[prefix[0]],prefix[1:])]
        except:
            pass

        return set(corrections)



    completions = autocomplete(trie, prefix, max_count)
    if len(completions) == max_count:
        return completions
    corrections = list(edits(trie, prefix))
    corrections.sort(key=lambda x:x[1])
    words = [correction[0] for correction in corrections]
    if max_count == None:
        return list(set(completions + words))
    if len(completions) < max_count:
        while len(completions) < max_count:
            edit = words.pop()
            completions.append(edit)
        return completions

def word_filter(trie, pattern):
    """
    Return list of (word, freq) for all words in trie that match pattern.
    pattern is a string, interpreted as explained below:
         * matches any sequence of zero or more characters,
         ? matches any single character,
         otherwise char in pattern char must equal char in word.

    Do not use a brute-force method that involves generating/looping over
    all the words in the trie.
    """
    if len(pattern) == 0:
        if trie.value != None:
            return [('', trie.value)]
    letter = pattern[0:1]
    matches = []
    if letter == '*':
        matches += word_filter(trie, pattern[1:])
        for child in trie.children:
            #take *
            matches += [(child + key, val) for key, val in word_filter(trie.children[child], pattern[1:])]
            #use * again
            matches += [(child + key, val) for key, val in word_filter(trie.children[child], pattern)]
    elif letter == '?':
        for child in trie.children:
            matches += [(child + key, val) for key, val in word_filter(trie.children[child], pattern[1:])]
    else:
        if letter in trie.children:
            matches += [(letter + key, val) for key, val in word_filter(trie.children[letter], pattern[1:])]
    return list(set(matches))



# you can include test cases of your own in the block below.
if __name__ == '__main__':
    trie = Trie()
    trie[(1, 2, 3)] = 'kitten'
    trie[(1, 2, 0)] = 'tricycle'
    trie[(1, 2, 0, 1)] = 'rug'
