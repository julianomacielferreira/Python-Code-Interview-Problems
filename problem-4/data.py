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

from tree_node import TreeNode

def build_symmetric_btree():
    # Root node
    root_node = TreeNode(4)

    # Creating left tree nodes
    root_node.left = TreeNode(5)

    root_node.left.left = TreeNode(2)
    root_node.left.left.left = TreeNode(9)

    root_node.left.left.left.left = TreeNode(3)
    root_node.left.left.left.right = TreeNode(0)

    root_node.left.left.right = TreeNode(7)
    root_node.left.left.right.right = TreeNode(6)

    root_node.left.right = TreeNode(8)
    root_node.left.right.left = TreeNode(1)

    # Creating right tree nodes
    root_node.right = TreeNode(5)
    root_node.right.left = TreeNode(8)
    root_node.right.left.right = TreeNode(1)

    root_node.right.right = TreeNode(2)
    root_node.right.right.left = TreeNode(7)
    root_node.right.right.left.left = TreeNode(6)

    root_node.right.right.right = TreeNode(9)
    root_node.right.right.right.left = TreeNode(0)
    root_node.right.right.right.right = TreeNode(3)

    return root_node


def build_unsymmetric_btree():
    # Root node
    root_node = TreeNode(4)

    # Creating left tree nodes
    root_node.left = TreeNode(5)
    root_node.left.left = TreeNode(2)
    root_node.left.right = TreeNode(7)
    root_node.left.left.left = TreeNode(9)
    root_node.left.left.right = TreeNode(7)
    root_node.left.left.left.left = TreeNode(3)
    root_node.left.left.left.right = TreeNode(0)
    root_node.left.left.right.right = TreeNode(6)

    # Creating right tree nodes
    root_node.right = TreeNode(5)
    root_node.right.left = TreeNode(8)
    root_node.right.right = TreeNode(2)
    root_node.right.left.left = TreeNode(6)
    root_node.right.left.right = TreeNode(1)
    root_node.right.right.right = TreeNode(9)
    root_node.right.right.right.left = TreeNode(0)
    root_node.right.right.right.right = TreeNode(3)

    return root_node