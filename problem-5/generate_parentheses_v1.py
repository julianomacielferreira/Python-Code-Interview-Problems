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
    """
    Checks if a combination of parentheses is valid.

    Args:
       combination (str): The combination of parentheses to check.

    Returns:
       bool: True if the combination is valid, False otherwise.
    """
    # Initialize the counter for open parentheses
    diff = 0  # Counter for open parentheses
    # Iterate over each parenthesis in the combination
    for pair in combination:
        # Check if the parenthesis is open
        if pair == '(':  # Check for open parenthesis
            # Increment the counter for open parentheses
            diff += 1  # Increment counter
        # If it's not an open parenthesis, it's a close parenthesis
        else:  # Close parenthesis
            # Check if there are open parentheses to close
            if diff == 0:  # No open parentheses to close
                # Return False if there are no open parentheses to close
                return False  # Invalid combination
            # If there are open parentheses to close
            else:  # Open parentheses to close
                # Decrement the counter for open parentheses
                diff -= 1
    # Check if the stack is empty at the end
    # Return True if the combination is valid and False otherwise
    return diff == 0


def generate(n):
    """
    Generates all possible combinations of well-formed parentheses.

    Args:
        n (int): The number of pairs of parentheses.

    Returns:
        list: A list of strings, each representing a possible combination of well-formed pairs.
    """

    def rec(n, diff, comb, combs):
        """
        Recursive helper function to generate combinations of well-formed parentheses.

        Args:
            n (int): The remaining number of parentheses to add.
            diff (int): The difference between the number of open and close parentheses.
            comb (list): The current combination of parentheses.
            combs (list): The list of all generated combinations.
        """
        # If the difference between open and close parentheses is negative, it's not a valid combination
        if diff < 0:
            return  # Stop exploring this branch
        # If there are no more parentheses to add
        elif n == 0:
            # If the difference between open and close parentheses is zero, it's a valid combination
            if diff == 0:
                # Add the current combination to the list of all generated combinations
                combs.append(''.join(comb))
        else:
            # Add an open parenthesis to the current combination
            comb.append('(')
            # Recursively call the function with one less parenthesis to add and increment the difference
            rec(n - 1, diff + 1, comb, combs)
            # Remove the last added parenthesis (backtracking)
            comb.pop()
            # Add a close parenthesis to the current combination
            comb.append(')')
            # Recursively call the function with one less parenthesis to add and decrement the difference
            rec(n - 1, diff - 1, comb, combs)
            # Remove the last added parenthesis (backtracking)
            comb.pop()

    # Initialize an empty list to store all generated combinations
    combs = []
    # Call the recursive function with the initial parameters
    rec(2 * n, 0, [], combs)

    # Return the list of all generated combinations
    return combs


if __name__ == "__main__":
    n = 3
    result = generate(n)
    print(result)
