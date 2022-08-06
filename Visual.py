# import the necessary libraries
import copy

import pandas as pd
import time
import plotly.express as px


from bubble import bubbleSort
from mergeSort import mergeSort
from counting import count_sort
from radix import radixSort
from quicksort import iterativeQuicksort
from insertion import insertionSort

# store algorithms to be used
SortingAlgo = ['MergeSort', 'QuickSort', 'BubbleSort', 'Insertion Sort', 'RadixSort', 'Counting Sort']

columns = ["convicts", "year"]
file = pd.read_csv("Caste.csv")
numbers = file.convicts.tolist()

numbers_deep = copy.deepcopy(numbers)

# time mergesort takes
start = time.time()
mergeSort(numbers)

end = time.time()
merge = (end - start) * 1000
print("Merge total", merge)

numbers = numbers_deep

# time bubblesort takes
start = time.time()
bubbleSort(numbers)
end = time.time()
bubble = (end - start)
print("Bubble total", bubble)

numbers = numbers_deep
# time counting sort takes
start = time.time()
count_sort(numbers)
end = time.time()
count = (end - start) * 1000
print("Count total", count)

numbers = numbers_deep
# time radix sort takes
start = time.time()
radixSort(numbers)
end = time.time()
radix = (end - start) * 1000
print("Bucket total", radix)

numbers = numbers_deep
# time quick sort takes
start = time.time()
iterativeQuicksort(numbers)
end = time.time()
quick = (end - start)
print("Quick total", quick)

numbers = numbers_deep
# time insertion sort takes
start = time.time()
insertionSort(numbers)
end = time.time()
insertion = (end - start) * 1000
print("Insertion total", insertion)

# store times
timeTaken = [merge, quick, bubble, insertion, radix, count]

pd.options.plotting.backend = "plotly"
year = file.year.tolist()

max_year = max(year)
min_year = min(year)
range_year = max_year - min_year + 1
buckets = int(range_year / 6)
idx = 0

# create dataframe
df = pd.DataFrame(
    dict(Click_To_View=['MergeSort', 'QuickSort', 'BubbleSort', 'Insertion Sort', 'RadixSort', 'Counting Sort'],
         TimeComplex=['LINEARITHMIC (nlogn)', 'LINEARITHMIC (nlogn)', 'QUADRATIC (n^2)',
                      'QUADRATIC (n^2)', 'LINEAR (n)', 'LINEAR (n)'],
         Time=timeTaken,
         #Year=[min_year, min_year + buckets, min_year + buckets * 2, min_year + buckets * 3, min_year + buckets * 4,max_year]
         ))

# creating the figure
""" 
    'x' and 'y' tell what info to store on the axis
    'labels' allows you to name the axis
    'hover_name' allows to to store a title for the bar when it is hovered over
"""
# timeTaken = timeTaken.sort()
fig = px.bar(df, x=SortingAlgo, y=timeTaken, color='Click_To_View',
             labels={'x': 'Sorting Algorithms', 'y': 'Time (ms)'},
             hover_name='TimeComplex',
             color_discrete_sequence=["lightseagreen", "lightseagreen", "lightskyblue", "lightskyblue", "lemonchiffon",
                                      "lemonchiffon"],
             # animation_frame="Year"

             )


sorted_df = file.sort_values(["convicts"], ascending=True, inplace=False)
sorted_df.to_csv("Sorted_csv.csv")

fig.show()  # show webpage
fig.update_layout(legend=dict(font=dict(family="Courier", size=17, color="black"), orientation="h",
                              yanchor="bottom",
                              y=1.00,
                              xanchor="right",
                              x=1), title="Visualizing Sorting Algorithms",
                  legend_title="Click To View The Algorithm",
                  font=dict(
                      size=18))

fig.show()  # show webpage
