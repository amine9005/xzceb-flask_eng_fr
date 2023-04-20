import unittest
from translator import french_to_english,english_to_french

class Test_English_To_French(unittest.TestCase):
    def test(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertEqual(english_to_french("Good luck"),'Bonne chance')
        
        self.assertEqual(english_to_french(''),'')
        self.assertEqual(english_to_french(None),'')
        self.assertEqual(english_to_french(123456789),'')
        
        self.assertNotEqual(english_to_french("Hello"),"Hello")
        self.assertNotEqual(english_to_french("Good luck"),"Good luck")

class Test_French_To_English(unittest.TestCase):
    def test(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertEqual(french_to_english("Bonne chance"),'Good luck')
        
        self.assertEqual(french_to_english(''),'')
        self.assertEqual(french_to_english(None),'')
        self.assertEqual(french_to_english(123456789),'')
        
        self.assertNotEqual(french_to_english("Bonjour"),"Bonjour")
        self.assertNotEqual(french_to_english("Bonne chance"),"Bonne chance")
        

unittest.main()