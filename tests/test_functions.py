import unittest
from functions import generate_conjugations

class TestConjugation(unittest.TestCase):

    def test_passive_generationktb(self):
        result = generate_conjugations("ktb", "p", "2", "m", "s", "p")
        self.assertTrue(result)

    def test_passive_generationxrj(self):
        result = generate_conjugations("xrj", "p", "2", "m", "s", "p")
        self.assertTrue(result)

    def test_passive_generationrbT(self):
        result = generate_conjugations("rbT", "p", "2", "m", "s", "p")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()