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
import unittest
from course_schedule_v2 import Graph


class GraphTestCase(unittest.TestCase):
    """
    These tests cover the following cases:

    - Graph initialization
    - Adding edges
    - Topological sorting on an acyclic graph
    - Topological sorting on a graph with a cycle
    - Topological sorting on an empty graph
    """

    def test_init(self):
        graph = Graph()

        self.assertEqual(graph.graph, {})
        self.assertEqual(graph.in_degree, {})

    def test_add_edge(self):
        graph = Graph()
        graph.add_edge('A', 'B')

        self.assertEqual(graph.graph, {'A': ['B']})
        self.assertEqual(graph.in_degree, {'A': 0, 'B': 1})

    def test_topological_sort(self):
        graph = Graph()
        graph.add_edge('A', 'B')
        graph.add_edge('A', 'C')
        graph.add_edge('B', 'D')
        graph.add_edge('C', 'D')

        self.assertEqual(graph.topological_sort(), ['A', 'B', 'C', 'D'])

    def test_add_edge_multiple(self):
        graph = Graph()
        graph.add_edge('A', 'B')
        graph.add_edge('A', 'C')
        graph.add_edge('B', 'D')

        self.assertEqual(graph.graph, {'A': ['B', 'C'], 'B': ['D']})
        self.assertEqual(graph.in_degree, {'A': 0, 'B': 1, 'C': 1, 'D': 1})

    def test_topological_sort_cycle(self):
        graph = Graph()
        graph.add_edge('A', 'B')
        graph.add_edge('A', 'C')
        graph.add_edge('C', 'A')

        with self.assertRaises(ValueError):
            graph.topological_sort()

    def test_topological_sort_empty_graph(self):
        graph = Graph()

        self.assertEqual(graph.topological_sort(), [])


if __name__ == '__main__':
    unittest.main()
