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


def gas_station(gas, cost):
    """
    Finds the starting gas station for a circular route.

    Args:
        gas (list): The amount of gas at each station.
        cost (list): The cost of gas to travel from each station to the next.

    Returns:
        int: The index of the starting station, or -1 if it's not possible.
    """
    remaining = 0  # Remaining gas after traveling through stations
    prev_remaining = 0  # Previous remaining gas
    candidate = 0  # Potential starting station
    # Loop through each station
    for i in range(len(gas)):
        # Calculate the remaining gas after traveling through the current station
        remaining += gas[i] - cost[i]  # Update remaining gas

        # If the remaining gas is negative, update the candidate starting station
        if remaining < 0:  # Not enough gas to reach the next station
            # Update the candidate starting station to the next station
            candidate = i + 1
            # Previous remaining gas before the candidate starting station
            prev_remaining += remaining
            # Reset the remaining gas
            remaining = 0

    # Check if it's possible to traverse the route starting from the candidate station
    # Return -1 if it's not possible
    if candidate == len(gas) or (remaining + prev_remaining) < 0:
        return -1  # Can't traverse the route
    else:
        # Return the candidate starting station
        return candidate


if __name__ == "__main__":
    result = gas_station(gas, cost)
    assert (result != -1)
    assert (result == 8)
