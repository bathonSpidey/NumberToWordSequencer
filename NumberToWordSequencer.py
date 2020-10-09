# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 22:50:40 2020

@author: batho
"""

import unittest

def GenerateSequences(sequence):
    generatedWordList=[]
    word=IndividualCharacterCombination(sequence)
    generatedWordList.append(word)
    firstTwoCombined=chr(int(sequence[:2])+96)
    firstTwoCombined+=IndividualCharacterCombination(sequence[2:])
    generatedWordList.append(firstTwoCombined)
    middleTwoCombined=IndividualCharacterCombination(sequence[0])
    middleTwoCombined+=chr(int(sequence[1:3])+96)
    middleTwoCombined+=IndividualCharacterCombination(sequence[3])
    generatedWordList.append(middleTwoCombined)
    return generatedWordList

def IndividualCharacterCombination(sequence):
    word=""
    for i in sequence:
        word+=chr(int(i)+96)
    return word
    
        






class TestStringMethods(unittest.TestCase):

    def test_individualCharacter(self):
        wordList=GenerateSequences("1123")
        self.assertEqual(wordList[0],"aabc")
    
    def test_firstTwoLettersCombined(self):
        wordList=GenerateSequences("1123")
        self.assertEqual(wordList[1], "kbc")
    
    def test_nextTwoLettersCombined(self):
        wordList=GenerateSequences("1123")
        self.assertEqual(wordList[2], "alc")
            
if __name__ == '__main__':
    unittest.main()