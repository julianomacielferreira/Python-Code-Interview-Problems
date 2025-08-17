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
from data import build_symmetric_btree, build_unsymmetric_btree


def are_symmetric(left_node, right_node):
    """
       Checks if a binary tree is symmetric.

       A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree.

       Args:
           left_node (TreeNode): The left node of the root of the binary tree.
           right_node (TreeNode): The right node of the root of the binary tree.

       Returns:
           bool: True if the tree is symmetric, False otherwise.
       """
    if left_node is None and right_node is None:
        return True
    elif ((left_node is None) != (right_node is None)) or left_node.value != right_node.value:
        return False
    else:
        return are_symmetric(left_node.left, right_node.right) and are_symmetric(left_node.right, right_node.left)


# Example usage
if __name__ == "__main__":
    # Root node
    symmetric_btree = build_symmetric_btree()

    assert (are_symmetric(symmetric_btree.left, symmetric_btree.right))

    # An un-symmetric binary tree

    # Root node
    un_symmetric_btree = build_unsymmetric_btree()

    assert (are_symmetric(un_symmetric_btree.left, un_symmetric_btree.right) == False)
