introString=input("enter the sentence: ")
characterCount=0
wordCount=1
for i in introString:
    characterCount=characterCount+1
    if i==' ':
        wordCount=wordCount+1
print("number of words in the sentence is")
print(wordCount)
print("number of characters in the sentence is")
print(characterCount)


