from abc import ABC, abstractmethod
from typing import Any, Optional

class List(ABC):
    """Base class for implementations of abstract data type List.
    
    These implementations involve:
        - array implementation,
        - pointer implementation,
        - cursor implementation.
    """
    @abstractmethod
    def end(self) -> int:
        """Return the position following n in an n-element list.
        """
#
#    @abstractmethod
#    def insert(self, x: Any, p: int):
#        """Insert x at position p in list.
#        """
#
#    @abstractmethod
#    def locate(self, x: Any):
#        """Return the position of x on list.
#        """
#    
#    @abstractmethod
#    def retrieve(self, p: int):
#        """Return the element at position p.
#        """
#    
#    @abstractmethod
#    def delete(self, p: int):
#        """Delete the element at position p.
#        """
#    
#    @abstractmethod
#    def next(self, p: int):
#        """Return the position following position p.
#        """
#    
#    @abstractmethod
#    def previous(self, p: int):
#        """Return the position preceding position p.
#        """
#    
#    @abstractmethod
#    def makenull(self):
#        """Make list empty and return end(L).
#        """
#
#    @abstractmethod
#    def first(self):
#        """Return the first position.
#        """
#
#    @abstractmethod
#    def printlist(self):
#        """Print the elements of L in the order of occurrence.
#        """


class Array(List):

    def __init__(self, elements: Optional[list[Any]] = None,
                 last: Optional[int] = None) -> None:

        if elements is None:
            elements = list()
        last = len(elements)-1 if last is None else last
        if last > len(elements)-1:
            raise ValueError(
                f"Last position of elements is {len(elements)-1}, "
                f"but {last=} was given.")
        if elements and last < 0:
            raise ValueError("elements not empty but last is negative")
        if not elements and last != -1:
            raise ValueError("elements empty but last is not -1")

        self.elements: list[Any] = elements
        self.last: int = last
    
    def end(self) -> int:
        """Return last + 1.
        """
        return self.last + 1