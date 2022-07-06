#************************************** Update Values in the Dictionaries and List *****************************************

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

# ************** question 1a ******************
#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

x[1][0] = 15
print(x)

# ************** question 2a ******************
# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students[0]['last_name'])
print(students[0]['first_name'])

# ************** question 3a ******************
# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

# ************** question 4a ******************
#Change the value 20 in z to 30
z[0]['y'] = 30
print(z)



#************************************** Iterate Through a List of Dictionaries *****************************************

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


# should output: (it's okay if each key-value pair ends up on 2 separate lines;
def iterateDictionary(list):
    for i in range(len(list)):
        for key, value in list[i].items():
            print(f"{key}, -, {value}")
iterateDictionary(students)

# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel




# ****************************************** Get Values From a List of Dictionaries **************************************
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, 
# the function prints the value stored in that key for each dictionary.
#  For example, iterateDictionary2('first_name', students) should output:

def iterateDictionary2(key,list):
    for i in range(len(list)):
        print(list[i][key])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)
print("*************************************************")


#*************************************** Iterate Through a Dictionary with List Values ************************************
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
# prints the name of each key along with the size of its list,
# and then prints the associated values within each key's list. 
# For example:
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dict):
    for key in dict:                        # loop key dictionary location & instructors
        print(len(dict[key]), key.upper())  # print the length of key, for second key 
        for i in range(len(dict[key])):     # loop thru each key inside of locations
            print(dict[key][i])             # print to see dictionary key index of each 
printInfo(dojo)

# output:
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
