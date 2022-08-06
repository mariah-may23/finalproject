# Bucket Sort in Python


def bucketSort(array):
    bucket = []

    max_element = max(array)

    min_element = min(array)

    range_arr = int((max_element - min_element) / 10)

    if range_arr < 1:
        range_arr = 1

    # Create empty buckets
    for i in range(10):
        bucket.append([])

    # print(bucket)
    # Insert elements into their respective buckets
    for j in array:
        index_b = int(j)

        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Sorted Array in descending order is")
print(bucketSort(array))
