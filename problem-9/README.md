## Minimum window substring

Given two strings ``s`` and ``t``, find the shortest substring of ``s`` that contains all characters of ``t``.

![](../static/minimum-window-substring.png)

For example, with the input:

**s** = "ADCFEBECEABEBADFCDFCBFCBEAD"

**t** = "ABCA"

And the output:

**output**: "CEABEBA"

#### Explanation:

"ADCFEBE<u>CEABEBA</u>DFCDFCBFCBEAD"

**CEABEBA** is the shortest substring of ``s`` that contains all characters of ``t`` (2 'A's, 1 'B', 1 'C')

#### Example use cases

1. Text Search: Can be used in text substring search applications to find the smallest substring of a document tha contains all the search terms.
2. Data Compression: Can be used in data compression applications to find the smallest substring of a string that contains all the required characters.