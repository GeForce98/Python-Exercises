#Quincy Asemota
#Weekly Assignment 4
#Write a program for a basic string extraction

#This program is designed to perform a basic string extraction.
#Prompts user to enter a message/string
string=input("Enter a String: ")
#Used to find length of the string
n= len(string)
#For loop that will iterate until the end of the string entered by user.
for i in range(n):
    #Checks the string to make sure every character is apart of the alphabet
    if string[i].isalpha() or string[i]==' ':
        print(string[i].lower(),end ="")
