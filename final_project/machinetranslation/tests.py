import unittest
import translator

class TestFrenchToEnglish(unittest.TestCase):

    def test_frenchToEnglishHello(self):
        frenchText = 'Bonjour'
        transatedText = translator.french_to_english(frenchText)
        self.assertEqual(transatedText, "Hello")

    def test_frenchToEnglishGoodbye(self):
        frenchText = 'Au revoir'
        transatedText = translator.french_to_english(frenchText)
        self.assertEqual(transatedText, "Goodbye")

    def test_translateNull(self):
        frenchText = ''
        with self.assertRaises(Exception):
            translator.french_to_english(frenchText)

class TestEnglishToFrench(unittest.TestCase):

    def test_englishToFrenchHello(self):
        englishText = 'Hello'
        transatedText = translator.english_to_french(englishText)
        self.assertEqual(transatedText, "Bonjour")

    def test_englishToFrenchGoodbye(self):
        englishText = 'Goodbye'
        transatedText = translator.english_to_french(englishText)
        self.assertEqual(transatedText, "Au revoir")
        
    def test_translateNull(self):
        englishText = ''
        with self.assertRaises(Exception):
            translator.english_to_french(englishText)

if __name__ == '__main__':
    unittest.main()
