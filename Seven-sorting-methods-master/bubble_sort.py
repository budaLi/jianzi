'''

README

This module aims to introduce the popular sorting method--bubble sort
and three different kind of schemes are conducted by python 3 language.


'''

# -*- coding:utf-8 -*-

import math

class BubbleSortMethod(object):
	# construction method
	def __init__(self,array):
		self.array=array

	# the most common method, the maximum number in the array is swapped to the last position during an iteration.
	def bubble_sort1(self):
		array=self.array
		n=len(array)
		for i in range(n):
			for j in range(n-i-1):
				if array[j] > array[j+1]:
					tmp=array[j]
					array[j]=array[j+1]
					array[j+1]=tmp

		return array



if __name__=='__main__':

	testlist=[2,5,7,1,9,4,6,0,12,35,7]
	bubble=BubbleSortMethod(testlist)  # new object of BubbleSortMethod class
	sortlist=bubble.bubble_sort1()







