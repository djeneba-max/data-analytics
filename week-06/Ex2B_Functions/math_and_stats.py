import random
import math
import statistics

# Starting variables
vals_1_100 = range(1,100)  # range() generates a sequence of numbers. The last number specified in the parentheses is excluded.
vals_sample = random.sample(vals_1_100, 75)  # subset. random.sample() accepts a sequence, such as range. 
vals_choices = random.choices(vals_1_100, k = 200)  # superset. random.choices() accepts a sequence too. # Unlike random.sample(), it allows repeated selections.
radius = random.randint(3,10)
pi = math.pi




# _Experimenting with a subset of integers 1-100: 
# Sum of the 75 sampled values
total = sum(vals_sample)  # built-in function

# Average of the 75 sampled values
average = statistics.mean(vals_sample)  # statistics function

# Median of the 75 sampled values
median = statistics.median(vals_sample)  # statistics function





# _Experimenting with a superset of 200 values, integers 1-100:
# Average of the 200 values
average_200 = statistics.mean(vals_choices)

# Median of the 200 values
median_200 = statistics.median(vals_choices)

# Mode of the 200 values
mode_200 = statistics.mode(vals_choices)

# Standard deviation of the 200 values
std_dev = statistics.stdev(vals_choices)

# Variance of the 200 values
variance = statistics.variance(vals_choices)
# stdev() and variance() are statistics functions applied to a sample.
# There are also pstdev() and pvariance() used for an entire population.





# _Modeling a random circle:
# Area of a random circle
area = pi * radius ** 2

# Round the area up to the nearest integer
area_up = math.ceil(area)

# Round the area down to the nearest integer
area_down = math.floor(area)





# Display the results
print("_Experimenting with a subset of integers 1-100:")
print("Sum of 75 sample values from 1 to 100:", total)
print("Average of 75 sample values:", average)
print("Median of 75 sample values:", median)

print('\n')   # print('\n') adds two line breaks between sections.
# We can put \n before the next section's text to have only one line break.

print("_Experimenting with a superset of 200 values, integers 1-100:")
print("Average of 200 values:", average_200)
print("Median of 200 values:", median_200)
print("Mode of 200 values:", mode_200)
print("Standard deviation of 200 values:", std_dev)
print("Variance of 200 values:", variance)

print('\n')

print("_Modeling a random circle:")
print(f"Radius = {radius}, area = {area_up} (rounded up to the nearest integer)")
print(f"Radius = {radius}, area = {area_down} (rounded down to the nearest integer)")