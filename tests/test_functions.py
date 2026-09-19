import unittest
from functions import generate_conjugations

class TestConjugation(unittest.TestCase):

    def test_active_generation(self):
        result = generate_conjugations("b*l", "p", "2", "m", "s", "a")
        self.assertTrue(result)

    def test_passive_generation(self):
        result = generate_conjugations("b*l", "p", "2", "m", "s", "p")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()