#Python program to get dictionary keys and values as list

def getListkeys(dict):
    return list(dict.keys())

def getListValues(dict):
    return list(dict.values())

#Driver program
dict = {'C': 1, 'C++': 8, 'Java': 6, 'JavaScript': 6, 'PERL': 4, 'Python': 6}
    

print ("**** Separator ****")

#Entire dictionary
print (dict)    #print the dictionary as is

print ("**** Separator *****")

#Only keys and only values
print (dict.keys())     # print only the keys from the dictionary
print (dict.values())   # print only the values from the dictionary

print ("**** Separator *****")

#Only keys, better syntax
for i in dict:
    print(i)

print ("**** Separator *****")

#Only values, better syntax
for i in dict:
    print(dict[i])

print ("**** Separator *****")

#Now only keys and only values, but after converting into lists
print (getListkeys(dict))       # now print the keys of the dictionary as a list
print (getListValues(dict))     #first print the values in the dictionary as a list