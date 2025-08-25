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

A code example of a DFS algorithm:

```python
class Graph:
    """
    A class representing an undirected graph using an adjacency list.

    Attributes:
        adjacency_list (dict): A dictionary where each key is a node and its corresponding value is a list of neighboring nodes.
    """

    def __init__(self):
        """
        Initialize an empty graph
        """
        self.adjacency_list = {}

    def add_edge(self, node1, node2):
        """
        Add an edge between two nodes in the graph.

        Args:
            node1 (any): The first node.
            node2 (any): The second node.

        Note:
            This method adds an edge between two nodes in both directions, making the graph undirected.
        """
        if node1 not in self.adjacency_list:
            self.adjacency_list[node1] = []
        if node2 not in self.adjacency_list:
            self.adjacency_list[node2] = []

        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    def dfs(self, start_node):
        """
        Perform a depth-first search traversal of the graph.

        Args:
            start_node (any): The node to start the traversal from.

        Returns:
            list: A list of nodes in the order they were visited.

        Raises:
            KeyError: If the start node is not in the graph.
        """
        if start_node not in self.adjacency_list:
            raise KeyError(f"Start node '{start_node}' not found in the graph")
        
        visited = set()
        traversal_order = []
        self._dfs_helper(start_node, visited, traversal_order)

        return traversal_order

    def _dfs_helper(self, node, visited, traversal_order):
        """
        A helper function to perform the depth-first search traversal.

        Args:
            node (any): The current node.
            visited (set): A set of visited nodes.
            traversal_order (list): A list to store the traversal order.
        """
        visited.add(node)
        traversal_order.append(node)

        for neighbor in self.adjacency_list[node]:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited, traversal_order)


# Example usage
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'E')
    graph.add_edge('D', 'F')

    graph_traversal_order = graph.dfs('A')
    print("DFS Traversal Order:", graph_traversal_order)
```

The output:

```bash
DFS Traversal Order: ['A', 'B', 'D', 'F', 'C', 'E']
```