# CS5800 - Algorithms: Final Project

## How to run?

Open the project directory in the terminal and run this command:

``python[your version of python] main.py [path to a .csv file] [name of the column in the csv file]
``

Sample .csv files are accessible from the ``/db`` subdirectory.

At the moment the app only works with integer numerical data.

## Topic

Visualization and Quantitative Comparisons of Various Sorting Algorithms for Large Data Sets

## Context

Everyone has their own unique way of learning. From adapting to digital coursework to staying disciplined with minimal
face-to-face interactions, getting used to this new type of education may cause students to struggle — especially if
their individual learning style isn’t being addressed. Gaining momentum in the 1960s through tests like the Myers-Briggs
Type Indicator, the learning style theory posits that different students learn best when information is presented to
them in a particular way. The learning style theory was popularized in 1992 when Fleming and Mills suggested a new model
of learning. The VARK Model is used to explain the different ways that students learn - Visual, Auditory,
Reading-Writing and Kinesthetic.

Visual learning refers to a mode of learning where students rely on graphic aids to remember and learn material. Visual
learners can easily visualize objects, have a great sense of balance and alignment, are very color-oriented and can
effortlessly envision imagery. Visual learners learn best by color-coding their notes, making to-do lists and using
concept maps to organize their thoughts.

When it comes to algorithms, some people consume the information by reading through pseudocode to understand the
specifics while others may process that same information by visualizing how an algorithm works. Our group aims to dive
further into the concept of visual learning and make algorithms more intuitive for their users by implementing
visualizations for some of most frequently used sorting algorithms. Each of us have our own unique motivation for
driving and implementing this goal. Coming into the Align program with diverse backgrounds, we have handled large
volumes of data in our respective fields. At the same time, we have come across the lack of educational tools and
knowledge for non-CS professionals to be able to sort through and implement a sorting program to easily access and
categorize the required parameterized data.

Aditya’s motivation for pursuing this topic is because he loves to build financial products that users love. Having more
context with tradeoffs for selecting one algorithmic implementation versus another gives him more perspective during the
costs/benefit analysis phase of product development. These insights are extremely valuable for making decisions and
prioritizing which feature to build based on accurate data.

Coming from the healthcare background, Shriya is passionate about this topic because she finds learning visually very
effective. Her experience of conducting various research working with tons of patient information in the medical field
exposed the problem of not being able to effectively categorize data and motivated her to understand the driving forces
behind how this data can be more effectively sorted through. Visualizing the ways different data sets are being sorted
and categorized satiate this curiosity and she believes this would serve as a great aid for non-tech grads to be able to
make decisions regarding their choice of algorithms.

Mariah strongly believes in helping students connect the dots more quickly by giving them a tool to learn about multiple
algorithms. Understanding when to use a specific algorithm and why is just as important as how an algorithm is
implemented. Developers in training can get a better grasp on the tradeoffs of selecting one algorithm over another to
augment their skillset. She believes this project will serve as a great educational tool for students trying to get a
grip of the subject of sorting as a whole.

The goal of this project fits Mit’s pursuits of being better prepared to handle the multitude of problems that will be
thrown at him on the job once he moves to the industry. Data visualizations making it easier to choose the right
algorithm on the job by comparing and benchmarking the performance of various algorithms on different inputs.

## What is the Question We Wish to Answer?

Problem: The main aim of this project is to be able to build an educational, visualization tool for analyzing various
sorting algorithms. Most learners struggle to see how different sorting algorithms work between each other for a common
dataset. There are lot of websites and tools online like VisuAlgo that helps understand implementation of different
types of algorithms for usually small data sets and only allow implementation knowledge to the user. Based on our
research, we did not find any tools that would allow the user to understand and pick the best algorithm for their
datasets based on comparisons of these most sort after algorithms.

