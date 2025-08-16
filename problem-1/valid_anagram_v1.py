"""
The MIT License

Copyright 2025 Juliano Maciel.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
from data import words


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


def is_anagram(word_a, word_b):
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

    frequencies_of_a = count_frequencies_of(word_a)

    frequencies_of_b = count_frequencies_of(word_b)

    return frequencies_of_a == frequencies_of_b


# Checking with examples
if __name__ == "__main__":
    for key in words:
        print(
            'Is the word "{0}" is anagram of "{1}"? {2}'.format(
                key, words[key], is_anagram(key, words[key]))
        )
