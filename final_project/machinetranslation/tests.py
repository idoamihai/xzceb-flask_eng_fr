import unittest
import translator

class TestFrenchToEnglish(unittest.TestCase):

    def test_frenchToEnglishHello(self):
        frenchText = 'bonjour'
        transatedText = translator.french_to_english(frenchText)
        self.assertEqual(transatedText, "Hello")

    def test_frenchToEnglishGoodbye(self):
        frenchText = 'au revoir'
        transatedText = translator.french_to_english(frenchText)
        self.assertEqual(transatedText, "Goodbye")

    def test_translateNull(self):
        frenchText = ''
        with self.assertRaises(Exception):
            translator.french_to_english(frenchText)

class TestEnglishToFrench(unittest.TestCase):

    def test_englishToFrenchHello(self):
        englishText = 'hello'
        transatedText = translator.english_to_french(englishText)
        self.assertEqual(transatedText, "Bonjour")

    def test_englishToFrenchGoodbye(self):
        englishText = 'goodbye'
        transatedText = translator.english_to_french(englishText)
        self.assertEqual(transatedText, "Au revoir")
        
    def test_translateNull(self):
        englishText = ''
        with self.assertRaises(Exception):
            translator.english_to_french(englishText)

if __name__ == '__main__':
    unittest.main()