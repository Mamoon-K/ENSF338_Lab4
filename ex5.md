# Exercise 5 - Reflecting on Measurements

## Question 1: Comparing timeit and repeat

When measuring the execution time of a program, factors that introduce inconsistencies are background processes running 
on the system may interfere with performance, causing fluctuations, and CPU scheduling by the operating system can slow execution.
In Python, garbage collection can create additional variability. 
Additionally, cache effects may improve execution times when a function is repeatedly executed (discussed in class).

The timeit and repeat functions try to handle these issues in different ways.

The timeit.timeit() function runs a given function multiple times, as specified by
the number parameter, and returns the total execution time. This approach helps reduce
measurement noise by averaging over multiple runs, but it does not provide insight into how execution
times vary between different trials.

On the other hand, timeit.repeat() runs multiple independent timing experiments,
each executing the function multiple times. It uses the repeat parameter, and it returns a collection of execution times,
allowing us to analyze variability and detect outliers. This method is particularly useful when system-level noise may
affect performance, as it provides a broader view of execution time distribution.

Choosing between timeit.timeit() and timeit.repeat() depends on the situation -
If execution time is expected to be stable and a single quick estimate is needed,
timeit.timeit() is appropriate. However, if execution times vary and a more detailed statistical 
analysis is required, timeit.repeat() is the better choice because it allows for a better
understanding of performance trends over multiple runs.

## Question 2: Choosing the Right Statistic

When working with timeit.timeit(), the most appropriate statistic to use is the average.
Since this function returns a single aggregated value, averaging helps smooth out fluctuations
caused by CPU scheduling, background processes, or other sources of noise.

For timeit.repeat(), different statistics can be applied depending on the analysis goal.
The minimum execution time is useful when identifying best-case performance because it filters out
interruptions caused by external factors like system resource allocation.
The average provides a more general performance trend by considering all recorded execution times.
The maximum value can highlight worst-case scenarios, which is important when considering performance outliers.



