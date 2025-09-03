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
from course_schedule_v3 import dfs


class DFSTestCase(unittest.TestCase):
    def test_acyclic_graph(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['D'],
            'C': ['D'],
            'D': [],
        }

        path = []
        order = []
        visited = set()

        self.assertTrue(dfs(graph, 'A', path, order, visited))

    def test_cyclic_graph(self):
        graph = {
            'A': ['B'],
            'B': ['C'],
            'C': ['A']
        }

        path = []
        order = []
        visited = set()

        self.assertFalse(dfs(graph, 'A', path, order, visited))

    def test_invalid_graph_type(self):
        graph = "invalid"

        path = []
        order = []
        visited = set()

        with self.assertRaises(TypeError):
            dfs(graph, 'A', path, order, visited)

    def test_invalid_path_type(self):
        graph = {
            'A': ['B']
        }

        path = 'invalid'
        order = []
        visited = set()

        with self.assertRaises(TypeError):
            dfs(graph, 'A', path, order, visited)


if __name__ == '__main__':
    unittest.main()
