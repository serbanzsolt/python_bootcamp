import unittest
import string

def encrypt (message):
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    encrypted_message = "".join([abc[abc.find(letter)+1] if len(abc) > (abc.find(letter)+1) else abc[0] for idx, letter in enumerate(message)])
    # encrypted_message = "".join([str(idx) for idx, letter in enumerate(message)])
    print(encrypted_message)
    return encrypted_message

class TestEncryption(unittest.TestCase):
    
    #in the TestCase class we use setUp method instead of __init__
    def setUp(self):
        self.my_message = "I' m Batman!!! 888"
    
    def test_inputExist(self):
        self.assertIsNotNone(self.my_message)
    
    def test_inputType(self):
        self.assertIsInstance(self.my_message, str)
    
    def test_functReturnSomething(self):
        self.assertIsNotNone(encrypt(self.my_message))
        
    def test_lenIO(self): #lenght of input and output
        self.assertEqual(len(self.my_message), len(encrypt(self.my_message)))
        
    def test_differentIO(self):
        self.assertNotIn(self.my_message, encrypt(self.my_message))
        
    def test_shiftedCipher(self):
        abc = string.ascii_letters + string.punctuation + string.digits + " "
        encrypted_message = "".join([abc[abc.find(letter)+1] if len(abc) > (abc.find(letter)+1) else abc[0] for idx, letter in enumerate(self.my_message)])
        # print(abc[abc.find("c")+1])
        print(encrypted_message)
        self.assertEqual(encrypted_message, encrypt(self.my_message))
    
if __name__ == "__main__":
    unittest.main()