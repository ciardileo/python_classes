# this code below, catches by the filter(), the biggest values in a list

numbers = [10, 2, 4, 10, 23, 21, 23, 1, 1]
numbers.sort(reverse=True)  # sort by the decreasing order
print(list(filter(lambda x: True if x == max(numbers) else False, numbers)))

# the filter applies a function for each element in a list and will return it to a new list if the function returns True
