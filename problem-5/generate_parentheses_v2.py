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


def generate_parenthesis(n):
    """
    Generates all possible combinations of well-formed parentheses.

    Args:
        n (int): The number of pairs of parentheses.

    Returns:
        list: A list of strings, each representing a possible combination of well-formed parentheses.
    """

    def backtrack(open_count, close_count, current_combination):
        # If the current combination has the correct number of parentheses, add it to the results list.
        if len(current_combination) == 2 * n:
            result.append("".join(current_combination))
            return

        # If the number of open parentheses is less than n, add an open parenthesis to the current combination
        if open_count < n:
            current_combination.append("(")
            backtrack(open_count + 1, close_count, current_combination)
            current_combination.pop()

        # If the number of closed parentheses is less than the number of open parentheses, add a closed parenthesis to the current combination.
        if close_count < open_count:
            current_combination.append(")")
            backtrack(open_count, close_count + 1, current_combination)
            current_combination.pop()

    result = []
    backtrack(0, 0, [])
    return result


if __name__ == "__main__":
    n = 3
    result = generate_parenthesis(n)
    print(result)