Solution: We want to design an visual tool for sorting algorithms that not only has the preliminary features of the
prevalent online websites for visualizing algorithm i.e. understanding how the algorithms work by showing a step by step
breakdown, but we want to take a step ahead and allow the users to see which algorithm would work better for their data
sets based on a comparison chart. Our ultimate goal is to be able to implement basic visualizations along with
comparisons specific to their data set and further, be able to implement a side-to-side visualization tool to help them
understand the algorithms better. Our tool will allow a user to easily compare the performance of different algorithms
on different inputs. We understand that the undertaking of this project is ambitious and therefore have divided our
projects into MVP and stretch goals dependent on the progress of our project as time permits.



## Scope

We will examine various sorting algorithms for numerical datasets.
More specifically, we intend to look at six key algorithms belonging to three distinct classes. These classes were
decided based on their time complexities. They are as follows:

1. Linear – counting sort, and bucket sort
2. Linearithmic – merge sort and quicksort
3. Quadratic – insertion sort and bubble sort.

Though there are many more classes of algorithms based on this criterion, we believe that examination of algorithms
belonging to these unique categories will provide a diverse view of varying runtimes.

Time permitting, this tool can be expanded to include more algorithms in other classes for the purpose of comparison to
expand the range of complexities investigated. Potentially, we will further develop our tool to include algorithmic
specific visuals to aid in the display of any algorithm. For example, this may include creating buckets to better
explain distribution of numerical elements in bucket sort. It may also include the demonstration of breaking an original
array into singular fragments so they may be placed back together in ascending order for merge sort. These more
intricate visualization ideas could further supplement the algorithms we wish to examine and would serve to create a
further comprehensive tool.

## Analysis											

## Getting Started

When our group met to discuss ideas for the final project we realized that we were facing the same question over the course of CS5800 – how can we improve our understanding of algorithms presented in the course, how can we get more hands-on practice with them, or put in programmer slang, – how can we grok the algorithms. 

To define our approach to this problem we conducted a review of the algorithm visualization tools available on the web. Among the tools, we’d looked at were Visualgo and the project of the USFCA. We determined that all the tools we’ve reviewed lacked two components – side-by-side algorithm comparisons and an actual performance benchmark for measuring which algorithm works better with the dataset of the user. Thus the idea of our project was born.

As a programming language to implement the project we chose Python for its ease of use, a wide variety of user-friendly libraries to use for visualization, and clean and neat implementations of sorting algorithms available. 

Being aware of the time constraints, we decided to focus on implementing an MVP as a first step of the project. We chose a performance benchmark graph as a key feature of the MVP. 
We have created a mock-up of the interface of the benchmark: 



All remaining features were chosen to be stretch goals after we successfully implement the MVP. We decided to practice a small-scale team style of development, uploading our code to GitHub without pull requests and doing pair programming over zoom to enhance productivity and simplify time management.

## Creating the Benchmark Graph
First, to choose the visualization library to best fit our needs, we picked NumPy, Pandas x Matplotlib, and Plotly and tested each library for how fast and how close we can implement a bar chart we put together as an interface mockup. NumPy turned out to be lacking in features to implement detailed bar charts as we wanted, while Matplotlib and Plotly both were great options and allowed for all the features that we needed. Between Plotly and Matplotlib, Plotly looked like the best candidate since it has additional features such as displaying the results on the interactive webpage, showing additional information for each bar on mouse hover, and allowing to add buttons to hide/show the relevant bar charts. We created a Proof of Concept implementation with Plotly and chose it as a framework to work with in this phase of the project.
We initially decided to use pre-existing implementations of the algorithms and test them out using small inputs for the code. We realized that the existing implementations would not be ideal for handling large datasets so we recoded the algorithm using a uniform template for inputs as well as ensuring they can work on large data sets of any given size. Some things we needed to account for was using iterative methods over recursive to avoid reaching memory mark and using data structures that used minimal space for the dataset. 

The visualization was created with a vision of being able to display the different sorting times in the most efficient and user-friendly manner. We wanted to use a graph representation that was both easy to display and easy to understand. We used Plotly’s bar graphs to show the time taken on the y-axis and the sorting algorithms on the x-axis. We also wanted additional features for users to be able to isolate different algorithms and compare them against each other. This was implemented using the button functionality in which the users just need to click the algorithm names they want to remove (displayed on the top of the screen ) from the graph and isolate the ones they want to keep. This allows better visualization of the comparator. 

