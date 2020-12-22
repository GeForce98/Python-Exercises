#Quincy Asemota
#Weekly Assignment #6
#Welcome Message

if __name__=="_ _main__":

    flag=True
    while(flag):
        try:
              filename=input("Please enter a filename to be used: ")
              #Opens the input file
              inFile=open(filename,'r')

              #Reads the lines within the file
              lines=inFile.readlines()
              #Creates an empty dictionary to store the words and its count
              wordDict={}
              #For each lines within the file
              for line in lines:
                  #Remove the ending new-line character
                  line=line.strip('/n')
                  #Split each lines at space
                  words=line.split('')
                  #For each word in a line
                  for word in words:
                      #Convert the word tolower case to make it case insensitive
                      word=word.lower()
                      #If the word is not present in the dictionary add it to the existing dictionary
                      #Else increment the count for word
                      if(word not in wordDict) and word!=":":
                          wordDict[word]=1
                      elif word!=":":
                          wordDict[word]+=1

                        #Create a list of tuples of words sorted according to values
                        listofTuples = sorted(wordDict.items(),key=lambda x:x[1],reverse=True)
                        
                        #Iterate over the sorted sequence
                        for elem in listofTuples:
                        print(elem[0],"::", elem[1])

                        inFile.close()
                        flag=False
        except:
            print("I am unable to find the existing file" + filename + "in current path\n")


    
