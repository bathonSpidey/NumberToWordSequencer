# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 22:50:40 2020

@author: batho
"""

import re

def GenerateSequences(sequence):
    generatedWordList=[]
    generatedWordList.append(IndividualCharacterCombination(sequence))
    generatedWordList= SlideTwoAtATime(sequence, generatedWordList)
    generatedWordList.append(CombineTwoAtATime(sequence))
    filteredList=FilterValidStrings(generatedWordList)
    return filteredList

def SlideTwoAtATime(sequence, generatedList):
    for i in range(len(sequence)-1):
        if i ==0:
            firstHalf=chr(int(sequence[i:i+2])+96)
            firstHalf+=IndividualCharacterCombination(sequence[2:])
            generatedList.append(firstHalf)
        elif i==len(sequence)-2:
            lastHalf=IndividualCharacterCombination(sequence[:i])
            lastHalf+=chr(int(sequence[i:i+2])+96)
            generatedList.append(lastHalf)
        else:
            firstSequence=IndividualCharacterCombination(sequence[:i])
            firstSequence+=chr(int(sequence[i:i+2])+96)
            firstSequence+=IndividualCharacterCombination(sequence[i+2:])
            generatedList.append(firstSequence)
    return generatedList
            
def IndividualCharacterCombination(sequence):
    word=""
    for i in sequence:
        word+=chr(int(i)+96)
    return word

def CombineTwoAtATime(sequence):
        word=""
        for i in range(0,len(sequence),2):
            word+=chr(int(sequence[i:i+2])+96)
        return word

def FilterValidStrings(generatedWordList):
    for word in generatedWordList:
        if re.findall('[^A-Za-z]',word):
            generatedWordList.remove(word)
    return generatedWordList