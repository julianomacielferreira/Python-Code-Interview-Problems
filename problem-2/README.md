## Find First and Last Position

Given a sorted array of integers ``int_array`` and an integer target, find the index of first and last position of target in ``int_array``.

The target should appear in sequence.

If target can't be found in int_array, return [-1, -1]

Example:

```
int_array = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]

Five is at position two (int_array[2]) and appears until position six (int_array[6]), so it should returns [2, 6]
```

Some integers to validate:

```python
# Data example
int_array = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
```

A first [solution](find_first_last_position_v1.py) can be:

```python


def find_first_last_position_v1(integers_array, target):
    """
        Finds the first and last position of an integer in an ordered array

        Params:
            integers_array (array): Ordered array
            target (int): Number to find the first and last position it appears in sequence

        Returns:
            [-1, -1] if the target was not in array, otherwise returns [first_index, last_index]
    """
    is_target_in_array = False

    for i in range(len(integers_array)):
        if integers_array[i] == target:
            is_target_in_array = True
            break

    if not is_target_in_array:
        return [-1, -1]

    first_position = False
    last_position = False

    for i in range(len(integers_array)):
        if integers_array[i] == target:
            if not first_position:
                first_position = i
            else:
                last_position = i

    # Only one occurrence of target
    if not last_position:
        last_position = first_position

    return [first_position, last_position]


# Checking
if __name__ == "__main__":
    assert (find_first_last_position_v1(int_array, 10) == [-1, -1])
    assert (find_first_last_position_v1(int_array, 5) == [2, 6])
    assert (find_first_last_position_v1(int_array, 7) == [7, 7])

```

A second [solution](find_first_last_position_v2.py):

```python
def find_first_last_position_v2(integers_array, target):
    """
        Finds the first and last position of an integer in an ordered array

        Params:
            integers_array (array): Ordered array
            target (int): Number to find the first and last position it appears in sequence

        Returns:
            [-1, -1] if the target was not in array, otherwise returns [first_index, last_index]
    """
    for i in range(len(integers_array)):
        if integers_array[i] == target:
            first_position = last_position = i

            while (last_position + 1) < len(integers_array) and integers_array[(last_position + 1)] == target:
                last_position += 1

            return [first_position, last_position]

    return [-1, -1]


# Checking
if __name__ == "__main__":
    assert(find_first_last_position_v2(int_array, 10) == [-1, -1])
    assert(find_first_last_position_v2(int_array, 5) == [2, 6])
    assert(find_first_last_position_v2(int_array, 7) == [7, 7])
```

A third [solution](find_first_last_position_v3.py) using a binary search tree to find the first occurrence of the number:

```python
def binary_search_first_occurrence(array, target):
    """
        Binary search to return the first occurrence of an integer in ordered array

        Params:
            array (array): Ordered array
            target (int): Number to find its position

        Returns:
            -1 if the target was not in array, otherwise returns position
    """
    if array[0] == target:
        return 0

    left = 0
    right = len(array) - 1

    while left <= right:

        mid_index = (right + left) // 2

        prev_to_mid_element = array[mid_index - 1]
        mid_element = array[mid_index]

        if mid_element == target and prev_to_mid_element < target:
            return mid_index
        elif mid_element < target:
            left = mid_index + 1
        else:
            right = mid_index - 1

    return -1


def find_first_last_position_v3(integer_array, target):
    """
        Finds the first and last position of an integer in an ordered array

        Params:
            integer_array (array): Ordered array
            target (int): Number to find the first and last position it appears in sequence

        Returns:
            [-1, -1] if the target was not in array, otherwise returns [first_index, last_index]
    """
    if len(integer_array) == 0:
        return [-1, -1]

    first_position = binary_search_first_occurrence(integer_array, target)

    if first_position == -1:
        return [-1, -1]

    last_position = first_position

    while (last_position + 1) < len(integer_array) and integer_array[(last_position + 1)] == target:
        last_position += 1

    return [first_position, last_position]


# Checking
if __name__ == "__main__":
    assert (find_first_last_position_v3([], 10) == [-1, -1])
    assert (find_first_last_position_v3(int_array, 10) == [-1, -1])
    assert (find_first_last_position_v3(int_array, 5) == [2, 6])
    assert (find_first_last_position_v3(int_array, 7) == [7, 7])
```

A fourth [solution](find_first_last_position_v4.py) using binary tree to find the last occurrence of the integer:

```python
from find_first_last_position_v3 import binary_search_first_occurrence

def binary_search_last_occurrence(array, target):
    """
        Binary search to return the last occurrence of an integer in ordered array

        Params:
            array (array): Ordered array
            target (int): Number to find its position

        Returns:
            -1 if the target was not in array, otherwise returns position
    """
    if len(array) == 0:
        return 0

    last_index = len(array) - 1

    if array[-1] == target:
        return last_index

    left = 0
    right = last_index

    while left <= right:
        mid_index = (right + left) // 2

        mid_element = array[mid_index]
        next_to_mid_element = array[mid_index+1]

        if mid_element == target and next_to_mid_element > target:
            return mid_index
        elif mid_element > target:
            right = mid_index - 1
        else:
            left = mid_index + 1

    return -1


def find_first_last_position_v4(integer_array, target):
    """
        Finds the first and last position of an integer in an ordered array

        Params:
            integer_array (array): Ordered array
            target (int): Number to find the first and last position it appears in sequence

        Returns:
            [-1, -1] if the target was not in array, otherwise returns [first_index, last_index]
    """
    if len(integer_array) == 0 or integer_array[0] > target or integer_array[-1] < target:
        return [-1, -1]

    first_position = binary_search_first_occurrence(integer_array, target)
    last_position = binary_search_last_occurrence(integer_array, target)

    return [first_position, last_position]


# Checking
if __name__ == "__main__":
    assert(find_first_last_position_v4([], 10) == [-1, -1])
    assert(find_first_last_position_v4(int_array, 10) == [-1, -1])
    assert(find_first_last_position_v4(int_array, 5) == [2, 6])
    assert(find_first_last_position_v4(int_array, 7) == [7, 7])
```