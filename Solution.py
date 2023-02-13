from random import shuffle, seed
from time import time
from math import ceil
import pandas as pd

NUM_OF_COLS = 8

def RTC_Encrypt(P, K):
    """"Takes a plaintext and a key of length 8. Retruns a ciphertext using Row Transposition Cipher (RTC) text"""
    #calulate number of rows needed
    numOfRows = ceil(len(P)/NUM_OF_COLS)
    
    print("The number of characters to be encrypted is: ", len(P), "\n\n")
    print("The number of rows in ecryption function: ", numOfRows, "\n\n")

    PlainRect = [['!' for i in range(NUM_OF_COLS)] for j in range(numOfRows)]
    
    #Fill the rectangle with the plaintext
    colIndex = 0
    rowIndex = 0
    for character in P:
        if colIndex == NUM_OF_COLS:
            colIndex = 0
            rowIndex += 1
        PlainRect[rowIndex][colIndex] = character

        colIndex += 1
    
    
    #Convert 2D list to pandas Dataframe to do column swapping
    plainDF = pd.DataFrame(PlainRect, columns=[1, 2, 3, 4, 5, 6, 7, 8])
    
    print('The Plaintext rectangle is: \n')
    print(plainDF.to_string(index=False, header=False), '\n\n')

    #Reorder the columns based on the key
    cipherDF = plainDF.reindex(columns=K)

    
    print('The Ciphertext rectangle is: \n')
    print(cipherDF.to_string(index=False, header=False, ), '\n\n')

    #Construct Cipher Text string and return it

    cipherText = ''
    
    for row in cipherDF.values.tolist():
        cipherTemp = ''.join(row)
        cipherText = cipherText +cipherTemp
    

    return cipherText


def RTC_Decrypt(C, K):
    """"Takes cipher text and returns plaintext after decrypting using Row Transposition Cipher (RTC)"""
    
     #calulate number of rows needed
    numOfRows = ceil(len(C)/NUM_OF_COLS)
    print("The number of characters in to be decrypted: ", len(C), "\n\n")
    print("The number of rows in decryption function: ", numOfRows, "\n\n")
    cipherRect = [['0' for i in range(NUM_OF_COLS)] for j in range(numOfRows)]


    #Reorder the Cipher
    colIndex = 0
    rowIndex = 0
    for character in C:
            cipherRect[rowIndex][K[colIndex]-1] = character
            colIndex += 1
            if colIndex == NUM_OF_COLS:
                colIndex = 0
                rowIndex += 1


    #Convert 2D list to pandas Dataframe to do column swapping and column filling
    decryptedDF = pd.DataFrame(cipherRect)

    print('The decrypted text rectangle is: \n')
    print(decryptedDF.to_string(index=False, header=False, ), '\n\n')


    #Construct decrypted text and return it
    decryptedText = ''
    for row in decryptedDF.values.tolist():
        decryptedTemp = ''.join(row)
        decryptedText = decryptedText + decryptedTemp
    
    return decryptedText

    

#Take plain text from user
while(True):
    plainIn = input("Please Enter The text you want to encrypt\n**You sentence should be above 100 characters**\nInput: ")
    #Check if plain text is above 100char and has no \n
    if len(plainIn) >= 100 or '\n' in plainIn:
        break
    print("Please write a sentence longer than 100 characters that has no newlines")
    #If not, start over


#Generate a random key consisting of 8 number with 1-8
key = []
for num in range(1, NUM_OF_COLS+1):
    key.append(num)
seed(time())
shuffle(key)

print('\n\nThe key is: \n')
print(key, '\n\n')

print('\n\nThe number of Columns is: ', NUM_OF_COLS, '\n\n')



#Pass plain text and Key to RTC_Encrypt
cipherText = RTC_Encrypt(plainIn, key)
print('Your ciphertext is:\n')
print(cipherText, '\n\n')


#Pass Cipher text to Decrypt Function
decryptedText = RTC_Decrypt(cipherText, key)
print('Your decrypted text is:\n')
print(decryptedText, '\n\n')

if decryptedText.replace('!', '') == plainIn:
    print("\n\nThe decrypted text equals the plaintext. The process is correct\n\n")
else:
    print("\n\nThe decrypted text does not equal the plaintext. In case your error had'!', you can check the correctness manually. Otherwise, sorry, an error may have happened\n\n")

#YAZAN RIHAN