import unittest
import uuid
import pystego
from pystego.stego import decode, encode

class TestPyStego(unittest.TestCase):
    def setUp(self) -> None:
        self.message = str(uuid.uuid4())
        encode('./resources/hacker.png', self.message)
        self.from_image = decode('./resources/hacker.png')
    
    def test_encode_decode(self):
        self.assertEqual(self.message, self.from_image)

if __name__ == '__main__':
    unittest.main()