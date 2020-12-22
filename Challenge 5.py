#Quincy Asemota
#Weekly Assignment 7

import csv

# method to count words from a string
def countWord(line):
    #split the string in words and count using len() method
    return (len(line.split()));

#display the program's welcome messages
print("This program is designed to take a CSV file as input from user and displays the ouput:")
print("\t1. This part of the program counts the number of headlines in each category")
print("\t2. This part of the program counts the number of words in each category")
print("\t3. This part of the program lists the categories with number of titles and word count")
print("\t4. This part of the program sorts the category list based on the number of titles from high to low")

# prompt user to enter input file
print("Please enter the file name: ")
filename = input()

newsDict = {} #dictionary for counting # of title
wordsDict = {} #dictionary for counting # of words

# TRY/EXCEPT Structure - for handling file reading error
try:
    #open the file in read mode
    with open(filename, 'r') as file:
      # This reads hte lines from NYT.csv file
      reader = csv.reader(file)
      next(reader)   

      # for loop through all the lines
      for line in reader:
        if (line[2] in newsDict):
         #if key exist in dictionary, increment the value by 1
         newsDict[line[2]] = newsDict[line[2]] + 1
        else :
         # if key not exist in dictionary, set it by 1 to start counting
         newsDict[line[2]] = 1

        if (line[2] in wordsDict):
         # if key exist in word count dictionary, get the value and add the count of word in title and subtitle
         wordsDict[line[2]] = wordsDict[line[2]] + countWord(line[0]) + countWord(line[1])
        else :
         #if key exist in word count dictionary, add the count of word in title and subtitle and set
         wordsDict[line[2]] = countWord(line[0]) + countWord(line[1])
    print("%-15s | %-15s | %-15s" % ("Category", "# of titles", "# of words"))
    # sort the values using lambda function and reverse the result to get high to low
    for key in sorted(newsDict.items(), key = lambda x: x[1], reverse = True):
      print("%-15s | %-15d | %-15d" % (key[0], newsDict[key[0]], wordsDict[key[0]]))

except OSError as err:
  print("Failed to open the file. Please try again. Error detail: {0}".format(err))
