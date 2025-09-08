## Kth Permutation

With the range of numbers from 1 to n inclusive, we can make n! permutations.
By labeling them in order starting from 1, you are asked to return the kth permutation.

![](../static/kth-permutation.png)

For example:

![](../static/kth-permutation-example.png)

A first solution not efficient for large values of n:

```python
import itertools


def kth_permutation(n, k):
    """
    Returns the k-th lexicographically ordered permutation of numbers from 1 to n.

    Args:
        n (int): The number of elements to permute (1 to n)
        k (int): The position of the permutation in lexicographic order (1-indexed)

    Returns:
        str: The k-th permutation as a string of concatenated digits.

    Raises:
        ValueError: If k is out of range (k < 1 or k > n!).

    Example:
        >>> kth_permutation(3, 2)
        '132'
    """
    permutations = list(itertools.permutations(range(1, n + 1)))

    if k < 1 or k > len(permutations):
        raise ValueError(f"k={k} out of range for n={n} (1 to {len(permutations)})")

    return ''.join(map(str, permutations[k - 1]))
```