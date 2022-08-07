# import the necessary libraries
import copy
import time

import pandas as pd
import plotly.express as px
from pandas import DataFrame

from sort.bubble import bubbleSort
from sort.counting import count_sort
from sort.insertion import insertionSort
from sort.mergeSort import mergeSort
from sort.quicksort import iterativeQuicksort
from sort.radix import radixSort


def plot(file: DataFrame, column: str):
    # store algorithms to be used
    SortingAlgo = ['MergeSort', 'QuickSort', 'BubbleSort', 'Insertion Sort', 'RadixSort', 'Counting Sort']

    numbers = file[column].tolist()

    numbers_deep = copy.deepcopy(numbers)

    # time mergesort takes
    start = time.time()
    mergeSort(numbers)

    end = time.time()
    merge = (end - start) * 1000
    # FIXME get rid of the printing?
    print("Merge total", merge)

    numbers = numbers_deep

    # time bubblesort takes
    start = time.time()
    bubbleSort(numbers)
    end = time.time()
    bubble = (end - start)
    # FIXME get rid of the printing?
    print("Bubble total", bubble)

    numbers = numbers_deep
    # time counting sort takes
    start = time.time()
    count_sort(numbers)
    end = time.time()
    count = (end - start) * 1000
    # FIXME get rid of the printing?
    print("Count total", count)

    numbers = numbers_deep
    # time radix sort takes
    start = time.time()
    radixSort(numbers)
    end = time.time()
    radix = (end - start) * 1000
    # FIXME get rid of the printing?
    print("Bucket total", radix)

    numbers = numbers_deep
    # time quick sort takes
    start = time.time()
    iterativeQuicksort(numbers)
    end = time.time()
    quick = (end - start)
    # FIXME get rid of the printing?
    print("Quick total", quick)

    numbers = numbers_deep
    # time insertion sort takes
    start = time.time()
    insertionSort(numbers)
    end = time.time()
    insertion = (end - start) * 1000
    # FIXME get rid of the printing?
    print("Insertion total", insertion)

    # store times
    timeTaken = [merge, quick, bubble, insertion, radix, count]

    # FIXME clean up please 🧹
    # pd.options.plotting.backend = "plotly"
    # year = file.year.tolist()
    #
    # max_year = max(year)
    # min_year = min(year)
    # range_year = max_year - min_year + 1
    # buckets = int(range_year / 6)
    # idx = 0

    # create dataframe
    df = pd.DataFrame(
        dict(Sorting=['MergeSort', 'QuickSort', 'BubbleSort', 'Insertion Sort', 'RadixSort', 'Counting Sort'],
             TimeComplex=['LINEARITHMIC (nlogn)', 'LINEARITHMIC (nlogn)', 'QUADRATIC (n^2)',
                          'QUADRATIC (n^2)', 'LINEAR (n)', 'LINEAR (n)'],
             Time=timeTaken,
             # Year=[min_year, min_year + buckets, min_year + buckets * 2, min_year + buckets * 3, min_year + buckets * 4,max_year]
             ))

    # creating the figure
    """ 
        'x' and 'y' tell what info to store on the axis
        'labels' allows you to name the axis
        'hover_name' allows to to store a title for the bar when it is hovered over
    """

    # FIXME clean up
    # timeTaken = timeTaken.sort()
    fig = px.bar(df, x=SortingAlgo, y=timeTaken, color='Sorting',
                 labels={'x': 'sort', 'y': 'Time (ms)'},
                 hover_name='TimeComplex',
                 color_discrete_sequence=["lightseagreen", "lightseagreen", "lightskyblue", "lightskyblue",
                                          "palevioletred",
                                          "palevioletred"],
                 # animation_frame="Year"

                 )

    # TODO why would we sort the values with an internal pandas sort algorithm to output the text file???
    #  this feature does not seem to provide any value or be relevant to the core idea of the project
    sorted_df = file.sort_values([column], ascending=True, inplace=False)
    sorted_df.to_csv("sorted_csv.csv")

    # FIXME why is there a call to show the page two times?
    # fig.show()  # show webpage
    fig.update_layout(legend=dict(font=dict(family="Courier", size=17, color="black"), orientation="h",
                                  yanchor="bottom",
                                  y=1.00,
                                  xanchor="right",
                                  x=1),
                      legend_title="Click to hide the algorithm",
                      font=dict(
                          size=18))

    fig.show()  # show webpage
