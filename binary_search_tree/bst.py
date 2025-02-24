"""
Programming for linguists

Implementation of the data structure "Binary Search Tree"
"""

class EmptyError (Exception):
    """
    Custom Error
    """

class NoNodeError (Exception):
    """
    Custom Error
    """


class Node:
    """
    Node Data Structure
    """
    def __init__(self, element: int):
        self.element = element
        self.right = None
        self.left = None

    def first_method(self):
        """
        For working lint
        """

    def second_method(self):
        """
        For working lint
        """

class BinarySearchTree:
    """
    Structure of BinarySearchTree
    """

    def __init__(self):
        self.root = None

    def add(self, element: int, node=None):
        """
        Add the element to the tree
        """
        if self.root is None:
            self.root = Node(element)
        else:
            if self.find(element):
                raise ValueError
            if node is None:
                node = self.root
            if element < node.element:
                if node.left is None:
                    node.left = Node(element)
                else:
                    self.add(element, node.left)
            else:
                if node.right is None:
                    node.right = Node(element)
                else:
                    self.add(element, node.right)

    def remove(self, element, node=None):
        """
        Remove element from the tree
        """
        if self.root is None:
            raise EmptyError
        if self.find(element) is True:
            if node is None:
                node = self.root
            if element < node.element and node.left:
                if node.left.element == element:
                    node.left = None
                else:
                    self.remove(element, node.left)
            if element > node.element and node.right:
                if node.right.element == element:
                    node.right = None
                else:
                    self.remove(element, node.right)
        else:
            raise NoNodeError

    def find(self, element, node=None):
        """
        Find element in the tree
        """
        if self.root is None:
            raise EmptyError
        if node is None:
            node = self.root
        if node.element == element:
            return True
        if not (node.left or node.right):
            return False
        if element < node.element and node.left:
            return self.find(element, node.left)
        if element > node.element and node.right:
            return self.find(element, node.right)
        return False

    def get_height(self, node=None):
        """
        Return the height of the tree
        """
        if self.root is None:
            raise EmptyError
        if node is None:
            node = self.root
        if node.left:
            left_height = self.get_height(node.left)
        else:
            left_height = 0
        if node.right:
            right_height = self.get_height(node.right)
        else:
            right_height = 0
        return 1 + max(left_height, right_height)
