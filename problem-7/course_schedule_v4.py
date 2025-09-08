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
from collections import deque


def bfs(graph, start):
    """
    Performs a breadth-first search (BFS) traversal of the graph starting from the given node.

    Args:
        graph: A dictionary representing the graph, where each key is a node and its corresponding value
                is a list of its neighbors.
        start: The node to start the traversal from.

    Returns:
        A list of nodes in the order they were visited.
    """
    visited = set()
    queue = deque([start])
    visited_order = []

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            visited_order.append(node)

            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return visited_order


def course_schedule(n, prerequisites):
    """
    Determines a valid order of courses given the number of courses and prerequisites.

    This functions implements Khan's algorithm for topological sorting, suitable for
    directed acyclic graphs (DAGs). Detects if a valid order exists.

    Args:
        n (int): The number of courses, labeled from 0 to n-1.
        prerequisites (lists of lists): Each inner list is [course, prerequisite],
                                        indicating the course depends on the prerequisite.

    Returns:
        list: A valid ordering of courses as a topological sort if one exists,
                otherwise, an empty list indicating no valid order (cycle is detected).

    Example:
        >>> n = 4
        >>> prerequisites = [[0, 1], [1, 2], [2, 3]]
        >>> course_schedule(n, prerequisites)
        [3, 2, 1, 0] # One possible valid order
    """
    graph = [[] for _ in range(n)]
    indegree = [0] * n

    for course, pre in prerequisites:
        graph[pre].append(course)
        indegree[course] += 1

    order = []
    queue = deque([i for i in range(n) if indegree[i] == 0])

    while queue:
        vertex = queue.popleft()
        order.append(vertex)

        for neighbor in graph[vertex]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # Check if all nodes were visited
    if len(order) != n:
        return []  # Cycle detected, no valid ordering

    return order
