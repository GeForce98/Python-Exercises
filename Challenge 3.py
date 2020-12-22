#Quincy Asemota
#Weekly Assignment 5
#Write a program that counts the letters in a given string and then display the letter count in order from high to low.

#Welcome Message
print("This program will count the letters in a given string")
print("It will display the letter count in order from highest to lowest")

#Prompt user to input a string
input_str=input("Please enter a string:")

#This stores the character count
char_count={}

#Used for iterating through every character in the user inputted string.
for c in input_str:

    #Used for changing the characters to upper case
    c=c.upper()

    #Checking the character is in dictionary or not
    if c not in char_count:
        char_count[c]=1
    else:
    #This increments the character value/count by one
        char_count[c]+=1

#This list of key,value pairs from built in dictionary
        lst=list(char_count.items())

#Sorting the list by values, if a few letters have the same count,
#Sorts the characters in alphabetical order
lst.sort(key=lambda x:(-x[1],x[0]))

#Character and Count
for k,v in lst:

    print('{0}-{1}'.format(k, v))

