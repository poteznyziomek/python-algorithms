import unittest
import algorithms.sorter as sorter


class NumbersClassListLikeProperties(unittest.TestCase):
	
	def test_special_method_len(self):
		'''Calling len on an instance should return the len(inst.a_list)'''
		inst = sorter.Numbers([1, 2, 3, 4, 5, 6, 7])
		self.assertEqual(len(inst), 7)
	
	def test_special_method_contains(self):
		'''Numbers class should support 'x in inst' statement'''
		inst = sorter.Numbers([4.06, -2.1, 3.39, 0.09, -0.91, 6.03, -1.12])
		self.assertIn(-2.1, inst)
		self.assertNotIn('-2.1', inst)
		self.assertNotIn('Niko the cat', inst)
	
	def test_special_method_getitem(self):
		'''Numbers class should support element subscription'''
		a_list = [-2.14, -5.88, -0.23, -4.4, -1.08]
		inst = sorter.Numbers(a_list)
		for i in range(len(a_list)):
			self.assertEqual(inst[i], a_list[i])
		
	def test_getitem_index_error(self):
		'''Numbers should raise IndexError when list index is out of range'''
		inst = sorter.Numbers([-2, 0, -4, -3, -6])
		self.assertRaises(IndexError, inst.__getitem__, 5)
	
	def test_special_method_setitem(self):
		'''Numbers should support setting item by key'''
		a_list = [0, 3, 7, 9, 3, 4, 9]
		inst = sorter.Numbers(a_list)
		a_list[1] = 0.9
		inst[1] = 0.9
		self.assertListEqual(a_list, inst.a_list)
	
	def test_special_method_delitem(self):
		'''Numbers should support del keyword'''
		a_list = [1.05, -4.73, 0.67, -2.25, 1.83]
		inst = sorter.Numbers(a_list)
		del a_list[3], inst[3]
		self.assertListEqual(a_list, inst.a_list)
	
	def test_append(self):
		'''Numbers should support list appending'''
		a_list = [0.73, -2.16, -6.22, -2.65, 2.35]
		inst = sorter.Numbers(a_list)
		a_list.append(29)
		inst.append(29)
		self.assertListEqual(a_list, inst.a_list)

class NumbersClassBadInput(unittest.TestCase):
	
	def test_numbers_type_error_exception_letter_string(self):
		'''Instantiating Numbers class with invalid argument should fail.
		
		When Numbers is passed a_list where at least one element is of type
		str (e.g. 'Niko the cat'), then __init__ re-raises NumbersTypeError
		exception which is originally raised by Numbers.validate_list method.
		'''
		a_list = [92, 99, 7, 23, 72, 10, 38, 8, 'Niko the cat', 86, 85]
		self.assertRaises(sorter.NumbersTypeError, sorter.Numbers, a_list)
	
	def test_numbers_type_error_exception_int_string(self):
		'''Instantiating Numbers class with invalid argument should fail.
		
		When Numbers is passed a_list where at least one element is of type
		str (e.g. '2' or '3.1'), then __init__ re-raises NumbersTypeError
		exception which is originally raised by Numbers.validate_list method.
		'''
		a_list = [86, 77, 1, 77, 49, 21, '6']
		self.assertRaises(sorter.NumbersTypeError, sorter.Numbers, a_list)
	
	def test_numbers_type_error_exception_float_string(self):
		'''Instantiating Numbers class with invalid argument should fail.
		
		When Numbers is passed a_list where at least one element is of type
		str (e.g. '.4' or '2.73'), then __init__ re-raises NumbersTypeError
		exception which is originally raised by Numbers.validate_list method.
		'''
		a_list = [2.47,  6.29,  3.53,  3.66,  -1.22,  -1.85,  '3.99',  5.55]
		self.assertRaises(sorter.NumbersTypeError, sorter.Numbers, a_list)
	
	def test_numbers_type_error_setitem(self):
		'''Throw NumbersTypeError exception when setting non int/float value'''
		inst = sorter.Numbers([-1, 1, 6, 2, 4, 5, 9])
		key, value = 1, 'Niko the big, fluffy cat'
		self.assertRaises(sorter.NumbersTypeError, inst.__setitem__, key, value)
	
	def test_append_numbers_type_error(self):
		'''Throw NumbersTypeError exception when appending non int/float value'''
		inst = sorter.Numbers([-2, -3, 8, -1, 8, 6, 5])
		self.assertRaises(sorter.NumbersTypeError, inst.append, 'Niko')

