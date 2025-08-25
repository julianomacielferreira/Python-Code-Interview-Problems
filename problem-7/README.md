## Course Schedule

Given an integer ``n`` representing the number of courses (courses are labeled from 0 to $n - 1$), and an array $prerequisites$
where $prerequisites[i] = [a, b]$ means that you first need to take the course $b$ before taking the course $a$, determine if
it's possible to finish all courses.

An impossible course schedule:

![](../static/course-schedule-impossible.png)

A possible course schedule:

![](../static/course-schedule-possible.png)

To solve this problem you must have a good idea about DFS (Depth-First Search) and Topological Sort. Let's elaborate more on that.

**Depth-First Search** is a graph traversal algorithm that explores a graph tree by visiting a node and then
visiting all of its neighbors before backtracking.

**How DFS Works**

1. Choose a starting node (also called the root node) in the graph.
2. Explore the node and mark it as visited.
3. Visit all the neighbors of the node that have not been visited.
4. Repeat steps 2 and 3 for each neighbor until all nodes have been visited.

**Types of DFS**

There are three types of DFS:

1. **Pre-order DFS:** Visit the current node before visiting its neighbors.
2. **In-order DFS:** Visit the left subtree, the current node, and then the right subtree (only applicable to binary trees).
3. **Post-order DFS:** Visit the neighbors before visiting the current node.

