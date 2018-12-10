# 1.Countdown - Create a function that accepts a number as an input.  
# Return a new array that counts down by one, 
# from the number (as arrays 'zero'th element) down to 0 (as the last element).  
# For example countDown(5) should return [5,4,3,2,1,0].
def count_down(num):
  new_list = []
  for i in range(num, 0 , -1):
    new_list.append(i)
  return new_list

# 2.Print and Return - Your function will receive an array 
# with two numbers. Print the first value, and return the second.
def print_return(list):
    print(list[0])
    return list[1]

# 3.First Plus Length - Given an array, return the sum of the first value
#  in the array, plus the array's length.
def first_plus_length(list):
    sum = list[0] + len(list)
    return sum

# 4.Values Greater than Second - Write a function that accepts any array,
# and returns a new array with the array values that are greater than its 
# 2nd value.  Print how many values this is.  If the array is only one 
# element long, have the function return False
def values_greater_than_second(list):
    new_list = []
    for i in range (len(list)):
        if list[i] > list[1]:
            new_list.append(list[i])
    print(len(new_list))
    if len(new_list) == 1:
        return false
    return new_list

# 5. This Length, That Value - Write a function called lengthAndValue which 
# accepts two parameters, size and value. This function should take two numbers 
# and return a list of length size containing only the number in value. 
# For example, lengthAndValue(4,7) should return [7,7,7,7]
def length_and_value(size,value):
    new_list = []
    for i in range(0,size,1):
        new_list.append(value)
    return new_list