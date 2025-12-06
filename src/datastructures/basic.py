from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Any
from dataclasses import dataclass

class List(ABC):
    """Base class for implementations of abstract data type List.
    
    These implementations involve:
        - array implementation,
        - pointer implementation,
        - cursor implementation.
    """
    @abstractmethod
    def end(self) -> Any:
        """Return the position following n in an n-element list."""

    @abstractmethod
    def insert(self, x: Any, p: int) -> None:
        """Insert x at position p.

        Insert moves elements at p and following positions to the next
        higher position. If p is end(), then x is appended to the end.
        If there is no position p, then raise IndexError.
        """

    @abstractmethod
    def locate(self, x: Any) -> int:
        """Return the position of x.

        If x appears more than once, then the position of the first
        occurence is returned. If x does not appear at all, then end()
        is returned.
        """
    
    @abstractmethod
    def retrieve(self, p: int) -> Any:
        """Return the element at position p.
        
        If p is out of range, then raise IndexError.
        """
    
    @abstractmethod
    def delete(self, p: int) -> None:
        """Delete the element at position p."""
    
    @abstractmethod
    def next(self, p: int) -> int:
        """Return the position following position p.

        If p is the last position, then return end().
        Raise IndexError if p is out of range.
        """
    
    @abstractmethod
    def previous(self, p: int) -> int:
        """Return the position preceding position p.
        
        Raise IndexError if p < 1 or p > end().
        """
    
    @abstractmethod
    def makenull(self) -> int:
        """Make list empty and return end(L)."""

    @abstractmethod
    def first(self) -> int:
        """Return the first position if nonempty, else end()."""

    @abstractmethod
    def printlist(self) -> None:
        """Print the elements of L in the order of occurrence."""


@dataclass
class Array(List):
    """Array implementation of the abstract data type List."""
    elements: list[Any]
    last: int
    maxlength: int

    def __init__(self,
                 elements: list[Any] | None = None,
                 last: int | None = None,
                 maxlength: int | None = None) -> None:

        if elements is None and last is None and maxlength is None:
            self.elements = list()
            self.last = -1
            self.maxlength = 0

        elif elements is not None and last is None and maxlength is None:
            self.elements = elements
            self.last = len(elements) - 1
            self.maxlength = len(elements)
        elif elements is None and last is not None and maxlength is None:
            self.elements = list()
            if last >= 0:
                raise ValueError("When only `last` parameter is " \
                                 "supplied, then it must be " \
                                 f"negative, but {last=} given.")
            else:
                self.last = -1
            self.maxlength = 0
        elif elements is None and last is None and maxlength is not None:
            self.elements = list(range(maxlength))
            self.last = -1
            self.maxlength = maxlength

        elif elements is not None and last is not None and maxlength is None:
            # empty list supplied
            if not elements and last < 0:
                self.elements = elements
                self.last = -1
                self.maxlength = 0
            elif not elements and last >= 0:
                raise ValueError("Empty `elements` supplied but `last` >= 0")
            elif elements and last < 0:
                self.elements = elements
                self.last = -1
                self.maxlength = len(elements)
            else: # nonempty elements and nonnegative last
                self.elements = elements
                self.last = last if last < len(elements) else len(elements) - 1
                self.maxlength = len(elements)
        elif elements is not None and last is None and maxlength is not None:
            if maxlength < 0:
                raise ValueError("`maxlength` must be nonnegative, " \
                                 f"but {maxlength=} supplied.")
            else:
                self.maxlength = maxlength
            self.last = min(len(elements)-1, maxlength-1)
            if len(elements) >= maxlength:
                self.elements = elements
            else:
                self.elements = (elements
                    + [i for i in range(maxlength-len(elements))])
        elif ((elements is None or not elements)
              and last is not None and maxlength is not None):
            if last >= 0:
                raise ValueError("`elements` not supplied but `last` " \
                                 f"is nonnegative: {last=}.")
            else:
                self.last = -1
            if maxlength < 0:
                raise ValueError("`maxlength` must be nonnegative, " \
                                 f"but {maxlength=} supplied.")
            else:
                self.maxlength = maxlength
            self.elements = list(range(maxlength))

        else: # each argument is supplied
            assert (elements is not None
                    and last is not None
                    and maxlength is not None)
            if maxlength < 0:
                raise ValueError("`maxlength` must be nonnegative, " \
                                 f"but {maxlength=} supplied.")
            else:
                self.maxlength = maxlength
            if last < 0:
                self.last = -1
            elif 0 <= last < len(elements):
                self.last = last
            else:
                self.last = len(elements) - 1
            if len(elements) >= maxlength:
                self.elements = elements
            else:
                self.elements = (elements
                    + [i for i in range(maxlength-len(elements))])
    
    def end(self) -> int:
        """Return last + 1."""
        return self.last + 1
    
    def insert(self, x: Any, p: int) -> None:
        """Insert x at position p

        Insert moves elements at p and following positions to the next
        higher position. If p is end(), then x is appended to the end.
        If there is no position p, then raise IndexError.
        """
        if self.last >= self.maxlength-1:
            raise IndexError("Array is full.")
        elif p > self.last + 1 or p < 0:
            raise IndexError(f"Position {p=} is out of range.")
        else:
            for q in range(self.last, p+1, -1):
                self.elements[q+1] = self.elements[q]
            self.last += 1
            self.elements[p] = x
    
    def locate(self, x: Any) -> int:
        """Return the position of x.

        If x appears more than once, then the position of the first
        occurence is returned. If x does not appear at all, then end()
        is returned.
        """
        for q in range(self.last+1):
            if self.elements[q] == x:
                return q
        return self.last + 1

    def retrieve(self, p: int) -> Any:
        """Return the element at position p.
        
        If p is out of range, then raise IndexError.
        """
        if p < 0 or p > self.last:
            raise IndexError(f"Position {p=} is out of range.")
        return self.elements[p]

    def delete(self, p: int) -> None:
        """Delete the element at position p.
        
        Raises IndexError if p is out of range.
        """
        if p > self.last or p < 0:
            raise IndexError(f"Position {p=} is out of range.")
        else:
            self.last -= 1
            for q in range(p,self.last+1):
                self.elements[q] = self.elements[q+1]
    
    def next(self, p: int) -> int:
        """Return the position following position p.

        If p is the last position, then return end().
        Raise IndexError if p is out of range.
        """
        if p < 0 or p > self.last:
            raise IndexError
        return p + 1
    
    def previous(self, p: int) -> int:
        """Return the position preceding position p.
        
        Raise IndexError if p < 1 or p > end().
        """
        if p < 1 or p > self.end():
            raise IndexError
        return p - 1

    def makenull(self) -> int:
        """Make list empty and return end."""
        end = self.end()
        self.last = -1
        return end

    def first(self) -> int:
        """Return the first position if nonempty, else end()."""
        return 0 if self.last >= 0 else self.end()

    def printlist(self) -> None:
        """Print the elements of L in the order of occurrence."""
        print(self.elements[:self.last+1])

