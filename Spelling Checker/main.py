# importing textblob library

from textblob import TextBlob  

t = 1

while t:

    # for incorrect spelling

    a = input("Enter the word to be checked:- ")    

    #printing original text

    print("original text: "+str(a))     

    b = TextBlob(a)  #correcting the text

    # prints the corrected spelling

    print("corrected text: "+str(b.correct()))

    t = int(input("Try Again? 1 : 0 "))