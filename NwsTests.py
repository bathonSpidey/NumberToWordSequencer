# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 22:11:12 2020

@author: batho
"""

import unittest
import NumberToWordSequencer as nws


class TestStringMethods(unittest.TestCase):

    def test_individualCharacter(self):
        wordList=nws.GenerateSequences("1123")
        self.assertEqual(wordList[0],"aabc")
    
    def test_firstTwoLettersCombined(self):
        wordList=nws.GenerateSequences("1123")
        self.assertEqual(wordList[1], "kbc")
    
    def test_nextTwoLettersCombined(self):
        wordList=nws.GenerateSequences("1123")
        self.assertEqual(wordList[2], "alc")
    
    def test_lastTwoLettersCombined(self):
        wordList=nws.GenerateSequences("1123")
        self.assertEqual(wordList[3],"aaw")
        
    def test_lastTwoLettersCombined(self):
        wordList=nws.GenerateSequences("1123")
        self.assertEqual(wordList[4],"kw")
    
    def test_specialCharacterWordsShouldBeRemoved(self):
        wordList=nws.GenerateSequences("11231")
        self.assertEqual(len(wordList),5)

if __name__ == '__main__':
    unittest.main()