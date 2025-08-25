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
