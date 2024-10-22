#!/usr/bin/python3
"""Module that defines a Node and a SinglyLinkedList class."""


class Node:
    """A class that defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a Node with data and an optional next_node.

        Args:
            data (int): The data stored in the node.

        Raises:
            TypeError: If data is not an integer or next_node is not a Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node.

        Args:
            value (int): The new data value.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value  # Private instance attribute

    @property
    def next_node(self):
        """Retrieve the next node.

        Returns:
            Node: The next node or None.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node.

        Args:
            value (Node or None): The new next node.

        Raises:
            TypeError: If value is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value  # Private instance attribute


class SinglyLinkedList:
    """A class that defines a singly linked list."""

    def __init__(self):
        """Initialize the singly linked list with head set to None."""
        self.__head = None  # Private instance attribute

    def __str__(self):
        """Print the entire list.

        Returns:
            str: A string representation of the linked list.
        """
        node = self.__head
        values = []
        while node:
            values.append(str(node.data))
            node = node.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list.

        Args:
            value (int): The data value to insert.
        """
        new_node = Node(value)
        if not self.__head or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
