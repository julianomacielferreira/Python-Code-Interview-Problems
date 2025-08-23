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
from data import gas, cost


def can_traverse(gas, cost, start):
    """
    Checks if it's possible to traverse a circular route with given gas and cost.

    Args:
        gas (list): The amount of gas at each station.
        cost (list): The cost of gas to travel from each station to the next.
        start (int): The starting station.

    Returns:
        bool: True if it's possible to traverse the route, False otherwise.
    """
    # Get the number of stations
    n = len(gas)
    # Initialize the remaining gas
    remaining = 0
    # Initialize the current station
    i = start
    # Flag to track if we've started the journey
    started = False
    # Traverse the route
    while i != start or not started:
        started = True
        # Calculate the remaining gas after traveling from the current station to the next
        remaining += gas[i] - cost[i]
        # If the remaining gas is negative, it's not possible to traverse the route
        if remaining < 0:
            return False
        # Move to the next station
        i = (i + 1) % n
    # If we've traversed the entire route without running out of gas, return True
    return True


def gas_station(gas, cost):
    """
    Finds the starting gas station for a circular route.

    Args:
        gas (list): The amount of gas at each station.
        cost (list): The cost of gas to travel from each station to the next.

    Returns:
        int: The index of the starting station, or -1 if it's not possible.
    """
    # Iterate over each station as a potential starting point
    for i in range(len(gas)):
        # Check if it's possible to traverse the route starting from the current station
        if can_traverse(gas, cost, i):
            # Return the index of the starting station
            return i
    # If no starting station is found, return -1
    return -1


if __name__ == "__main__":
    result = gas_station(gas, cost)
    assert (result != -1)
    assert (result == 8)
