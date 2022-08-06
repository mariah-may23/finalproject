// =================== Libraries ==================
#include <stdio.h> // Include file for standart input/output

// =============== Helper Functions ===============

// Swaps two numbers in an array
// Input: The 'address of' an index into an array for positions in an array.
void swap(int* a, int* b){
    // TODO: Swap two integers in an array.
    //
	int temp = *a;
	*a = *b;
	*b = temp;
}


// Name: sort
// Input(s):
//          (1) 'array' is a pointer to an integer address. 
//              This is the start of some 'contiguous block of memory' that we will sort.
//          (2) 'size' tells us how big the array of data is we are sorting.
// Output: No value is returned, but 'array' should be modified to store a sorted array of numbers.
void sortIntegers(int* array, unsigned int size){
    // TODO: Implement insertion sort
    //
	int i;
	int j;
	int min;
	for(i = 1; i < size ; i++) {
		min = array[i];
		j = i -1;
		while( j >=0 && array[j] > min) {

			array[j+1] =  array[j];
			j--;
		}
		
		swap(&array[j+1], &min);	
	}
	
}
