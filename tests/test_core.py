# tests/test_core.py

import unittest
from OpenAMM.core import Metamaterial

class TestMetamaterial(unittest.TestCase):
    def test_compute_response(self):
        properties = {'density':1.2,
                      'type':   1   }
        meta = Metamaterial(properties)
        response = meta.compute_response(10.0)
        self.assertEqual(response, 12.0)

if __name__ == '__main__':
    unittest.main()
