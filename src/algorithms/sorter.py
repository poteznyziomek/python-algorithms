import math

class NumbersTypeError(TypeError): pass


class Numbers(object):
	'''Create a list-like object with int/float values only'''
	
	def __init__(self, a_list=[]):
		try:
			self.a_list = self.validate_list(a_list)
		except NumbersTypeError:
			raise
	
	def __len__(self):
		'''Return len(self.a_list)'''
		return len(self.a_list)
	
	def __contains__(self, element):
		'''Return True if element in self.a_list, False otherwise'''
		return element in self.a_list
	
	def __getitem__(self, key):
		'''Return self.a_list[key]'''
		if key >= len(self.a_list):
			raise IndexError
		return self.a_list[key]
	
	def __setitem__(self, key, value):
		'''Equivalent to self.a_list[key] = value'''
		if not (isinstance(value, int) or isinstance(value, float)):
			error_msg = f'List elements cannot be of type {type(value)}.'
			raise NumbersTypeError
		self.a_list[key] = value
	
	def __delitem__(self, key):
		'''Equivalent to del self.a_list[key]'''
		del self.a_list[key]
	
	def validate_list(self, a_list):
		'''Validate a_list passed to Numbers when instantiating.
		
		Return a_list if its every element is either of type int or float,
		raise NumbersTypeError otherwise.
		'''
		for item in a_list:
			if not (isinstance(item, int) or isinstance(item, float)):
				error_msg = f'List elements cannnot be of type {type(item)}.'
				raise NumbersTypeError(error_msg)
		return a_list
	
	def append(self, key):
		'''Append key to the end of the self.a_list
		
		Raise NumbersTypeError if type of key is other than int or float.
		'''
		if not (isinstance(key, int) or isinstance(key, float)):
			error_msg = f'List elements cannot be of type {type(key)}.'
			raise NumbersTypeError(error_msg)
		self.a_list.append(key)

	def bubble(self):
		'''Sort self.a_list using a bubble sort algorithm'''
		for i in range(len(self.a_list)):
			for j in range(len(self.a_list)-1-i):
				if self.a_list[j] > self.a_list[j+1]:
					self.a_list[j], self.a_list[j+1] = self.a_list[j+1], \
                		self.a_list[j]
	
	def insertion(self):
		'''Sort self.a_list using an insertion sort algorithm'''
		for j in range(1, len(self.a_list)):
			key = self.a_list[j]
			# insert self.a_list[j] into the sorted sequence self.a_list[:j]
			i = j - 1
			while i >= 0 and self.a_list[i] > key:
				self.a_list[i+1] = self.a_list[i]
				i -= 1
			self.a_list[i+1] = key
	
	def insertion_sort_r(self):
		'''Sort self.a_list using a recursive insertion sort algorighm.
		'''
		n = len(self.a_list)
		self._insertion_sort_r(self.a_list, n)

	def _insertion_sort_r(self, a_list, n):
		'''A method that does the actual job of sorting.
		
		This method is called by insertion_sort_r.
		'''
		if n < 2:
			return
		self._insertion_sort_r(a_list, n-1)
		key = a_list[n-1]
		j = n - 2
		while j >= 0 and a_list[j] > key:
			a_list[j+1] = a_list[j]
			j -= 1
		a_list[j+1] = key

	
	def selection(self):
		'''Sort self.a_list using a selection sort algorithm'''
		for i in range(len(self.a_list)-1):
			# key - i is the index of the smallest element of self.a_list[i:]
			key = self.a_list[i:].index(min(self.a_list[i:])) + i
			self.a_list[i], self.a_list[key] = self.a_list[key], self.a_list[i]
	
	@staticmethod
	def merge(a_list, p, q, r):
		'''Merge two sorted sublists into one sorted list'''
		n_L = q - p + 1 # length of a_list[p:q+1]
		n_R = r - q # length of a_list[q+1:r+1]
		L = a_list[p:q+1]
		R = a_list[q+1:r+1]
		i = 0 # i indexes the smallest remaining element in L
		j = 0 # j indexes the smallest remaining element in R
		k = p # k indexes the location in a_list to fill
		
		# As long as each of the arrays L and R contains an unmerged element,
		# copy the smallest unmerged element back into a_list[p:r+1]
		while i < n_L and j < n_R:
			if L[i] <= R[j]:
				a_list[k] = L[i]
				i += 1
			else:
				a_list[k] = R[j]
				j += 1
			k += 1
		
		# Having gone through one of L and R entirely, copy the remainder of
		# the other to the end of a_list[p:r+1]
		while i < n_L:
			a_list[k] = L[i]
			i += 1
			k += 1
		while j < n_R:
			a_list[k] = R[j]
			j += 1
			k += 1
	
	def merge_sort(self):
		'''Sort self.a_list using merge sort algorithm'''
		n = self.a_list.index(self.a_list[-1])
		self._merge_sort(self.a_list, 0, n)
	
	def _merge_sort(self, a_list, p, r):
		'''A method that does the actual job of sorting.
		
		Is called by merge_sort method.'''
		if p >= r:
			return
		q = math.floor((p+r)/2)
		self._merge_sort(a_list, p, q)
		self._merge_sort(a_list, q+1, r)
		self.merge(a_list, p, q, r)