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


def dfs(graph, vertex, path, order, visited):
    """
    Performs a depth-first search (DFS) on a graph.

    This function is a recursive helper function for topological sorting.
    It traverses the graph depth-first, adding vertices to the path and marking them as visited.
    Once a vertex has no more unvisited neighbors, it is added to the order list.

    Args:
        graph (dict): The graph represented as an adjacency list. Each key is a vertex, and its
            corresponding value is a list of its neighbors.
        vertex: The current vertex being visited.
        path (list): The current path of vertices.
        order (list): The list of vertices in topological order.
        visited (set): The set of visited vertices.

    Returns:
        bool: True if the graph is acyclic, False otherwise.

    Raises:
        TypeError: If a graph is not a dict, or if path, order, or visited are not a list or set.

    Notes:
        This function modifies the path, order, and visited parameters in-place.
    """
    if not isinstance(graph, dict):
        raise TypeError("Graph must be a dict")
    if not isinstance(path, list) or not isinstance(order, list):
        raise TypeError("Path and order must be lists")
    if not isinstance(visited, set):
        raise TypeError("Visited must be a set")

    path.append(vertex)

    for neighbor in graph.get(vertex, []):
        if neighbor in path:
            return False
        if neighbor not in visited:
            visited.add(neighbor)
            if not dfs(graph, neighbor, path, order, visited):
                return False

    order.append(path.pop())

    return True


def topological_sort(graph):
    """
    Performs a topological sort on a direct acyclic graph (DAG)

    This function uses a depth-first (DFS) approach to traverse the graph and returns a list
    of vertices in topological order. A topological order is an ordering of the vertices such that
    for every edge (u, v), vertex u comes before vertex v in the ordering.

    Args:
        graph (dict): The graph represented as an adjacency list. Each key is a vertex, and its corresponding
                        value is a list of its neighbors.

    Returns:
        list: A list of vertices in topological order. If the graph contains cycles, the result is not guaranteed to be
              a valid topological order.

    Notes:
        This function assumes that the graph is represented as a dictionary where each key is a vertex and its corresponding
        value is a list of its neighbors. The function also assumes that the graph does not contain any self-loops or
        parallel edges.

        If the graph contains a cycle, the result is not guaranteed to be a valid topological order. You may want to add
        cycle detection to the function if you need to handle cyclic graphs.

    Time Complexity:
        O(V + E), where V is the number of vertices and E is the number of Edges.

    Example:
        >>> graph = {
        ...     'A': ['B', 'C'],
        ...     'B': ['D'],
        ...     'C': ['D'],
        ...     'D': []
        ... }

        >>> topological_sort(graph)
        ['A', 'C', 'B', 'D']
    """
    visited = set()
    path = []
    order = []

    for vertex in graph:
        if vertex not in visited:
            visited.add(vertex)
            dfs(graph, vertex, path, order, visited)

    return order[::-1]


def course_schedule(n, prerequisites):
    """
    Determine if it's possible to finish all courses based on the given prerequisites.

    This function uses a depth-first search (DFS) approach to detect cycles in a graph.
    If a cycle is detected, it means that there is no valid order to finish all courses,
    and the function returns False. Otherwise, it returns True.

    Args:
        n (int): The number of courses
        prerequisites (list): A list of pairs where the first element is the course and the second element is its
                              prerequisite.

    Returns:
        bool: True if it's possible to finish all courses, False otherwise.

    Notes:
        This function assumes that the courses are numbered from 0 to n-1.

    Time complexity:
        O(n + m), where n is the number of courses and m is the number of prerequisites.

    Example:
      >>> course_schedule(2, [[1, 0]])
      True
      >>> course_schedule(2, [[1, 0], [0, 1]])
      False
    """
    graph = [[] for i in range(n)]

    for pre in prerequisites:
        graph[pre[1]].append(pre[0])

    visited = set()
    path = set()

    dfs_fn = lambda course: (
        False if course in path else
        True if course in visited else
        all(dfs(neighbor) for neighbor in graph[course]) and
        (visited.add(course) or path.add(course) or all([path.remove(course), True]))
    )

    for course in range(n):
        if course not in visited and not dfs_fn(course):
            return False
    return True
