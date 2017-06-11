#UserPassword cracker
#ord() is used for obtaining ascii value
#chr() is used for obtaining the character value back
import KMP

def passwordCracker(userPasswords,templatePassword):
    hashTable=[None]*26  #creating hashTable

    #Initailize the hashTable
    for i in range(26):
        hashTable[i]=0
        

    print("\n")    
    for i in range(len(userPasswords)):
        temp=userPasswords[i]
        for j in range(len(temp)):
            index=ord(temp[j].lower())-97
            hashTable[index]=hashTable[index]+1
            

    print("\n")
    for i in range(len(templatePassword)):
        index=ord(templatePassword[i])-97
        hashTable[index]=hashTable[index]-1
        
  
    print("\n")
    #checking the value of HashTable
    for i in range(26):        
        if hashTable[i]!= 0:
            print("Wrong Password")

 

    
#Driver Function
userPasswords=["because", "can", "do", "must", "we", "what","we","we"] #declaring as tuple so that they cannot be changed
templatePassword="wedowhatwemustbecausewecan"
passwordCracker(userPasswords,templatePassword)                  
