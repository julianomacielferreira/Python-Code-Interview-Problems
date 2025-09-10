## Kth Permutation

With the range of numbers from 1 to n inclusive, we can make n! permutations.
By labeling them in order starting from 1, you are asked to return the kth permutation.

![](../static/kth-permutation.png)

For example:

![](../static/kth-permutation-example.png)

A first solution not efficient for large values of n, 
generating all permutations is impractical due to the factorial growth (n! permutations):

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

A more efficient solution that handles larger ``n`` efficiently compared to generating all permutations, and 
computes k-th permutation without enumerating all:

```python
def kth_permutation(n, k):
    """
    Returns the k-th lexicographically ordered permutation of numbers from 1 to n.

    Args:
        n (int): The number of elements to permute (1 to n)
        k (int): The position of the permutation in lexicographically order (1-indexed)

    Returns:
        str: The k-th permutation as a string of concatenated digits.

    Raises:
        ValueError: If k is out of range (k < 1 or k > n!).
    """
    if k < 1 or k > math.factorial(n):
        raise ValueError(f"k={k} out of range for n={n} (1 to {math.factorial(n)})")

    nums = list(range(1, n + 1))
    result = []

    k -= 1  # Adjust k to 0-indexed

    for i in range(n, 0, -1):
        fact = math.factorial(i - 1)
        index = k // fact
        k %= fact
        result.append(nums[index])
        nums.pop(index)

    return ''.join(map(str, result))
```

The operation ``index = k // fact`` is a crucial part of the algorithm that efficiently computes the k-th permutation
without needing to generate all possible permutations, which is especially important for large values of ``n``.

#### Reasons for efficiency

1. **Avoids generating all permutations:** The number of permutations of ``n`` elements in ``n!`` (factorial), which grows extremely rapidly. For ``n=20``, ``n!`` is a huge number ( $\gt$ 2 $\times$ 10<sup>18</sup>).
2. **Direct computation:** The algorithm uses properties of factorials to determine the k-th permutation directly, position by position.
3. **Complexity:** The algorithm has O(n) complexity, as it iterates ``n`` times to construct the permutation.
4. **Use of factorials:** The division of ``k // fact`` helps identify the next element in the sequence, allowing incremental construction.

#### Contrast with naive approach 

**Naive approach:** Generating all ``n!`` permutations and picking the k-th is impractical for large ``n``.
**Efficient algorithm:** Computes the permutation without enumerating all, allowing handling large ``n`` 
(mainly limited by numerical precision and memory for very large ``n``) 

#### Example of a naive approach limitation

- ``n=15``: ``15! = 1.3 x 10^12`` permutations. Generating all is infeasible.
- With the efficient algorithm, the k-th permutation is computed with operations proportional to ``n``, not ``n!``.

For example, with ``n = 4`` and ``k = 16`` (15 by starting from 0)

We have 24 permutations ($4! = 4 \times 3 \times 2 \times 1$ ) divided into 4 parts $\implies$ the length of a part is 6
($24 \div 4$)

$\lfloor{k \div length}\rfloor = \lfloor{15 \div 6}\rfloor = 2 \implies$ the kth permutation is in part 2

|        n        |      k      | 
|:---------------:|:-----------:|
|        4        |     15      |
|       n!        | part_length |
|       24        |      6      |

| unused elements |
|:---------------:|
|  [1, 2, 3, 4]   |
|   permutation   |
|        3        |