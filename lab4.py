# 1. Program to find the maximum and minimum elements in a list:
def find_max_min(lst):
    maximum = lst[0]
    minimum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return maximum, minimum

# Example usage
numbers = [3, 1, 9, 7, 2, 6]
max_num, min_num = find_max_min(numbers)
print("Maximum:", max_num)
print("Minimum:", min_num)

#2. Program to sort a list in ascending order without using sort():
def sort_list(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                # Swap the elements
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

# Example usage
numbers = [5, 2, 8, 1, 3]
sorted_list = sort_list(numbers)
print("Sorted list:", sorted_list)

#3. Program to remove duplicates from a list and print unique elements:
def remove_duplicates(lst):
    unique_elements = []
    for item in lst:
        if item not in unique_elements:
            unique_elements.append(item)
    return unique_elements

# Example usage
numbers = [4, 2, 4, 1, 3, 2, 1, 5]
unique_numbers = remove_duplicates(numbers)
print("Unique elements:", unique_numbers)

##4. Program to find common elements between two lists:
def find_common_elements(lst1, lst2):
    common_elements = []
    for item in lst1:
        if item in lst2 and item not in common_elements:
            common_elements.append(item)
    return common_elements


