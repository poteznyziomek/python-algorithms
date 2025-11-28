import unittest
import copy
import itertools
import datastructures.basic as basic

class ListDataStructure(unittest.TestCase):
    
    def test_array_creation(self):
        """Invalid array creation should raise exception."""
        elements = [0, 5, 7, 7, 2, 1, 5, 6, 6, 4, 9, 0, 1, 5, 3, 2]
        k = 10

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
        for i,j in itertools.product(
                set(range(-k,len(elements)))
                | set(range(len(elements),len(elements)+k)),
                repeat=2
                ):
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
            else:
                self.assertRaises(
                    ValueError, basic.Array,
                    elements=elements, last=i, maxlength=j
                )
        
        
        
    def test_array_end(self):
        """end should return last+1."""
        elements = [1, 6, 4, 4, 9, 3, 4, 0, 6, 6, 8, 4, 8, 2, 2, 6, 4]
        last = len(elements) - 1
        # No parameters supplied.
        self.assertEqual(basic.Array().end(), 0)

        # One parameter supplied
        self.assertEqual(basic.Array(elements=elements).end(), last+1)
        self.assertEqual(basic.Array(last=-1).end(), 0)

        # Both parameters supplied
        for i in range(len(elements)):
            self.assertEqual(basic.Array(elements=elements,last=i).end(),
                             i+1)

    @unittest.skip("Problem with max length of elements.")
    def test_array_insert(self):
        """insert should insert x at valid position p.
        """
        elements = [
            9, 1, 5, 9, 6, 5,
            5, 9, 4, 1, 7, 7,
            2, 1, 9, 0, 1, 5,
            0, 5, 4, 6, 0, 3
        ]
        new = -9999
        array = basic.Array(elements=elements)

        # use .retrieve and .delete

        # For i, 0 <= i <= last:
        # 1. Insert x at position i.
        # 2. Check if x is at position i (must be true).
        # 3. Delete element at position i which is x.
        # 4. Confirm element at position i is not x.
        for i in range(array.end()):
            array.insert(x=new, p=i)
            self.assertEqual(array.retrieve(i), new)
            array.delete(p=i)
            self.assertNotEqual(array.retrieve(p=i), new)


        # Insert x at position .end().
        # Confirm x is at position last.
        # Delete element at position last.
        # Confirm that element at position last is not x.
        array.insert(x=new, p=array.end())
        self.assertEqual(array.retrieve(array.end()-1), new)
        array.delete(p=array.end()-1)
        self.assertNotEqual(array.retrieve(array.end()-1), new)

        # For i, -k <= i <= -1 or .end() + 1 <= i <= .end() + 1 + k, where k is
        # some positive integer:
        # Assert that an exception is raised (index out of range).
        k = 10
        for i in set(range(-k,0)) | set(range(array.end()+1,array.end()+2+k)):
            self.assertRaises(IndexError, array.insert, x=new, p=i)
    
    def test_array_locate(self):
        """The locate method should return the position of x."""
        elements = [2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4, 5, 9, 0, 4, 5,
                    2, 3, 5, 3, 6, 0, 2, 8, 7, 4, 7, 1, 3, 5, 2, -999]
        sought = -999

        # x is not on the list
        self.assertEqual(basic.Array(elements=[1, 2, 3, 4]).locate(x=sought),
                         len([1, 2, 3, 4]))
        
        # x is on the list
        for x in elements:
            self.assertEqual(basic.Array(elements=elements).locate(x=x),
                             elements.index(x))
    
    def test_array_retrieve(self):
        """This method should return the element at a given position."""
        elements = ['1', '0', '8', '2', '3', '2', '3', '2',
                    '3', '3', '7', '1', '1', '1', '3', '8']
        
        # Position p is in range.
        for i in range(len(elements)):
            self.assertEqual(basic.Array(elements=elements).retrieve(p=i),
                             elements[i])

        # Position p is out of range.
        k = 10
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
            self.assertEqual(array.retrieve(p=pos), val)
            array.delete(p=pos)
            self.assertEqual(array.locate(x=val), array.end())
            self.assertEqual(array.end()+1, len(elements))

        # 1. Create an Array.
        # 2. Delete all elements from the end.
        # 3. Try to delete from an empty array.
        array = basic.Array(elements=elements)
        for i in range(len(elements)-1, -1, -1):
            array.delete(p=i)
        self.assertRaises(IndexError, array.delete, p=0)

        # Try to delete elements at positions which are out of range.
        k = 10
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
        k = 10
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
        k = 10
        for i in (set(range(-k,1))
                  | set(range(len(elements)+1, len(elements)+k+1))):
            self.assertRaises(IndexError,
                              basic.Array(elements=elements).previous,
                              p=i)


if __name__ == "__main__":
    unittest.main(verbosity=0)