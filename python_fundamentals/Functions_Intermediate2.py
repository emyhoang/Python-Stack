1. Given

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# How would you change the value 10 in x to 15?  Once you're done x should then be 
# [ [5,2,3], [15,8,9] ].  

# - grab the second array in the array and set the firt element to the value to 15.
x[1][0]=15

# How would you change the last_name of the first student from 'Jordan' to "Bryant"?
students[0]['last_name']= "Bryant"

# For the sports_directory, how would you change 'Messi' to 'Andres'?
sports_directory['soccer'][0] = "Andres"

# For z, how would you change the value 20 to 30?
z[0]['y'] = 30

# 2.Create a function that given a list of dictionaries, 
# it loops through each dictionary in the list and 
# prints each key and the associated value.  
# For example, given the following list:
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def print_key_values(list_of_dictionaries):
  
  for i in range (0,len(list_of_dictionaries)):
      print(list_of_dictionaries[i]['first_name'], list_of_dictionaries[i]['last_name'])

print_key_values(students)

# 3. Create a function that given a list of dictionaries and a key name, 
# it outputs the value stored in that key for each dictionary.  

# For example, iterateDictionary2('first_name', students) should output
# Michael
# John
# Mark
# KB
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterate_dictionary(list_of_dictionaries, key_names):
  for person in list_of_dictionaries:
      print (person[key_names])
    
iterate_dictionary(students,'first_name')

# say that
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# Create a function 
def dojo_overview():
# that prints the name of each location 
  for i in (len(list_of_dictionaries)):
      print(list_of_dictionaries[i]]
# and also how many locations the Dojo currently has. 
#     count = 0
#     count += 1
#     print("locations" = count) 
# #  Have the function also print the name of each instructor 
# print(dojo.'instructors')
#  and how many instructors the Dojo currently has.  
 
#  For example, printDojoInfo(dojo) should output
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon