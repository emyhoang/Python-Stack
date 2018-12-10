# 1.Biggie Size - Given an array, write a function that changes all positive numbers 
# in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array,
#  changed to [-1, "big", "big", -5].
def makeItBig(list):
  for i in range(0,len(list),1):
    if (list[i] >= 0):
      list[i] = "big"
  return list


# 2.Count Positives - Given an array of numbers, create a function to replace last value 
# with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3]
#  and returns it.  (Note that zero is not considered to be a positive number).
def count_positives(my_list):
  count=0
  for i in range(0,len(my_list),1):
    if my_list[i] >= 0:
      count += 1
  my_list[len(my_list) -1] = count
  return my_list



# 3.SumTotal - Create a function 
# that takes an array as an argument and
#  returns the sum of all the values in the array.
# 
#   For example sumTotal([1,2,3,4]) should return 10
def sum_total(my_list):
  sum = 0
  for i in range(0,len(my_list),1):
    sum+= my_list[i]
  return sum


# 4.Average - Create a function
#  that takes an array as an argument 
# and returns the average of all the values in the array.
#   
# For example multiples([1,2,3,4]) should return 2.5
def average(my_list):
  sum = 0 
  for i in range(0,len(my_list),1):
    sum += my_list[i]
  return sum/len(my_list)

# 5.Length - Create a function 
# that takes an array as an argument 
# 
# and returns the length of the array.
# 
#   For example length([1,2,3,4]) should return 4
def length(list_of_numbers):
  return len(list_of_numbers)

# 6.Minimum - Create a function
#  that takes an array as an argument 
# and returns the minimum value in the array. 
# If the passed array is empty, have the function return false.  
# For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
def minimum(arr):
  min = arr[0]
  for i in range(0,len(arr)):
    if arr[i] < min:
      min = arr[i]
  if arr == []:
    return false
  return min

# 7.Maximum - Create a function
#  that takes an array as an argument and 
# returns the maximum value in the array.  
# If the passed array is empty, have the function return false. 
#  
# For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.
def maximum(arr):
  max = arr[0]
  for i in range(0,len(arr)):
    if arr[i] > max:
      max = arr[i]
  if arr == []:
    return false
  return max

# 8.UltimateAnalyze - Create a function 
# that takes an array as an argument and 
# returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.
def ultimate_analyze(arr):
  dictionary = {
    sum_total: sum_total(arr),
    avg : average(arr),
    min : minimum(arr),
    max: maximum(arr),
    length: length(arr)
  }
  return dictionary


# 9.ReverseList - Create a function 
# that takes an array as an argument and 
# return an array in a reversed order.  
# Do this without creating an empty temporary array. 
#  
# For example reverse([1,2,3,4]) should return [4,3,2,1]. 
# This challenge is known to appear during basic technical interviews.
def reverse_list(arr):
  
  return arr