Based on the need for a proper visualizing tool and to analyze the different workings of the sorting algorithms, we coded a program to create a webpage that displayed the various sorting 
 



After achieving our MVP, our major motivation was to be able to sort and display data for any industry, any field. To this end, we used CSVs from transportation, health, jail records, and insurance collections from Kaggle and hooked them to our code as feeder inputs for our algorithm. Our program was able to efficiently sort data, display the running time of different algorithms as well as produce an output file based on the most efficient algorithm.

## Limitations

In the early stages of building our tool, we majorly focused on designing for the visual aspect of it. Initially, we ran into several issues concerning the look of our interface, including:

Mapping the color of each bar to the class of the algorithm
Creating an interactive legend as a header
Scaling plot columns

Plotly was chosen as the visualization library for the reasons that it best fit our needs and goals for the tool, however, we did not have prior experience using it. In order to develop our interface, further study into the fundamentals of this interactive graphing library gave us the understanding to resolve these issues.

The datasets we used when building the interface were all relatively small. Before a command line interface was created (see part IV), we manually entered datasets into our program so that an interface could be generated rather quickly. Initially, no errors occurred; the simple data was easily run and sorted. As we began to further develop our application, we decided to test with larger numbers and datasets. Here, we came across the following problem: our quicksort algorithm was exceeding the maximum recursion depth.

Originally, the quicksort algorithm used a recursive approach. The initial datasets did not cause this error because the function called itself fewer times than the maximum recursive depth. This differs from larger datasets, which need to call the function more times. When tested with large data, the IDE raised this error to protect against stack overflow that would arise in an infinite recursion. To prevent this error, we decided to use a quicksort algorithm with an iterative approach. This new approach did not raise any errors.  

## Finding the Data

We sourced our data from Kaggle which is an open source site with publicly available data sets used in many software engineering development projects. Because there were so many formats for usable data ranging from csv, json, sql, etc., we had a plethora of options available for our data acquisition process.
 
We leveraged data sets ranging from convict data, insurance data, population data, and rental data to validate our sorting algorithms and test against datasets across a variety of industries. To keep our code consistent, we standardized the file format to be exclusively csv, with a consideration to handle additional formats in the future. 

The data was fed into the application as a csv file along with the column to sort. Both of these parameters were then passed to a plot function that would take in the column to be sorted along with the file stored as a data frame. The plot function would then apply each of the predefined sorting algorithms to the selected column in the csv dataset.

