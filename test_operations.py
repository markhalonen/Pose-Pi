import unittest
import operations
import random

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
            
    def testWriteReadTag(self):
        tag = str(random.random())
        operations.writeTag(tag)
        self.assertEqual(tag, operations.readTag())
    
    def testCheckSnapCommandFormat(self):
        self.assertTrue(operations.checkSnapCommandFormat(operations.toJSON('{"command":"snap","args":{"photo_event_id":"04248558-2c8b-454e-95fd-f9c46955d919","hw_id":"8f2c1519-80a6-4209-8c4b-a3ca9aee40a1"}}')))

if __name__ == '__main__':
    unittest.main()