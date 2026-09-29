import unittest
from functions import generate_conjugations

class TestConjugation(unittest.TestCase):

    def test_generate_conjugations(self):
        generated_forms = generate_conjugations(questions=100)
        if len(generated_forms) != 100:
            self.fail(f"Expected 100 generated forms, but got {len(generated_forms)}")

if __name__ == "__main__":
    unittest.main()