## Creating the Command-Line Interface
To provide ourselves and our users a way to comfortably use our application, we decided to implement a command-line interface (CLI).
This was the list of features that we’ve prioritized for our CLI to have:
Take a path to the .csv file from the user as an argument and pass the path to the csv-reader
Take the name of the column to sort from the user as an argument and pass the column name to the benchmark graph (plotting) module
Process any errors that the user makes while using the CLI
Since we were working in the results- and speed-oriented style, we decided to look for existing implementations of the aforementioned functionality. 
Our choice was the CLI library called Typer. Typer provides out-of-the-box argument parsing, API for error handling, and simple style-customization of the command-line output (e.g. adding colors and font styles). It fit perfectly for our task.
Additionally, we implemented an error-handling logic for the file path and column name. Specifically, we are checking that the given path is correct and that the given column exists in the provided .csv file. Also, within the current scope of the project, we decided to limit sorting to only integer numerical values. To that end, we added another error check for the data type of the column.
Though we’ve only used a small subset of all the features that Typer offers, the ease of use that it opens prompts us to continue using this library in the consequent projects that our team makes.
## Creating the Sorting Visualizer
![](https://github.com/mariah-may23/finalproject/blob/main/gif.gif)

	
After achieving our MVP, which was to create a basic comparator of the sorting time taken to sort the csv data sets. We achieved that, as described above, by showing a basic bar graph representation of the various sorting time taken by the algorithms. The next step was to actually develop the visualizer. It was challenging initially to come up with a proper strategy for the implementation. The first choice was between the UI for the visualizer. Tkinter, was an easy to understand and apply UI but the biggest hurdle came when trying to implement algorithms that did not sort in place and required extra memory handling. Moreover, the GUI did not work smoothly for datasets greater than 200. 

	
So, scratching the implementation right from the base, we turned to PyGame - the graphical package used to design games in Python. It was definitely a learning curve with the package, but the quality and quantity of sorting took a big leap. It was easier to implement the setup for the algorithm dataset but the real challenge was to create a uniform platform for the implementation of different classes of algorithms handling both in-place and extra memory-requiring algorithms.  The sorting algorithms had to be reformed to take in additional inputs for the graphical representation of various data being sorted at every step. We were able to refactor the code to show a proper visualization of data being sorted in ascending order. The visualizer is shown below.



## Refactoring

To make our code more readable and easy to work with – to run it as well as to implement new features, we’ve completed a refactoring. 

We separated our code into two three modules – the sort module, containing all the sorting algorithms that we used, a main file, containing the CLI logic, and visu module, containing the logic responsible for displaying the benchmark graph. 

Then the code was split up into logical blocks and abstracted into separate functions. We isolated three functions within the main module – the main function itself, which acts as a Controller and calls every other function in the project, the function to read the path to the file and process the file into a Pandas DataFrame, and the function to check whether the given column exists in the file and its datatype is an integer. 

For the visu module, we decided to stick with one function to plot the benchmark graph since it nicely bundled together all the relevant procedures. 
We cleaned up our code from the unnecessary comments and code used for testing. On the other hand, we added new comments to clarify certain procedures and commands within the project. We provided naming clarity to our variables and functions and made sure that each of the names follows the Python naming conventions.


## Conclusion										

In conclusion the team was able to successfully validate the problem statement and design an application to visualize sorting algorithms. Due to time constraints, we took a minimum viable product approach to include the critical functionality needed to demo a usable version of the tool. Some limitations of our project include :

The need for more datasets and larger sizes of our data to stress test our algorithms against. 

Increasing the number of sorting algorithm possibilities to choose from would make this tool more robust by giving the user more flexibility with their analysis. 

The tool currently uses the command line to run the program and make a selection for the data set and column to use. A better user experience would be to make user selections within the tool either via the menu bar or drop-down. 

Further customizations can also be made to the visualizations by drilling deeper into the sorting algorithm and seeing the progress of the data manipulation live. 

Aditya learned how to source the right data to fit the needs of the project goals. He quickly ran into some issues with data types the algorithms would be able to process, so the team needed to filter for integer-specific data. Aditya was also able to further develop his git skillset with a better understanding of leveraging branching strategy to collaborate with other software developers on the team. With further time available to spend on this codebase, future use cases could be to release this as an open source project to help other developers learn. 

Dmitrii learned the power of the Typer library and found a love for building applications utilizing a command line interface. Dmitrii was able to get into the mindset of a user to creatively find pain points that a user would encounter. He was then able to build in informative error handling messages to improve the user experience. The results of this tool were very informative; In fact, Dmitrii believes he will run similar algorithms and visually compare datasets on the job once he graduates from Northeastern during his solution evaluation process. 

Mariah learned how to use the plotly library to depict insightful visuals based on the data that was collected. She also discovered unique ways to make an interactive chart that responds to user clicks by slicing through the data. Mariah’s research enabled her to develop a way to parallelly compute and display sorting results. This is a fantastic project that can be highlighted as part of a personal portfolio to be used during the career search and interview process. 

Shriya learned how to work with Pandas data frames to manipulate data and pass around column-based sets across the application. She also learned how to parse the csv files and read in key data that needed to be stored. Moreover, she utilized the PyGame animation package of Python to create the visualizations of various sorting algorithms which helped in achieving another milestone for this project. She hopes that the visual aspects help the user get a basic understanding of how the algorithm works after reading up on basic documentation. She aspires to eventually integrate more algorithms into her code base and turn it into an open learning platform for all students looking for a good resource to learn about algorithms.  Shriya is passionate about research at Northeastern and this is a great example of a project that can be further advanced by working with a professor at the school. 

 
