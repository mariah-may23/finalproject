# import the dependencies
import copy
import time

import pandas as pd
import plotly.express as px
from pandas import DataFrame

# import sorting algorithms from our custom sort module
from sort.bubble import bubble_sort
from sort.counting import count_sort
from sort.insertion import insertion_sort
from sort.mergeSort import merge_sort
from sort.quicksort import quicksort
from sort.radix import radix_sort


# sets up and displays a benchmark graph of sorting the given file by the given column
def plot(file: DataFrame, column: str):
    # store algorithms to be used
    algos = ['Merge Sort', 'QuickSort', 'Bubble Sort', 'Insertion Sort', 'Radix Sort', 'Counting Sort']

    # convert the dataframe column into a list
    numbers = file[column].tolist()

    # make a deep copy of the list to reuse it for each algorithm
    numbers_deep = copy.deepcopy(numbers)

    # let user know the program started
    print("Sorting... Wait until a browser window opens")

    # calculate how much time merge sort takes
    start = time.time()
    merge_sort(numbers)
    end = time.time()
    merge = (end - start) * 1000

    numbers = numbers_deep

    # calculate how much time bubble sort takes
    start = time.time()
    bubble_sort(numbers)
    end = time.time()
    bubble = (end - start)

    numbers = numbers_deep

    # calculate how much time counting sort takes
    start = time.time()
    count_sort(numbers)
    end = time.time()
    count = (end - start) * 1000

    numbers = numbers_deep

    # calculate how much time radix sort takes
    start = time.time()
    radix_sort(numbers)
    end = time.time()
    radix = (end - start) * 1000

    numbers = numbers_deep

    # calculate how much time quick sort takes
    start = time.time()
    quicksort(numbers)
    end = time.time()
    quick = (end - start)

    numbers = numbers_deep

    # calculate how much time insertion sort takes
    start = time.time()
    insertion_sort(numbers)
    end = time.time()
    insertion = (end - start) * 1000

    # store times
    times = [merge, quick, bubble, insertion, radix, count]

    # create dataframe
    df = pd.DataFrame(
        {"Sorting Algorithm": ['MergeSort', 'QuickSort', 'BubbleSort', 'Insertion Sort', 'RadixSort', 'Counting Sort'],
         "Time Complexity": ['LINEARITHMIC (n log(n))', 'LINEARITHMIC (n log(n))', 'QUADRATIC (n^2)',
                             'QUADRATIC (n^2)', 'LINEAR (n)', 'LINEAR (n)'],
         "Time": times,
         })

    # create the figure

    """ 
        'x' and 'y' tell what info to store on the axis
        'labels' allows you to name the axis
        'hover_name' allows to to store a title for the bar when it is hovered over
    """

    fig = px.bar(df, x=algos, y=times, color='Sorting Algorithm',
                 labels={'x': 'Sorting Algorithm', 'y': 'Time (ms)'},
                 hover_name='Time Complexity',
                 color_discrete_sequence=["lightseagreen", "lightseagreen", "lightskyblue", "lightskyblue",
                                          "palevioletred",
                                          "palevioletred"],
                 )

    # add the buttons to hide the chosen algorithm bar charts
    fig.update_layout(legend=dict(font=dict(family="Courier", size=17, color="black"), orientation="h",
                                  yanchor="bottom",
                                  y=1.00,
                                  xanchor="right",
                                  x=1),
                      legend_title="Click to hide the bar chart:",
                      font=dict(
                          size=18))

    fig.show()  # show webpage
