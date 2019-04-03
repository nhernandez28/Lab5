# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 17:37:07 2019

@author: Nance
"""

class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.item = []
        for i in range(size):
            self.item.append([])
        
def InsertC(H,k,l):
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    b = h(k,len(H.item))
    H.item[b].append([k,l]) 
   
def FindC(H,k):
    # Returns bucket (b) and index (i) 
    # If k is not in table, i == -1
    b = h2(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0].Item == k:
            #return b, i, H.item[b][i][1]
            return H.item[b][i][1]
    return b, -1, -1
 
def LoadFactor(H):
    items = countItems(H)
    return items/len(H.item)
    
def countItems(H):
    tot =0
    for i in range(len(H.item)):
        tot += len(H.item[i])
    return tot


def h(s,n):
    #hashes word node
    r = 0
    for c in s.Item:
        r = (r*n + ord(c))% n
    return r

def h2(s,n):
    #hashes string
    r = 0
    for c in s:
        r = (r*n + ord(c))% n
    return r

'''H = HashTableC(11)
A = ['data','structures','computer','science','university','of','texas','at','el','paso']
for a in A:
    InsertC(H,a,len(a))
    print(H.item)

for a in A: # Prints bucket, position in bucket, and word length
    print(a,FindC(H,a))'''
 