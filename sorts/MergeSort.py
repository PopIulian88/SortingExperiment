def merge(arr, left_index, mid_index, right_index):
	## left and right arrays
	left_array = arr[left_index:mid_index+1]
	right_array = arr[mid_index+1:right_index+1]

	## getting the left and right array lengths
	left_array_length = mid_index - left_index + 1
	right_array_length = right_index - mid_index

	## indexes for merging two arrays
	i = j = 0

	## index for array elements replacement
	k = left_index

	## iterating over the two sub-arrays
	while i < left_array_length and j < right_array_length:

		## comapring the elements from left and right arrays
		if left_array[i] < right_array[j]:
			arr[k] = left_array[i]
			i += 1
		else:
			arr[k] = right_array[j]
			j += 1
		k += 1

	## adding remaining elements from the left and right arrays
	while i < left_array_length:
		arr[k] = left_array[i]
		i += 1
		k += 1

	while j < right_array_length:
		j += 1
		k += 1

def mergeSort(arr, left_index, right_index):
	## base case for recursive function
	if left_index >= right_index:
		return 

	## finding the middle index
	mid_index = (left_index + right_index) // 2

	## recursive calls
	mergeSort(arr, left_index, mid_index)
	mergeSort(arr, mid_index + 1, right_index)

	## merging the two sub-arrays
	merge(arr, left_index, mid_index, right_index)
	return arr