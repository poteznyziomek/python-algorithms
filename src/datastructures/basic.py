"""

``datastructures.basic``
========================

The basic data structures include ``Array`` and ``SLinkedList`` (singly-
linked list), which are implementations of the ``List`` abstract data
type.
"""
from abc import ABC, abstractmethod
from collections.abc import Sequence, MutableSequence
from typing import Any
from dataclasses import dataclass


class List(ABC):
    """Base class for implementations of abstract data type List.

    These implementations involve:
        - array implementation,
        - pointer implementation.
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
    """Array implementation of the abstract data type List.

    Useful when:
    + the number of elements is known not to exceed a certain
    value throughout the execution of the program,
    + the `previous` or `end` methods are to be frequently used.
    Other implementations should be considered if:
    + the bound on the number of elements cannot be established,
    + the `insert` and `delete` methods are to be frequently used.

    Parameters
    ----------
    elements : MutableSequence[Any] or None, default None
        The values which initially should populate the array.
    last : int or None, default None
        The position of the last element in the array.
    maxlength : int or None, default None
        The upper bound on the number of elements. If it is None, then
        this value is inferred based on the `elements` and `last`.

    Raises
    ------
    ValueError
        When `last` is the only parameter given, but is not negative.
        When empty `elements` given, but `last` >= 0.
        When `maxlength` is negative.
        When `elements` not given but `last` is nonnegative.
    IndexError
        When methods are called with inappropriate values.

    Notes
    -----
    As already mentioned in the description, this data structure may be
    favorable if frqeuent calls to `previous` and `end` methods are to
    be made. Executing these methods requires constant time according to
    their implementation. On the other hand `insert` and `delete`
    require movement of elements, which is not constant in time, in
    which case other implementations may be preferable.
    This implementation is based on [1]_.

    References
    ----------
    .. [1] Alfred V. Aho, John E. Hopcroft, Jeffrey D. Ullman, "Data
    structures and algorithms", Addison-Wesley, 1983.
    """
    elements: MutableSequence[Any]
    last: int
    maxlength: int

    def __init__(self,
                 elements: MutableSequence[Any] | None = None,
                 last: int | None = None,
                 maxlength: int | None = None) -> None:

        if elements is None and last is None and maxlength is None:
            self.elements = []
            self.last = -1
            self.maxlength = 0

        elif elements is not None and last is None and maxlength is None:
            self.elements = elements
            self.last = len(elements) - 1
            self.maxlength = len(elements)
        elif elements is None and last is not None and maxlength is None:
            self.elements = []
            if last >= 0:
                raise ValueError("When only `last` parameter is "
                                 "supplied, then it must be "
                                 f"negative, but {last=} given.")
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
            else:  # nonempty elements and nonnegative last
                self.elements = elements
                self.last = last if last < len(elements) else len(elements) - 1
                self.maxlength = len(elements)
        elif elements is not None and last is None and maxlength is not None:
            if maxlength < 0:
                raise ValueError("`maxlength` must be nonnegative, "
                                 f"but {maxlength=} supplied.")
            self.maxlength = maxlength
            self.last = min(len(elements)-1, maxlength-1)
            if len(elements) >= maxlength:
                self.elements = elements
            else:
                self.elements = (list(elements)
                                 + list(range(maxlength-len(elements))))
        elif ((elements is None or not elements)
              and last is not None and maxlength is not None):
            if last >= 0:
                raise ValueError("`elements` not supplied but `last` "
                                 f"is nonnegative: {last=}.")
            self.last = -1
            if maxlength < 0:
                raise ValueError("`maxlength` must be nonnegative, "
                                 f"but {maxlength=} supplied.")
            self.maxlength = maxlength
            self.elements = list(range(maxlength))

        else:  # each argument is supplied
            assert (elements is not None
                    and last is not None
                    and maxlength is not None)
            if maxlength < 0:
                raise ValueError("`maxlength` must be nonnegative, "
                                 f"but {maxlength=} supplied.")
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
                self.elements = (list(elements)
                                 + list(range(maxlength-len(elements))))

    def end(self) -> int:
        """Return the position following the last position.

        If the last position in the array is `last`, then this method
        returns `last` + 1.

        Returns
        -------
        int
        """
        return self.last + 1

    def insert(self, x: Any, p: int) -> None:
        """Insert a given element at the specified position.

        Inserting `x` at position `p` moves the elements at further
        positions.

        Parameters
        ----------
        x : Any
            The new element to be inserted.
        p : int
            The position at which `x` is to be placed.

        Returns
        -------
        None

        Raises
        ------
        IndexError
            If the array is full, no new element can be inserted.
            If the position `p` is invalid. The position `p` must be in
            range 0 <= p <= n + 1, where n is the last index in the
            array.

        Notes
        -----
        This implementation is inspired by the array implementation
        found in [1]_. However in contrast to the book, we allow the
        type of `x` to be anything. User is advised to proceed with
        caution.

        References
        ----------
        .. [1] Alfred V. Aho, John E. Hopcroft, Jeffrey D. Ullman, "Data
        structures and algorithms", Addison-Wesley, 1983.
        """
        if self.last >= self.maxlength-1:
            raise IndexError("Array is full.")
        if p > self.last + 1 or p < 0:
            raise IndexError(f"Position {p=} is out of range.")
        for q in range(self.last, p+1, -1):
            self.elements[q+1] = self.elements[q]
        self.last += 1
        self.elements[p] = x

    def locate(self, x: Any) -> int:
        """Return the position of the given element.

        If `x` appears more than once, then the position of the first
        occurence is returned. If `x` does not appear at all, then end()
        is returned.

        Parameters
        ----------
        x : Any
            The sought element.

        Returns
        -------
        int
            The position of the first occurence of `x` or the value
            returned by the call to the end method.

        See Also
        --------
        Array.end: Returns the position following the last position.
        """
        for q in range(self.last+1):
            if self.elements[q] == x:
                return q
        return self.last + 1

    def retrieve(self, p: int) -> Any:
        """Return the element at the given position.

        Parameters
        ----------
        p : int
            The position from which an element is to be retrieved.

        Returns
        -------
        Any
            The value at `p`.

        Raises
        ------
        IndexError
            If `p` is out of range. The `p` parameter must be in range
            0 <= p <= n, where n is the last position in the array.
        """
        if p < 0 or p > self.last:
            raise IndexError(f"Position {p=} is out of range.")
        return self.elements[p]

    def delete(self, p: int) -> None:
        """Delete the element at the given position.

        Parameters
        ----------
        p : int
            The position of the element to be deleted.

        Returns
        -------
        None

        Raises
        ------
        IndexError
            If `p` is out of range. The position `p` must be in range
            0 <= p <= n, where n is the positio of the last element.
        """
        if p > self.last or p < 0:
            raise IndexError(f"Position {p=} is out of range.")
        self.last -= 1
        for q in range(p, self.last+1):
            self.elements[q] = self.elements[q+1]

    def next(self, p: int) -> int:
        """Return the position following the given position.

        For a given `p` return `p` + 1.

        Parameters
        ----------
        p : int

        Returns
        -------
        int
            If `p` is the last position, then return end(). Otherwise
            return `p` + 1.

        Raises
        ------
        IndexError
            If `p` is out of range. The parameter `p` must be in range
            0 <= p <= n, where n is the position of the last element.

        See Also
        --------
        Array.end: Returns the position following the last position.
        """
        if p < 0 or p > self.last:
            raise IndexError
        return p + 1

    def previous(self, p: int) -> int:
        """Return the position preceding the given position.

        For a given position `p` return `p` - 1.

        Parameters
        ----------
        p : int

        Returns
        -------
        int

        Raises
        ------
        IndexError
            If `p` is not a valid position. The parameter `p` must be in
            range 1 <= `p` <= n + 1, where n is the position of the last
            element in the array.
        """
        if p < 1 or p > self.end():
            raise IndexError
        return p - 1

    def makenull(self) -> int:
        """Empty the array.

        Makes the array empty and returns the value of the call to the
        end method.

        Returns
        -------
        int
            This is the value returned by end.

        See Also
        --------
        Array.end: Returns the position following the last position.

        Notes
        -----
        Under the hood the last attribute is set to -1. If last is -1 it
        indicates that the array is empty.
        """
        end = self.end()
        self.last = -1
        return end

    def first(self) -> int:
        """Return the first position.

        If empty, return end(). Either way this method always returns 0.

        Returns
        -------
        int
            The number 0 (zero).

        See Also
        --------
        Array.end: Returns the position following the last position.
        """
        return 0 if self.last >= 0 else self.end()

    def printlist(self) -> None:
        """Print the elements in the order of occurrence."""
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
