import unittest
import copy
import itertools
import datastructures.basic as basic

class ListDataStructure(unittest.TestCase):
    def setUp(self):
        self.k: int = 10
    
    def test_array_creation(self):
        """Invalid array creation should raise exception."""
        elements = [0, 5, 7, 7, 2, 1, 5, 6, 6, 4, 9, 0, 1, 5, 3, 2]
        k = self.k

        # No parameters supplied.
        # elements default to the empty list, last defaults to -1,
        # maxlength defaults to 0
        self.assertIsInstance(basic.Array(), basic.Array)
        self.assertListEqual(basic.Array().elements, list())
        self.assertEqual(basic.Array().last, -1)
        self.assertEqual(basic.Array().maxlength, 0)

        # One parameter supplied.
        # elements supplied
        # last defaults to len(elements)-1,
        # maxlength defaults to len(elements)
        elements=[2, 6, 8, 5, 4, 5, 2, 0]
        self.assertListEqual(basic.Array(elements=elements).elements,
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
                self.assertListEqual(basic.Array(last=i).elements, list())
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
                self.assertListEqual(
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
                self.assertListEqual(
                    basic.Array(elements=elements, last=i).elements,
                    elements)
                self.assertEqual(basic.Array(elements=elements, last=i).last,
                                 -1)
                self.assertEqual(
                    basic.Array(elements=elements, last=i).maxlength,
                    len(elements))
            elif 0 <= i < len(elements):
                self.assertListEqual(
                    basic.Array(elements=elements, last=i).elements,
                    elements)
                self.assertEqual(
                    basic.Array(elements=elements, last=i).last,
                    i)
                self.assertEqual(
                    basic.Array(elements=elements, last=i).maxlength,
                    len(elements))
            else:
                self.assertListEqual(
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
                self.assertListEqual(
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

if __name__ == "__main__":
    unittest.main(verbosity=0)