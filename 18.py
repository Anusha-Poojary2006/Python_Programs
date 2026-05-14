#function to get count of words in the string getCountWords

def getCountWords(string):
    wordlist=string.strip().split(" ")
    print(len(wordlist))
   


string=input("Enter a string:")
getCountWords(string)
