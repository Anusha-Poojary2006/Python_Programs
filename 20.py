#function to remove spaces from the string removeSpaces

def removeSpaces(string):
    output=''
    for char in string:
        if char!=" " and char!='\t' and char!='\n':
            output=output+char
    print(output)

input=input("Enter a input:")
removeSpaces(input)