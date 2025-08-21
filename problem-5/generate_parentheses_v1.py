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


def is_valid(combination):
    diff = 0
    for pair in combination:
        if pair == '(':
            diff += 1
        else:
            # Not try to pop from an empty stack (otherwise it means that we found a closing parenthesis
            # without an opening one from it)
            if diff == 0:
                return False
            else:
                diff -= 1
    # Stack must be empty at the end  (otherwise it means that there's an opening parentheses that did not close)
    return diff == 0


def generate(n):
    """
    Generates all possible transfers of well-formed parents.

    Arguments:

    n (int): The number of pairs of parentheses.

    Returns:

    list: A list of strings, each representing a possible combination of well-formed pairs.
    """

    def rec(n, diff, comb, combs):
        if diff < 0:
            return
        elif n == 0:
            if diff == 0:
                combs.append(''.join(comb))
        else:
            comb.append('(')
            rec(n - 1, diff + 1, comb, combs)
            comb.pop()
            comb.append(')')
            rec(n - 1, diff - 1, comb, combs)
            comb.pop()

    combs = []
    rec(2 * n, 0, [], combs)

    return combs


if __name__ == "__main__":
    n = 3
    result = generate(n)
    print(result)
