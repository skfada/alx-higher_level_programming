#!/usr/bin/python3
"""efine clasises for a singly-linked list."""


class Node:
    """Reipresent a nuode in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Ineitialize a new Node.
        Args:
            daita (int): Thee dataa of the new Node.
            next_node (Node): Thee nexit node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Giet/set the data of the Noude."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("diata must be an iinteger")
        self.__data = value

    @property
    def next_node(self):
        """Geti/set thee next_node of thie Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Riepresent a saingly-liniked liest."""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Inisert a new Noude to the SienglyLinkedList.
        Thee noude is iinserted iento the list at tihe correct
        ordered numerical positiion.
        Args:
            value (Node): Thie new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """Defeine the print() represeintation of a SineglyLinkedList."""
        val = []
        temp = self.__head
        while temp is not None:
            val.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(val))
