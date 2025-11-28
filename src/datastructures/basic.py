from abc import ABC, abstractmethod
from typing import Any

class List(ABC):
    """Base class for implementations of abstract data type List.
    
    These implementations involve:
        - array implementation,
        - pointer implementation,
        - cursor implementation.
    """
    @abstractmethod
    def end(self) -> int:
        """Return the position following n in an n-element list."""

    @abstractmethod
    def insert(self, x: Any, p: int) -> None:
        """Insert x at position p in list."""

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
    
#    @abstractmethod
#    def makenull(self):
#        """Make list empty and return end(L)."""
#
#    @abstractmethod
#    def first(self):
#        """Return the first position."""
#
#    @abstractmethod
#    def printlist(self):
#        """Print the elements of L in the order of occurrence."""


class Array(List):

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
        #elif elements is not None and last is not None and maxlength is not None:
            assert (elements is not None
                    and last is not None
                    and maxlength is not None)
            if -2 < last < len(elements):
                self.last = last
            else:
                raise ValueError(f"`last` cannot exceed {len(elements)-1}, " \
                                 f"but {last=} supplied.")
            if maxlength < 0:
                raise ValueError("`maxlength` must be nonnegative, " \
                                 f"but {maxlength=} supplied.")
            else:
                self.maxlength = maxlength
            if len(elements) >= maxlength:
                self.elements = elements
            else:
                self.elements = (elements
                    + [i for i in range(maxlength-len(elements))])
    
    def end(self) -> int:
        """Return last + 1."""
        return self.last + 1
    
    def insert(self, x: Any, p: int) -> None:
        """Insert x at position p."""
        if p > self.last + 1 or p < 0:
            raise IndexError(f"Position {p=} is out of range.")
        else:
            for q in range(self.last, p-1, -1): # !!!Index last+1 DNE!!!
                self.elements[q+1] = self.elements[q]
    
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