class NumbersClassBubbleSort(unittest.TestCase):

    def test_bubble_positive_integers(self):
        a_list = [163, 82, 73, 98, 311, 280, 486]
        inst = sorter.Numbers(a_list)
        inst.bubble()
        correct_result = [73, 82, 98, 163, 280, 311, 486]
        self.assertListEqual(inst.a_list, correct_result)
    
    def test_bubble_integers(self):
        a_list = [-524, -13, 459, -409, -551, 268, 966, 708]
        inst = sorter.Numbers(a_list)
        inst.bubble()
        correct_result = [
            -551, -524, -409, -13,
            268, 459, 708, 966
        ]
        self.assertListEqual(inst.a_list, correct_result)
    
    def test_bubble_positive_reals(self):
        a_list = [
            45.961732798702386, 67.07936186682147,
            12.011696271466631, 11.547817329512544,
            48.46421976476098, 22.639592181910203,
            74.63828976517652, 56.26218251097809,
            58.27341337622983, 2.2814320145361773
        ]
        inst = sorter.Numbers(a_list)
        inst.bubble()
        correct_result = [
            2.2814320145361773, 11.547817329512544,
            12.011696271466631, 22.639592181910203,
            45.961732798702386, 48.46421976476098,
            56.26218251097809, 58.27341337622983,
            67.07936186682147, 74.63828976517652
        ]
        self.assertListEqual(inst.a_list, correct_result)
    def test_bubble_reals(self):
        a_list = [
            -231.98497465842354, -35.87467237092551,
            -76.22394678445153, -746.5367393542417,
            464.55122563049486, -767.0239891633445,
            356.00486474446643, 44.41729141532494,
            413.86150276022727, 502.75541658589634
        ]
        inst = sorter.Numbers(a_list)
        inst.bubble()
        correct_result = [
            -767.0239891633445, -746.5367393542417,
            -231.98497465842354, -76.22394678445153,
            -35.87467237092551, 44.41729141532494,
            356.00486474446643, 413.86150276022727,
            464.55122563049486, 502.75541658589634
        ]
        self.assertListEqual(inst.a_list, correct_result)
    def test_bubble_integers_reals(self):
        a_list = [
            -271, 402,
            133, 403,
            -136.71570327215466, 488.60257724670066,
            -171.23574339024356, 213.55582391551604,
            534, -443.957615131471
        ]
        inst = sorter.Numbers(a_list)
        inst.bubble()
        correct_result = [
            -443.957615131471, -271,
            -171.23574339024356, -136.71570327215466,
            133, 213.55582391551604,
            402, 403,
            488.60257724670066, 534
        ]
        self.assertListEqual(inst.a_list, correct_result)
    

class NumbersClassInsertionSort(unittest.TestCase):

    def test_insertion(self):
        a_list = [5, 4, 3, 2, 1]
        inst = sorter.Numbers(a_list)
        inst.insertion()
        correct_result = [1, 2, 3, 4, 5]
        self.assertListEqual(inst.a_list, correct_result)


class NumbersClassSelectionSort(unittest.TestCase):
	
	def test_selection(self):
		a_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
		inst = sorter.Numbers(a_list)
		inst.selection()
		correct_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		self.assertListEqual(inst.a_list, correct_result)


class NumbersClassMerge(unittest.TestCase):
	
	def test_merge_function(self):
		'''Merging two sorted subarrays should yield a sorted array'''
		a_list = [2, 4, 6, 7, 1, 2, 3, 5]
		b_list = [
			-3.3, -1.1, 1.52, 2.78, 9.86, 11.45, 14.32, -4.34,
			-0.65, 10.01, 10.22, 10.64, 11.6, 12.0, 14.81
		]
		a_inst = sorter.Numbers([])
		b_inst = sorter.Numbers([])
		a_p, a_q, a_r = 0, 3, 7
		b_p, b_q, b_r = 0, 6, 14
		a_inst.merge(a_list, a_p, a_q, a_r)
		b_inst.merge(b_list, b_p, b_q, b_r)
		a_correct_result = [1, 2, 2, 3, 4, 5, 6, 7]
		b_correct_result = [
			-4.34, -3.3, -1.1, -0.65, 1.52, 2.78, 9.86, 10.01,
			10.22, 10.64, 11.45, 11.6, 12.0, 14.32, 14.81
		]
		self.assertListEqual(a_list, a_correct_result)
		self.assertListEqual(b_list, b_correct_result)
	
	def test_merge_sort(self):
		'''Test merge sort'''
		a_list = [12, 3, 7, 9, 14, 6, 11, 2]
		a_inst = sorter.Numbers(a_list)
		a_correct_result = [2, 3, 6, 7, 9, 11, 12, 14]
		a_inst.merge_sort()
		self.assertListEqual(a_inst.a_list, a_correct_result)

if __name__ == "__main__":
    unittest.main(verbosity=2)
   #unittest.main()
