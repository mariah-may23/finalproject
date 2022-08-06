# import the necessary libraries
import pandas as pd
import time
import plotly.express as px
from bubble import bubbleSort
from mergeSort import mergeSort
from counting import count_sort
from bucket import bucketSort

# store algorithms to be used
SortingAlgo = ['MergeSort', 'BubbleSort', 'Counting Sort']

# get user's numbers
numbers = input("Enter the numbers of the SortingAlgo (ex: 3,6,1)")
numbers = numbers.split(',')
numbers = [int(x) for x in numbers]

# time mergesort takes
start = time.time()
mergeSort(numbers)
end = time.time()
merge = (end - start) * 1000
print("Merge total", merge)

# time bubblesort takes
start = time.time()
bubbleSort(numbers)
end = time.time()
bubble = (end - start) * 1000
print("Bubble total", bubble)

# time counting sort takes
start = time.time()
count_sort(numbers)
end = time.time()
count = (end - start) * 1000
print("Count total", count)

# time bucket sort takes
start = time.time()
bucketSort(numbers)
end = time.time()
bucket = (end - start) * 1000
print("Bucket total", bucket)

# store times
timeTaken = [merge, bubble, count]

pd.options.plotting.backend = "plotly"

# create dataframe
df = pd.DataFrame(dict(Sorting=['MergeSort', 'BubbleSort', 'CountingSort'],
                       TimeComplex=['LINEARITHMIC (nlogn)', 'QUADRATIC (n^2)', 'LINEAR (n)']))

# creating the figure
""" 
    'x' and 'y' tell what info to store on the axis
    'labels' allows you to name the axis
    'hover_name' allows to to store a title for the bar when it is hovered over
"""
fig = px.bar(df, x=SortingAlgo, y=timeTaken, color='Sorting', labels={'x': 'Algorithm', 'y': 'Time (ms)'},
             hover_name='TimeComplex')

fig.show()  # show
