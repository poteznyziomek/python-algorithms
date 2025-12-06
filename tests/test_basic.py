import unittest
import copy
import itertools
import datastructures.basic as basic

class ListDataStructure(unittest.TestCase):
    def setUp(self):
        self.k: int = 10
    
    def test_array_creation(self):
        """Invalid array creation should raise exception.
        
        The `elements` parameter should be a Sequence type to allow
        for calling `len` and accessing elements through indices in the
        array methods.
        """
        elements = [0, 5, 7, 7, 2, 1, 5, 6, 6, 4, 9, 0, 1, 5, 3, 2]
        k = self.k

        # No parameters supplied.
        # elements default to the empty list, last defaults to -1,
        # maxlength defaults to 0
        self.assertIsInstance(basic.Array(), basic.Array)
        self.assertSequenceEqual(basic.Array().elements, list())
        self.assertEqual(basic.Array().last, -1)
        self.assertEqual(basic.Array().maxlength, 0)

        # One parameter supplied.
        # elements supplied
        # last defaults to len(elements)-1,
        # maxlength defaults to len(elements)
        elements=[2, 6, 8, 5, 4, 5, 2, 0]
        self.assertSequenceEqual(basic.Array(elements=elements).elements,
                             elements)
        self.assertEqual(basic.Array(elements=elements).last, len(elements)-1)
        self.assertEqual(basic.Array(elements=elements).maxlength,
                         len(elements))

        # last supplied
        # last must be negative, otherwise ValueError is raised
        # elements default to [], maxlength defaults to len([]) which is
        # 0.
        # Remark: negative last is changed to -1.
        for i in range(-10,11):
            if i < 0:
                self.assertIsInstance(basic.Array(last=i), basic.Array)
                self.assertSequenceEqual(basic.Array(last=i).elements, list())
                self.assertEqual(basic.Array(last=i).last, -1)
                self.assertEqual(basic.Array(last=i).maxlength, 0)
            else:
                self.assertRaises(ValueError, basic.Array, last=i)
        
        # maxlength supplied
        # elements default to a list with maxlength amount of elements
        # last defaults to -1
        for i in range(10):
            self.assertEqual(len(basic.Array(maxlength=i).elements), i)
            self.assertEqual(basic.Array(maxlength=i).last, -1)


        # Two parameters supplied.
        # elements and last
        # If empty elements are supplied, then last must be negative and
        # maxlength defaults to 0.
        # If nonempty elements and last are supplied, then maxlength
        # defaults to len(elements). Note that last may be less than
        # len(elements) - 1 (maxlength still defaults to len(elements)).
        # If last exceeds len(elements) - 1, then it defaults to this
        # value.
        for i in range(-10, 11):
            if i < 0:
                self.assertSequenceEqual(
                    basic.Array(elements=list(), last=i).elements,
                    list())
                self.assertEqual(basic.Array(elements=list(), last=i).last, -1)
                self.assertEqual(
                    basic.Array(elements=list(), last=i).maxlength,
                    0)
            else:
                self.assertRaises(ValueError, basic.Array,
                                  elements=list(), last=i)
        for i in (set(range(-k,0))
                  | set(range(0,len(elements)))
                  | set(range(len(elements),len(elements)+k))):
            if i < 0:
                self.assertSequenceEqual(
                    basic.Array(elements=elements, last=i).elements,
                    elements)
                self.assertEqual(basic.Array(elements=elements, last=i).last,
                                 -1)
                self.assertEqual(
                    basic.Array(elements=elements, last=i).maxlength,
                    len(elements))
            elif 0 <= i < len(elements):
                self.assertSequenceEqual(
                    basic.Array(elements=elements, last=i).elements,
                    elements)
                self.assertEqual(
                    basic.Array(elements=elements, last=i).last,
                    i)
                self.assertEqual(
                    basic.Array(elements=elements, last=i).maxlength,
                    len(elements))
            else:
                self.assertSequenceEqual(
                    basic.Array(elements=elements, last=i).elements,
                    elements)
                self.assertEqual(
                    basic.Array(elements=elements, last=i).last,
                    len(elements)-1)
                self.assertEqual(
                    basic.Array(elements=elements, last=i).maxlength,
                    len(elements))

        
        # elements, maxlength
        # maxlength must be nonnegative
        # len(elements) may be less or bigger than maxlength
        # if len(elements) < maxlength, then elements must be extended,
        # so that len(elements_extended) = maxlength
        # last defaults to min(len(elements)-1, maxlength-1)
        for i in range(-k,0):
            self.assertRaises(ValueError, basic.Array,
                              elements=elements, maxlength=i)
        for i in (set(range(len(elements)))
                  | set(range(len(elements),len(elements)+k))):
            if i <= len(elements):
                self.assertSequenceEqual(
                    basic.Array(elements=elements, maxlength=i).elements,
                    elements)
            else:
                self.assertEqual(
                    len(basic.Array(elements=elements, maxlength=i).elements),
                    i
                )
            self.assertEqual(
                basic.Array(elements=elements, maxlength=i).last,
                min(len(elements)-1, i-1))
            self.assertEqual(
                basic.Array(elements=elements, maxlength=i).maxlength,
                i)

        # last, maxlength
        # As mentioned above if elements is omitted, last must be -1.
        # last must be negative, maxlength must be nonnegative
        for i,j in itertools.product(range(-k,k+1),repeat=2):
            if i < 0 and j >= 0:
                self.assertEqual(
                    len(basic.Array(last=i, maxlength=j).elements),
                    j
                )
                self.assertEqual(
                    basic.Array(last=i, maxlength=j).last,
                    -1
                )
                self.assertEqual(
                    basic.Array(last=i, maxlength=j).maxlength,
                    j
                )
            else:
                self.assertRaises(
                    ValueError, basic.Array,
                    last=i, maxlength=j
                )

        # Three arguments supplied
        # elements, last, maxlength
        # If elements is [] then the above rules apply as if it was
        # omitted.
        # If elements is nonempty, then last can be any integer bigger
        # than -2 and smaller than len(elements), maxlength is any
        # nonnegative integer.
        for i,j in itertools.product(range(-k,k+1),repeat=2):
            if i < 0 and j >= 0:
                self.assertEqual(
                    len(
                        basic.Array(elements=[], last=i, maxlength=j).elements
                    ),
                    j
                )
                self.assertEqual(
                    basic.Array(elements=[], last=i, maxlength=j).last,
                    -1
                )
                self.assertEqual(
                    basic.Array(elements=[], last=i, maxlength=j).maxlength,
                    j
                )
            else:
                self.assertRaises(
                    ValueError, basic.Array,
                    elements=[], last=i, maxlength=j
                )
        for i,j in itertools.product(range(-k,len(elements)+k),repeat=2):
            if -2 < i < len(elements) and 0 <= j <= len(elements):
                self.assertEqual(
                    len(
                        basic.Array(
                            elements=elements, last=i, maxlength=j
                        ).elements
                    ),
                    len(elements) #j
                )
                self.assertEqual(
                    basic.Array(elements=elements, last=i, maxlength=j).last,
                    i
                )
                self.assertEqual(
                    basic.Array(
                        elements=elements, last=i, maxlength=j
                    ).maxlength,
                    j
                )
            elif -2 < i < len(elements) and len(elements) < j:
                self.assertEqual(
                    len(
                        basic.Array(
                            elements=elements, last=i, maxlength=j
                        ).elements
                    ),
                    j
                )
                self.assertEqual(
                    basic.Array(elements=elements, last=i, maxlength=j).last,
                    i
                )
                self.assertEqual(
                    basic.Array(
                        elements=elements, last=i, maxlength=j
                    ).maxlength,
                    j
                )
            elif i >= len(elements) and 0 <= j <= len(elements):
                self.assertEqual(
                    len(
                        basic.Array(
                            elements=elements, last=i, maxlength=j
                        ).elements
                    ),
                    len(elements)
                )
                self.assertEqual(
                    basic.Array(elements=elements, last=i, maxlength=j).last,
                    len(elements)-1
                )
                self.assertEqual(
                    basic.Array(
                        elements=elements, last=i, maxlength=j
                    ).maxlength,
                    j
                )
            elif i >= len(elements) and j > len(elements):
                self.assertEqual(
                    len(
                        basic.Array(
                            elements=elements, last=i, maxlength=j
                        ).elements
                    ),
                    j
                )
                self.assertEqual(
                    basic.Array(elements=elements, last=i, maxlength=j).last,
                    len(elements)-1
                )
                self.assertEqual(
                    basic.Array(
                        elements=elements, last=i, maxlength=j
                    ).maxlength,
                    j
                )
            elif i <= -2 and 0 <= j <= len(elements):
                self.assertEqual(
                    len(
                        basic.Array(
                            elements=elements, last=i, maxlength=j
                        ).elements
                    ),
                    len(elements)
                )
                self.assertEqual(
                    basic.Array(elements=elements, last=i, maxlength=j).last,
                    -1
                )
                self.assertEqual(
                    basic.Array(
                        elements=elements, last=i, maxlength=j
                    ).maxlength,
                    j
                )
            elif i <= -2 and j > len(elements):
                self.assertEqual(
                    len(
                        basic.Array(
                            elements=elements, last=i, maxlength=j
                        ).elements
                    ),
                    j
                )
                self.assertEqual(
                    basic.Array(elements=elements, last=i, maxlength=j).last,
                    -1
                )
                self.assertEqual(
                    basic.Array(
                        elements=elements, last=i, maxlength=j
                    ).maxlength,
                    j
                )
            else:
                self.assertRaises(
                    ValueError, basic.Array,
                    elements=elements, last=i, maxlength=j
                )
        
        
        
    def test_array_end(self):
        """end should return last+1."""
        elements = [1, 6, 4, 4, 9, 3, 4, 0, 6, 6, 8, 4, 8, 2, 2, 6, 4]
        last = len(elements) - 1
        k = self.k
        # No parameters supplied.
        self.assertEqual(basic.Array().end(), 0)

        # One or two parameter supplied
        self.assertEqual(basic.Array(elements=elements).end(), last+1)
        for i in (set(range(-k,len(elements)))
                  | set(range(len(elements),len(elements)+k))):
            if i < 0:
                self.assertEqual(basic.Array(last=i).end(), 0)
            elif 0 <= i < len(elements):
                self.assertRaises(ValueError, basic.Array, last=i)
                self.assertEqual(basic.Array(elements=elements, last=i).end(),
                                 i+1)
            else: # i >= len(elements)
               self.assertEqual(basic.Array(elements=elements, last=i).end(),
                                len(elements))

        # Three parameters supplied
        for l,m in itertools.product(range(-k,len(elements)+k),
                                     range(len(elements)+k)):
            if l < 0:
                self.assertEqual(
                    basic.Array(elements=elements, last=l, maxlength=m).end(),
                    0
                )
            elif 0 <= l < len(elements) and m < len(elements):
                self.assertEqual(
                    basic.Array(elements=elements, last=l, maxlength=m).end(),
                    l+1)
            elif len(elements) <= l and m < len(elements):
                self.assertEqual(
                    basic.Array(elements=elements, last=l, maxlength=m).end(),
                    len(elements))
            elif 0 <= l < len(elements) and m >= len(elements):
                self.assertEqual(
                    basic.Array(elements=elements, last=l, maxlength=m).end(),
                    l+1
                )
            else: # 0 <= l < len(elements) and m >= len(elements)
                self.assertEqual(
                    basic.Array(elements=elements, last=l, maxlength=m).end(),
                    len(elements)
                )

    def test_array_insert(self):
        """This method should insert x at valid position p.
        
        Valid positions are 0, 1, ..., end(), where end() <= maxlength.
        Any attempt of calling this method on other positions raises
        IndexError.
        """
        elements = [
            9, 1, 5, 9, 6, 5,
            5, 9, 4, 1, 7, 7,
            2, 1, 9, 0, 1, 5,
            0, 5, 4, 6, 0, 3
        ]
        new = -9999
        k = self.k

        # Try to insert to an array of maxlength equal 0.
        for i in range(-k,k+1):
            self.assertRaises(IndexError, basic.Array().insert, x=new, p=i)

        # Try to insert at invalid positions.
        for i in range(len(elements)):
            self.assertRaises(
                IndexError,
                basic.Array(
                    elements=copy.deepcopy(elements), maxlength=i).insert,
                x=new, p=i)
        array = basic.Array(elements=elements, maxlength=len(elements)//2)
        for i in (set(range(-k,0))
                  | set(range(len(elements)//2, len(elements)//2+k))):
            self.assertRaises(IndexError, array.insert, x=new, p=i)

        # Initialize empty array of maxlength k.
        # Insert new element at the end until full.
        array = basic.Array(maxlength=k)
        for i in range(k):
            array.insert(x=new, p=i)
            self.assertEqual(array.elements[i], new)
        self.assertRaises(IndexError, array.insert, x=new, p=k)

        # Initialize empty array of maxlength k.
        # Insert new element at the beginning until full.
        array = basic.Array(maxlength=k)
        for i in range(k):
            array.insert(x=new, p=0)
            self.assertEqual(array.elements[0], new)
        self.assertRaises(IndexError, array.insert, x=new, p=0)
    
    def test_array_locate(self):
        """The locate method should return the position of x."""
        elements = [2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4, 5, 9, 0, 4, 5,
                    2, 3, 5, 3, 6, 0, 2, 8, 7, 4, 7, 1, 3, 5, 2, -999]
        sought = -999

        # x is not on the list
        k = self.k
        for i in range(-k,len(elements)+k):
            array = basic.Array(elements=[1, 2, 3, 4], last=i)
            self.assertEqual(array.locate(x=sought),
                             array.end())
        
        # x is on the list
        for x in elements:
            self.assertEqual(basic.Array(elements=elements).locate(x=x),
                             elements.index(x))
    
    def test_array_retrieve(self):
        """This method should return the element at a given position.
        
        Raises Index Error if the given position is out range.
        """
        elements = ['1', '0', '8', '2', '3', '2', '3', '2',
                    '3', '3', '7', '1', '1', '1', '3', '8']
        
        # Position p is in range.
        for i in range(len(elements)):
            self.assertEqual(basic.Array(elements=elements).retrieve(p=i),
                             elements[i])

        # Position p is out of range.
        k = self.k
        for i in (set(range(-k,0))
                  | set(range(len(elements),len(elements)+k+1))):
            self.assertRaises(IndexError,
                              basic.Array(elements=elements).retrieve, p=i)

    def test_array_delete(self):
        """The method delete should remove element at position p.
        
        The element is removed by shifting elements at positions
        p+1, p+2, ..., last to positions p, p+1, ..., last-1
        respectfully. If p is out of range, IndexError is raised.
        """
        elements = [1, 2, 0, 2, -111, 0, 5, 6, 9, -222,
                    0, 3, 1, 5, -333, 9, 5, 9, 4]
        positions = {4: -111, 9: -222, 14: -333}

        # 1. Check that element at position p, where p = 4 or 9 or 14
        # equals elements[p].
        # 2. Delete element at position p.
        # 3. Check that the corresponding value is not present.
        # 4. Check that end() + 1 == len(elements)
        # Each time start with a fresh array
        for pos,val in positions.items():
            array = basic.Array(elements=copy.deepcopy(elements))
            self.assertEqual(array.elements[pos], val)
            array.delete(p=pos)
            self.assertNotIn(val, array.elements)

        # 1. Create an Array.
        # 2. Delete all elements from the end.
        # 3. Try to delete from an empty array.
        array = basic.Array(elements=elements)
        for i in range(len(elements)-1, -1, -1):
            array.delete(p=i)
        self.assertRaises(IndexError, array.delete, p=0)

        # Try to delete elements at positions which are out of range.
        k = self.k
        for i in (set(range(-k,0))
                | set(range(len(elements),len(elements)+k+1))):
            self.assertRaises(IndexError,
                              basic.Array(elements=elements).delete, p=i)
    
    def test_array_next(self):
        """For p in range, next returns p+1."""
        elements = [1, 2, 3, 4, 5]
        
        # p in range
        for i in range(len(elements)):
            self.assertEqual(basic.Array(elements=elements).next(p=i), i+1)
        
        # p out of range
        k = self.k
        for i in set(range(-k,0)) | set(range(len(elements),len(elements)+k)):
            self.assertRaises(IndexError,
                              basic.Array(elements=elements).next,
                              p=i)
    
    def test_array_previous(self):
        """The method previous should return p-1.
        
        If p < 1 or p > end(), IndexError exception is raised.
        """
        elements = [1, 2, 3, 4, 5, 6]

        # p in range
        for i in range(1,len(elements)+1):
            self.assertEqual(basic.Array(elements=elements).previous(p=i), i-1)

        # p out of range
        k = self.k
        for i in (set(range(-k,1))
                  | set(range(len(elements)+1, len(elements)+k+1))):
            self.assertRaises(IndexError,
                              basic.Array(elements=elements).previous,
                              p=i)

    def test_array_makenull(self):
        """This method should empty the list and return end().
        
        The underlying list object is not emptied, rather the `last`
        is set to -1, which indicates the empty list.
        """
        elements = [0, 6, 2, 6, 6, 5, 7, 0, 6, 8, 6, 5, 7, 7, 5, 0, 1]
        k = self.k
        for i in range(len(elements)+k):
            array = basic.Array(elements=elements, maxlength=i)
            self.assertEqual(array.last+1, array.makenull())
            self.assertEqual(array.last, -1)
    
    def test_array_first(self):
        """This method should return the first position.
        
        If the list is empty it returns end().
        """
        # Empty.
        self.assertEqual(basic.Array(maxlength=10).first(), 0)
        # Nonempty.
        self.assertEqual(basic.Array(elements=[1], maxlength=10).first(), 0)


class SingleLinkedList(unittest.TestCase):

    def setUp(self):
        self.k: int = 1000

    def test_singly_linked_list_creation(self):
        """Test creation under different arguments.
        
        + `elements` is a sequence-type optional parameter.
        + The `head`'s value (or cargo or payload) is None. If the
        `head`'s `next` is None then the list is considered empty.
        """
        k = self.k
        self.assertIsNone(basic.SLinkedList().head.nxt) # empty list
        self.assertIsNotNone(basic.SLinkedList(elements=[1, 2, 3]).head.nxt)

        array = basic.SLinkedList(elements=range(k))
        node = array.head.nxt
        for i in range(k):
            assert node is not None
            self.assertIsNotNone(node.element)
            self.assertEqual(node.element, i)
            node = node.nxt
    
    def test_singly_linked_list_end(self):
        """This method should return a pointer to the last cell.
        
        The position, say i (0 < i <= n), is considered a pointer to
        the cell holding the pointer to the i-th element. Position 0 is
        a pointer to the head, and position end() is a pointer to the
        cell:
        [ | ] -> [a0 | ]  -> ... -> [a{i-1} | ] -> [ai | ] -> ... -> [an | .]
        ^^^^^    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        head                 list
        The second field (after the pipe `|` symbol) in the head [ | ]
        is a pointer to the cell containing the element a0, which means
        it is the position one. The second field in the cell
        [a{i-1} | ] is a pointer to the cell containing the element ai,
        which means that it is the position i. The second field in the
        cell [a{n-1} | ] (not visible in the diagram) is a pointer to
        the cell containing the element an (which is the last element
        on the list), which means it is the position end().

        In the following tests we want to get the pointer, call it i, so
        that i.nxt.element == end().nxt.element == the last element of
        the list.
        Equivalently end() is the second to last node, so we cant test
        for equality end().nxt.nxt == None (a pointer to None uniquely
        signifies the last element) and for all i (0 <= i < end()) we
        have i.nxt.nxt != None.

        For the empty list end() should return Node(None, None).

        NEVERMIND. This implementation is simply not feasible. Consider
        the following alternatives:
        1. With each cell [ai | ] associate an integer i, where
        0 <= i <= n. The `head` is associated with -1. For a list in the
        diagram above, the `end` method returns n+1.
        2. Position i is associated with the cell [a{i-1} | ] (per the
        description in the book) for i such that 0 < i <= n. The `end`
        method returns n+1 which is associated with the last cell
        [an | . ] (this does not seem right).

        We follow with the 1st implementation.
        """
        k = self.k
        #sll = basic.SLinkedList(range(k)) # (k-1)th cell points to the last
        #node = sll.head
        #for i in range(k+1):
        #    if i < k:
        #        assert node is not None
        #        self.assertIsNotNone(node.nxt)
        #    else:
        #        assert node is not None
        #        self.assertIsNone(node.nxt)
        #        self.assertEqual(node, sll.end())
        #    node = node.nxt
        
        ## If the list is empty, end() should return None.
        #self.assertEqual(basic.SLinkedList().end(), basic.Node())

        for i in range(k):
            # make an i-element list, assert that end() == i+1
            self.assertEqual(
                basic.SLinkedList(elements=range(i)).end(), i
            )
        self.assertEqual(basic.SLinkedList().end(), 0)
    
    def test_singly_linked_list_insert(self):
        """The `insert` method should insert new element at position p.
        
        If the list is empty, then the new element can only be appended
        at the end().
        Valid positions p for insertion: 0 <= p <= end().
        p = 0: [|] -> [ap | ] - > [a0 | ] -> [a1 | ] -> ... -> [an | .],
        p = 1: [|] -> [a0 | ] - > [ap | ] -> [a1 | ] -> ... -> [an | .],
        ...
        p = i: [|] -> [a0 | ]  -> ... -> [a{i-1} | ] -> [ap | ] -> [ai | ] - >  ... -> [an | .],
        ...
        p = end(): [|] -> [a0 | ] - > ... -> [an | .] -> [ap | ],
        where ap = x is the value of the new element.
        """
        elements = [
            1, 3, 1, 1, 0, 2, 8, 7, 7, 7, 1,
            4, 6, 0, 5, 9, 9, 0, 5, 2, 3
        ]
        new = -999
        k = self.k
        # 1. Put new at i (0 <= i <= len(elements)) position in a linked
        # list.
        # 2. Put new at the same position in a deep copy of elements.
        # 3. Assert that the lists are equal.
        for i in range(len(elements)+1):
            linked_list = basic.SLinkedList(elements=elements)
            elements_copy = copy.deepcopy(elements)
            linked_list.insert(x=new, p=i)
            elements_copy.insert(i, new)
            node = linked_list.head.nxt
            assert node is not None
            for j in range(len(elements_copy)):
                self.assertEqual(
                    elements_copy[j],
                    node.element
                )
                node = node.nxt
        # Inserting into the empty list is valid only for p = 0.
        for i in range(-k,k+1):
            if i == 0:
                linked_list = basic.SLinkedList()
                linked_list.insert(x=new, p=i)
                assert linked_list.head.nxt is not None
                self.assertEqual(
                    linked_list.head.nxt.element,
                    new
                )
            else:
                linked_list = basic.SLinkedList()
                self.assertRaises(
                    IndexError,
                    linked_list.insert, x=new, p=i
                )

    def test_singly_linked_list_locate(self):
        """The `locate` method should return the position of an element.
        
        If the sought element appears more than once, the position of
        the first occurence is returned.
        If the sought element is not present, end() is returned.
        """
        k = self.k
        linked_list = basic.SLinkedList(elements=range(0,-k,-1))
        for i in range(k):
            self.assertEqual(
                linked_list.locate(x=-i), i
            )
        
        # Not on a list.
        sought_elements = [-111*i for i in range(1,k)]
        linked_list = basic.SLinkedList(elements=range(k))
        linked_list_end = linked_list.end()
        for i in range(k-1):
            self.assertEqual(
                linked_list.locate(x=sought_elements[i]),
                linked_list_end
            )
        
        # Empty list.
        linked_list_empty = basic.SLinkedList()
        for i in range(-k,k):
            self.assertEqual(linked_list_empty.locate(x=i), 0)
    
    def test_singly_linked_list_retrieve(self):
        """The `retrieve` method should return the value at position p.
        
        If the position p is out of range, the IndexError should be
        raised.
        """
        k = self.k
        # In range.
        linked_list = basic.SLinkedList(elements=range(0,-k,-1))
        for i in range(k):
            self.assertEqual(
                linked_list.retrieve(p=i),
                -i
            )
        
        # Out of range.
        linked_list = basic.SLinkedList(elements=range(k))
        for i in set(range(-k,0)) | set(range(k,2*k+1)):
            self.assertRaises(
                IndexError,
                linked_list.retrieve,
                p=i
            )
        
        # Empty list.
        linked_list_empty = basic.SLinkedList()
        for i in range(-k,k+1):
            self.assertRaises(
                IndexError,
                linked_list_empty.retrieve,
                p=i
            )
    
    def test_singly_linked_list_delete(self):
        """The `delete` method should remove the element at position p.
        
        If the position p is out of range, raise IndexError.
        """
        # 1. Create a k-element list [0, 1, ..., k-1].
        # 2. Delete element at position i for i = k-1, k-2, ..., 0.
        # 3. Confirm that the list is empty.
        k = self.k
        elements = [i for i in range(k)]
        linked_list = basic.SLinkedList(elements=elements)
        for i in range(k):
            elements.pop()
            linked_list.delete(p=k-1-i)
            node, j = linked_list.head.nxt, 0
            while node is not None:
                self.assertEqual(node.element, elements[j])
                node = node.nxt
                j += 1
        self.assertEqual(linked_list.head, basic.Node(None, None))

        # Invalid positions.
        linked_list = basic.SLinkedList(elements=range(k))
        for i in set(range(-k,0)) | set(range(k, 2*k+1)):
            self.assertRaises(
                IndexError,
                linked_list.delete,
                p=i
            )
        
        # Empty list.
        linked_list_empty = basic.SLinkedList()
        for i in range(-k,k+1):
            self.assertRaises(
                IndexError,
                linked_list_empty.delete,
                p=i
            )
    
    def test_singly_linked_list_next(self):
        """The `next` method should return p+1 for a given p.
        
        Valid positions p are these such that -1 <= p <= n, where n is
        the position of the last element on the list. If p is not a
        valid position, the IndexError exception should be raised.
        """
        k = self.k
        linked_list = basic.SLinkedList(elements=range(k))
        
        # In range.
        for i in range(-1,k):
            self.assertEqual(linked_list.next(p=i), i+1)

        # Out of range.
        for i in set(range(-k,-1)) | set(range(k,2*k+1)):
            self.assertRaises(
                IndexError,
                linked_list.next,
                p=i
            )
        
        # For the empty list the only valid position is -1, which yields
        # 0.
        linked_list_empty = basic.SLinkedList()
        for i in range(-k,k+1):
            if i == -1:
                self.assertEqual(linked_list_empty.next(p=i), 0)
            else:
                self.assertRaises(IndexError, linked_list_empty.next, p=i)
    
    def test_singly_linked_list_previous(self):
        """The `previous` method returnes the p-1 for a given position p.
        
        If p is not in range, the method should raise IndexError.
        """
        k = self.k
        linked_list = basic.SLinkedList(elements=range(k))

        # In range.
        for i in range(1,k+1):
            self.assertEqual(linked_list.previous(p=i), i-1)
        
        # Out of range.
        for i in set(range(-k,1)) | set(range(k+1,2*k+3)):
            self.assertRaises(IndexError, linked_list.previous, p=i)

        # Empty list.
        linked_list_empty = basic.SLinkedList()
        for i in range(-k,k+1):
            self.assertRaises(IndexError, linked_list_empty.previous, p=i)

    def test_singly_linked_list_makenull(self):
        """The `makenull` method should make the head equal to Node().
        
        It should also return end().
        For the empty list this method should be a no-op.
        """
        k = self.k
        linked_list = basic.SLinkedList(elements=range(k))
        result = linked_list.makenull()
        self.assertEqual(linked_list.head, basic.Node())
        self.assertEqual(result, k)
    
    def test_singly_linked_list_first(self):
        """The `first` method should return 0.
        
        If the list is empty it also returns 0.
        """
        k = self.k
        linked_list = basic.SLinkedList(elements=range(k))
        self.assertEqual(linked_list.first(), 0)
        self.assertEqual(basic.SLinkedList().first(), 0)
    
    @unittest.skip("Requires capturing the stdout. Another time.")
    def test_singly_linked_list_printlist(self):
        """The `printlist` should print the elements of the list.
        
        The elements should be printed in the order of occurrence.
        """


if __name__ == "__main__":
    unittest.main(verbosity=0)