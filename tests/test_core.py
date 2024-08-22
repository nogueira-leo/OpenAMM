import unittest

import numpy as np

from openamm.core import CSAMM

class TestMetamaterial(unittest.TestCase):
    def test_compute_response(self):
        """

        Returns:
            response:
        """
        meta = CSAMM(properties)
        response = meta.compute_response(frequency)
        resp = properties.get('density') * frequency
        self.assertTrue(all(response==resp))


if __name__ == '__main__':
    unittest.main()
