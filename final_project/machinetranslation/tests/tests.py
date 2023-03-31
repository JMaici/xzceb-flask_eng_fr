"""
Unit tests for translation functions
"""

import unittest
from translator import english_to_french, french_to_english

class TestTranslationFunctions(unittest.TestCase):
    def test_english_to_french(self):
        """
        Tests the english_to_french function with different inputs
        """
        # Test null input
        self.assertIsNone(english_to_french(None))
        
        # Test translation of 'Hello'
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        
    def test_french_to_english(self):
        """
        Tests the french_to_english function with different inputs
        """
        # Test null input
        self.assertIsNone(french_to_english(None))
        
        # Test translation of 'Bonjour'
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()
