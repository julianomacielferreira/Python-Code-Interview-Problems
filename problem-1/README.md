## Valid Anagram

Given two strings ``str1`` and ``str2``, verify if they are anagrams.

Two strings are ``anagrams`` if they are made of the same characters with the same frequencies, just with a different order.

Summarizing, the solution just compare the frequencies of characters of ``str1`` to the frequencies of characters of ``str2``, if they're equals return True, otherwise return False.

Examples:

- triangle / integral
- danger / garden
- peach / cheap
- elbow / below
- cat / act

Some words to validate:

```python
# Data example
words = {
    'triangle': 'integral',
    'danger': 'garden',
    'hot': 'dog',
    'elbow': 'below',
    'peach': 'cheap',
    'cat': 'act',
    'cart': 'star',
    'TRIANGLE': 'integral',
    'juliano': 'giuliano',
    'arithmetic': 'geometrics'
}
```

A first [solution](valid_anagram_v1.py) can be:

```python
def count_frequencies_of(word):
    """
        Utility function to count frequencies of a letter in a string

        Params:
            word (str): Word to count the letter frequencies

        Returns:
            frequency_counter (dict): the dictionary of letters and frequencies
    """
    frequency_counter = {}

    for char in word.lower():
        if char in frequency_counter:
            frequency_counter[char] += 1
        else:
            frequency_counter[char] = 1

    return frequency_counter


def is_anagram_v1(word_a, word_b):
    """
        Verify if two string are anagram

        Params:
            word_A (str): First word to compare
            word_B (str): Second word to compare

        Returns:
            True if they are anagrams, False otherwise
    """
    # Check the lengths
    if len(word_a) != len(word_b):
        return False

    frequencies_of_a = count_frequencies_of(word_a)

    frequencies_of_b = count_frequencies_of(word_b)

    return frequencies_of_a == frequencies_of_b


# Checking with examples
if __name__ == "__main__":
    for key in words:
        print(
            'Is the word "{0}" is anagram of "{1}"? {2}'.format(
                key, words[key], is_anagram_v1(key, words[key]))
        )



```

A second [solution](valid_anagram_v2.py):

```python
def is_anagram_v2(word_a, word_b):
    """
        Verify if two string are anagram

        Params:
            word_a (str): First word to compare
            word_b (str): Second word to compare

        Returns:
            True if they are anagrams, False otherwise
    """
    # Check the lengths
    if len(word_a) != len(word_b):
        return False

    # Iterate through str1 and check if str2 contains each character too
    for char1 in word_a.lower():
        if char1 not in word_b.lower():
            return False

    return True


# Checking with examples
if __name__ == "__main__":
    for key in words:
        print(
            'Is the word "{0}" is anagram of "{1}"? {2}'.format(
                key, words[key], is_anagram_v2(key, words[key]))
        )
```

A third [solution](valid_anagram_v3.py):

```python
from collections import Counter


def is_anagram_v3(word_a, word_b):
    """
        Verify if two string are anagram

        Params:
            word_a (str): First word to compare
            word_b (str): Second word to compare

        Returns:
            True if they are anagrams, False otherwise
    """
    # Check the lengths
    if len(word_a) != len(word_b):
        return False

    return Counter(word_a) == Counter(word_b)


# Checking with examples
for key in words:
    print(
        'Is the word "{0}" is anagram of "{1}"? {2}'.format(
            key, words[key], is_anagram_v3(key, words[key]))
    )

```

A fourth [solution](valid_anagram_v4.py):

```python
def is_anagram_v4(word_a, word_b):
    """
        Verify if two string are anagram

        Params:
            word_a (str): First word to compare
            word_b (str): Second word to compare

        Returns:
            True if they are anagrams, False otherwise
    """
    # Check the lengths
    if len(word_a) != len(word_b):
        return False

    return sorted(word_a) == sorted(word_b)


# Checking with examples
if __name__ == "__main__":
    for key in words:
        print(
            'Is the word "{0}" is anagram of "{1}"? {2}'.format(
                key, words[key], is_anagram_v4(key, words[key]))
        )
```

The output:

```
Is the word "triangle" is anagram of "integral"? True
Is the word "danger" is anagram of "garden"? True
Is the word "hot" is anagram of "dog"? False
Is the word "elbow" is anagram of "below"? True
Is the word "peach" is anagram of "cheap"? True
Is the word "cat" is anagram of "act"? True
Is the word "cart" is anagram of "star"? False
Is the word "TRIANGLE" is anagram of "integral"? True
Is the word "juliano" is anagram of "giuliano"? False
Is the word "arithmetic" is anagram of "geometrics"? False
```