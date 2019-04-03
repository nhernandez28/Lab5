"""
CS2302
Lab5
Purpose: gain expirience with hash tables using chaining
Created on Mon Mar 25, 2019
Olac Fuentes
@author: Nancy Hernandez
"""

import time
import numpy as np
import Lab3
import WordClass
import ProfFile as HTC

#creates BST
def CreateBSTList():
    timeStart = time.time()
    #reads file
    File1 = open('glove.6B.50d.txt', encoding = 'utf-8')
    tree = None
    numWords = 0
    
    for line in File1:
        numWords += 1
        #splits file
        lineSplit = line.split()
        tempText = lineSplit.pop(0)
        #embeddings
        arrays = np.array(lineSplit)
        temp = WordClass.Word(tempText, arrays)
        #creates BST
        Lab3.Insert(tree,temp)
        
    #Lab3.Delete(tree,temp)
    
    #Times how long it takes to read
    timeEnd = time.time() - timeStart
     
    #height
    print('Height: ', Lab3.MaxHeight(tree))
    #Running time
    print('Running time for binary search tree construction: ', timeEnd, 'seconds')
    #number of nodes
    print('Number of Nodes: ', numWords)
        
    
#creates hash table
def CreateHT():
    timeStart = time.time()
    
    #reads file
    File1 = open('glove.6B.50d.txt', encoding = 'utf-8') 
    initialTS = 31 
    HTTable = HTC.HashTableC(initialTS)
    #Initial table size
    print('Initial Table Size: ', initialTS)
    
    NumWords = 0
    
    for line in File1:
        #counts number of nodes
        NumWords += 1
        #splits file
        lineSplit = line.split()
        tempText = lineSplit.pop(0)
        arrays = np.array(lineSplit)
        #creates HT
        tempWord = WordClass.Word(tempText, arrays)
        HTC.InsertC(HTTable, tempWord, len(tempWord.Item))
        
        
    timeEnd = time.time()
    #Final table size
    print('Final table size: ', len(HTTable.item))
    #time for HT
    print('Time: ', timeEnd - timeStart, 'seconds')
    print('Percent of empty lists: ', PercentageE(HTTable))
    #number of nodes
    print('Number of Nodes: ', NumWords)
    print('Standard deviation of the lengths of the lists: ', StanD(HTTable))
    
    #Gets similarities
    print('Word similarities found:', ReadFileTwoHT(HTTable))
    


#Similarities for HT
def ReadFileTwoHT(HTTable):
    timeStart = time.time()
    
    #Read file 2 here
    File2 = open('file2.txt', encoding = 'utf-8') 
    
    #reads file
    for line in File2:
        #print(line)
        lineSplit = line.split()
        #split both words
        Word1 = lineSplit[0]
        Word2 = lineSplit[1]
        #searches for both words in file1
        Word1_2 = HTC.FindC(HTTable, Word1)
        Word2_2 = HTC.FindC(HTTable, Word2)
       
    timeEnd = time.time() - timeStart
    
    print('Similarities ', lineSplit, ' are', CosDist(Word1_2.item,Word2_2.item), 4)
    print('Running time for hash table query processing: ', timeEnd)
    

def CosDist(w1, w2):
    #Gets dot product
    dProduct = []
    dProduct = np.dot(w1)
    
    #For first word
    for i in w1:
        dProduct[i] = w1[i]*w2[i]
    total = 0
    
    #for second word
    for i in w1:
        total += dProduct[i]
        
    #calculates magnitude
    magnitude1 = np.linalf.norm(w1.arrays)
    magnitude2 = np.linalf.norm(w2.arrays)
    
    #gets final total
    total = total // (magnitude1 * magnitude2)
    
    return total


#Reads file two
def ReadFileTwo(tree):
    timeStart = time.time()
    
    #Read file 2 here
    File2 = open('file2.txt', encoding = 'utf-8') 
    
    for line in File2:
        #splits file
        lineSplit = line.split()
            
        #Splits both words
        Word1 = lineSplit[0]
        Word2 = lineSplit[1]
        
        #searches for both words
        Word1_2 = Lab3.Find(tree, Word1)
        Word2_2 = Lab3.Find(tree, Word2)
        print(type(Word1))
        print(Word1_2.item.Item)
        
        #CosDist(Word1_2, Word2_2)
    
    timeEnd = time.time() - timeStart
    print('Running time for binary search tree query processing: ', timeEnd)


#Finds empty percentage in HT
def PercentageE(H):
    empty = 0
    
    for i in range(len(H.item)):
        if len(H.item[i]) < 1:
            empty += 1
    #gets percentage    
    return 100 * empty / len(H.item)
    

#standard Deviation
def StanD(H):
    items = []
    
    #Goes through each item 
    for item in H.items:
        items.append(len(H.item[item]))
    
    #uses python function to obtain standard deviation
    deviation = np.std(items)
    
    return deviation


print('Choose table implementation')
print('Type 1 for binary search tree or 2 for has table with chaining')
userChoice = input('Choice: ')

if userChoice == "1":
    print()
    print('Building binary search tree')
    
    print()
    print('Binary Search Tree Stats:')
    tempTree = CreateBSTList()
    print()
    print('Reading word file to determine similarities')
    print()
    print('Word similarities found: ')
    
    ReadFileTwo(tempTree)
    
    print()
    print('Runing time for binary search tree query processing:')
    
elif userChoice == "2":
    print()
    print('Building hash table with chaining')
    print()
    print('Hash table stats:')
    CreateHT()
    
    print('Final table size: ' )
    print('Load Factor: ')
    
    print('Reading file to determine similarities')
    print()
    
else:
    print('Invalid Selection!')