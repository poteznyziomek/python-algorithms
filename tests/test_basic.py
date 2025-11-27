import unittest
import datastructures.basic as basic

class ListDataStructure(unittest.TestCase):
    
    def test_array_creation(self):
        """Invalid input should raise exception.
        """
        # No parameters supplied.
        # elements default to the empty list, last defaults to -1
        self.assertIsInstance(basic.Array(), basic.Array)


        # One parameter supplied.
        elements=[2, 6, 8, 5, 4, 5, 2, 0]
        # last defaults to len(elements)-1
        self.assertIsInstance(basic.Array(elements=elements), basic.Array)
        # If elements is ommited, then last if passed must be -1.
        for i in range(-10,11):
            if i == -1:
                self.assertIsInstance(basic.Array(last=i), basic.Array)
            else:
                self.assertRaises(ValueError, basic.Array, last=i)


        # Both parameters supplied.
        elements = [0, 5, 7, 7, 2, 1, 5, 6, 6, 4, 9, 0, 1, 5, 3, 2]
        last = len(elements)-1
        # Valid instantiation.
        self.assertIsInstance(basic.Array(elements=elements, last=last),
                              basic.Array)
        
        # If elements is nonempty, then last cannot be set to -1.
        self.assertRaises(ValueError, basic.Array,
                          elements=elements, last = -1)
        # if elements is empty, then last must be -1.
        for i in range(-10,11):
            if i == -1:
                self.assertIsInstance(basic.Array(elements=[], last=i),
                                      basic.Array)
            else:
                self.assertRaises(ValueError, basic.Array, elements=[], last=i)

        for i in range(1,20):
            # last cannot exceed the last index of elements
            self.assertRaises(ValueError, basic.Array,
                              elements=elements, last=last+i)
            # last cannot be negative if elements is nonempty
            self.assertRaises(ValueError, basic.Array,
                              elements=elements, last=-i)
        
        # Suppose elements is nonempty and indexed as follows:
        # 0, 1, ..., n for some n >= 0. Then last can be any i such that
        # 0 <= i <= n. If last < n then elements in positions
        # last+1, last+2, ..., n are superfluous.
        for i in range(last):
            self.assertIsInstance(basic.Array(elements=elements, last=i),
                                  basic.Array)
        
    def test_array_end(self):
        """Return last+1.
        """
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



if __name__ == "__main__":
    unittest.main(verbosity=0)