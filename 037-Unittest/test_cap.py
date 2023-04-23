import cap
import unittest

class TestCap(unittest.TestCase):
    
    def test_one_word (self):
        text = "python"
        result = cap.test_cap(text)
        self.assertEqual(result, "Python")
        
    def test_multiple_word (self):
        text = "monty python"
        result = cap.test_cap(text)
        self.assertEqual(result, "Monty Python")

if __name__ == "__name__":
    unittest.main()