@dataclass
class Node:
    element: Any | None = None
    nxt: Any | None = None


@dataclass
class SLinkedList(List):
    """Pointer implementation of the abstract data type List."""
    head: Node
    def __init__(self, elements: Sequence[Any] | None = None):
        """Singly-linked list.
        
        [ | ] -> [a0 | ] -> [a1 | ] -> ... -> [an | .]
        ^^^^^    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        head                 list
        The list is made up of cells, each cell consisting of an element
        of the list and a pointer to the next cell on the list. The cell
        [ai | ] holding the element ai has a pointer (in the field
        after the pipe `|` character) to the cell holding a{i+1} for
        i = 0, 2, ..., n-1. The cell [an | .] holding an has a None
        pointer. The `head` cell [ | ] points to the cell holding a0;
        the head holds no element.
        The position i is a pointer to the cell holding the pointer to
        ai for i = 1, 2, ..., n. Position 0 is a pointer to the head,
        and position end() is a pointer to the last cell.
        """
        self.head = Node(None, None)
        if elements:
            next_node = self.head
            for element in elements:
                next_node.nxt = Node(element=element, nxt=None)
                next_node = next_node.nxt
    
    def end(self) -> int:
        """Return a pointer to the last cell."""
        #node = self.head
        #while node.nxt is not None:
        #    node = node.nxt
        #return node
        node, i = self.head, -1
        while node.nxt is not None:
            i += 1
            node = node.nxt
        return i+1
            

    def insert(self, x: Any, p: int) -> None:
        """Insert x at position p.

        Insert moves elements at p and following positions to the next
        higher position. If p is end(), then x is appended to the end.
        If there is no position p, then raise IndexError.
        """
        if 0 <= p <= self.end():
            node, i = self.head, 0
            while i < p:
                assert node is not None
                node = node.nxt
                i += 1
            assert node is not None
            temp = node
            node.nxt = Node(element=x, nxt=temp.nxt)
        else:
            raise IndexError("Position out of range.")

    def locate(self, x: Any) -> int:
        """Return the position of x.

        If x appears more than once, then the position of the first
        occurence is returned. If x does not appear at all, then end()
        is returned.
        """
        node, i = self.head, -1
        #while node.nxt is not None:
        while node is not None:
            if node.element == x:
                return i
            i += 1
            node = node.nxt
        return i

    
    def retrieve(self, p: int) -> Any:
        """Return the element at position p.
        
        If p is out of range, then raise IndexError.
        """
        node, i = self.head.nxt, 0
        while node is not None:
            if i == p:
                return node.element
            i += 1
            node = node.nxt
        raise IndexError("Position is out of range.")

    
    def delete(self, p: int) -> None:
        """Delete the element at position p.
        
        If p is invalid position, raise IndexError.
        """
        i = 0
        previous_node = self.head
        current_node = previous_node.nxt
        while current_node is not None:
            assert previous_node is not None
            if i == p:
                previous_node.nxt = current_node.nxt
                return
            i += 1
            previous_node = previous_node.nxt
            current_node = current_node.nxt
        raise IndexError("Position out of range.")
    
    def next(self, p: int) -> int:
        """Return the position following position p.

        If p is the last position, then return end().
        Raise IndexError if p is out of range.
        """
        node, i = self.head, -1
        while node is not None:
            if i == p:
                return i + 1
            i += 1
            node = node.nxt
        raise IndexError("Position out of range.")
    
    def previous(self, p: int) -> int:
        """Return the position preceding position p.
        
        Raise IndexError if p < 1 or p > end().
        """
        if p < 1:
            raise IndexError
        else:
            i = -1
            node = self.head
        while node is not None:
            i += 1
            node = node.nxt
            if i == p:
                return i - 1
        raise IndexError("Position out of range.")
    
    def makenull(self) -> int:
        """Make list empty and return end(L)."""
        end = self.end()
        self.head = Node()
        return end

    def first(self) -> int:
        """Return the first position if nonempty, else end()."""
        return 0

    def printlist(self) -> None:
        """Print the elements of L in the order of occurrence."""
        node = self.head
        if node.nxt is None:
            print("[]")
        else:
            while node is not None:
                print(node.element)
                node = node.nxt