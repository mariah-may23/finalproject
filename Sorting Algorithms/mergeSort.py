import time
def mergeSort(numbers):

    if len(numbers) > 1:

        # Finding the mid of the array
        mid = len(numbers) // 2

        # Dividing the array elements
        L = numbers[:mid]

        # into 2 halves
        R = numbers[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                numbers[k] = L[i]
                i += 1
            else:
                numbers[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            numbers[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            numbers[k] = R[j]
            j += 1
            k += 1

    return numbers
