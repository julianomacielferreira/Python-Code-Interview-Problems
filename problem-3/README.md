## k<sub>th</sub> Largest Element

Given an array of integers ``int_array`` and an integer ``k``, find the ``kth`` largest element.

``k`` is between 1 and ``len(int_array)``

Example:

```python
int_array = [4 ,2, 9, 7, 5, 6 , 7, 1, 3]

k = 4
```

Output:

- 1º largest element is 9
- 2º largest element is 7
- 3º largest element is 7
- 4º largest element is 6

Procedure:

- 1º iteration: the maximum is 9, remove it
- 2º iteration: the maximum is 7, remove it
- 3º iteration: the maximum is 7, remove it
- 4º iteration: the maximum is 6, the kth largest element

Some data to validate:

```python
# Data example
int_array = [4, 2, 9, 7, 5, 6, 7, 1, 3]
```

A first [solution](kth_largest_element_v1.py) using numpy:

```python
import numpy as np

def kth_largest_element_v1(integer_array, k):
    """
        Given an array of integers and an integer k, find the kth largest element.

        Params:
            integer_array (array): Ordered array
            k (int): Position to find the element

        Returns:
            -1 if the target was not in array, otherwise returns the element
    """
    if k <= 0 or k > len(integer_array):
        return -1

    _array_ = np.sort(np.array(integer_array))

    return _array_[-k]


if __name__ == "__main__":
    assert (kth_largest_element_v1(int_array, 4) == 6)
    assert (kth_largest_element_v1(int_array, 11) == -1)
```

A second [solution](kth_largest_element_v1.py) using numpy:

```python
import numpy as np


def kth_largest_element_v2(integer_array, k):
    """
        Given an array of integers and an integer k, find the kth largest element.

        Params:
            integer_array (array): Ordered array
            k (int): Position to find the element

        Returns:
            -1 if the target was not in array, otherwise returns the element
    """
    if k <= 0 or k > len(integer_array):
        return -1

    _array_ = np.array(integer_array)

    for i in range(k - 2):
        _array_ = np.delete(_array_, np.where(_array_ == max(_array_)))

    return max(_array_)


if __name__ == "__main__":
    assert (kth_largest_element_v2(int_array, 4) == 6)
    assert (kth_largest_element_v2(int_array, 11) == -1)
```

A third solution using a heap data structure and numpy:

```python
import numpy as np
import heapq


def kth_largest_element_v3(integer_array, k):
    """
        Given an array of integers and an integer k, find the kth largest element.

        Params:
            integer_array (array): Ordered array
            k (int): Position to find the element

        Returns:
            -1 if the target was not in array, otherwise returns the element
    """
    if k <= 0 or k > len(integer_array):
        return -1

    _array_ = np.array(integer_array)

    _array_ = [-item for item in _array_]

    heapq.heapify(_array_)

    for i in range(k - 1):
        heapq.heappop(_array_)

    return -heapq.heappop(_array_)


if __name__ == "__main__":
    assert (kth_largest_element_v3(int_array, 4) == 6)
    assert (kth_largest_element_v3(int_array, 11) == -1)
```
