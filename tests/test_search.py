import unittest
import algorithms.search as search

class BinarySearch(unittest.TestCase):

    def test_binary_search_integers(self):
        '''binary_search determines whether target value is a member of a list consisting of integer values.'''
        a_list = [-29, -24, -22, -17, 7, 9, 18, 21, 24, 27]
        for i in range(len(a_list)):
            self.assertEqual(i,
                search.binary_search(
                    a_list[i], a_list, 0, len(a_list)-1))
    
    def test_binary_serach_floats(self):
        '''binary_search determines whether target value is a member of a list consisting of float values.'''
        a_list = [-8.36, -5.97, -2.54, -2.15, 3.75, 4.77, 5.91, 6.96]
        for i in range(len(a_list)):
            self.assertEqual(i,
                search.binary_search(
                    a_list[i], a_list, 0, len(a_list)-1))

    def test_binary_search_strings(self):
        '''binary_search determines whether target value is a member of a list consisting of str values.'''
        a_list = ['a', 'aa', 'b', 'c', 'ddd', 'x', 'y', 'z']
        for i in range(len(a_list)):
            self.assertEqual(i,
                search.binary_search(
                    a_list[i], a_list, 0, len(a_list)-1))

    def test_binary_search_nonexistent_values(self):
        '''binary_search should return None if the target value is not present in the input list.'''
        a_list = [-24, -20, -13, -8, -3, 0, 3, 4]
        b_list = [-6.89, -5.54, -1.4, -1.27, 0.5, 3.7, 5.26, 9.16]
        c_list = ['a', 'aaaba', 'abde', 'hxh', 'xyz']
        self.assertEqual(
            search.binary_search(
                -23, a_list, 0, len(a_list)-1), None)
        self.assertEqual(
            search.binary_search(
                9.166, b_list, 0, len(b_list)-1), None)
        self.assertEqual(
            search.binary_search(
                'aaba', c_list, 0, len(c_list)-1), None)
    
    def test_is_sorted(self):
        '''is_sorted should return False when input list is unsorted, True otherwise.'''
        a_list = list(range(10,0,-1))
        b_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        c_list = ['f', 'e', 'd', 'c', 'b', 'a']
        unsorted_lists = [a_list, b_list, c_list]
        d_list = list(range(10))
        e_list = ['a', 'aa', 'b', 'c', 'd', 'e']
        sorted_lists = [d_list, e_list]

        for l in unsorted_lists:
            self.assertFalse(search.is_sorted(l))
        for l in sorted_lists:
            self.assertTrue(search.is_sorted(l))
    
    def test_binary_search_unsorted_input_list(self):
        '''binary_search should raise exception when input list is unsorted.'''
        a_list = [11, 0, 0, -5, -14, 19, -9, -16]
        b_list = [-5.91, 9.61, 6.53, 6.29,
                  8.08, -6.45, -4.46, -0.45]
        c_list = ['aa', 'a', 'b', 'c', 'cc', 'd']
        unsorted_lists = [a_list, b_list, c_list]
        for l in unsorted_lists:
            self.assertRaises(search.InputError,
                search.binary_search, 1.5, l, 0, 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)