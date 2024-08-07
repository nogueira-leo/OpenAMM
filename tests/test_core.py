import unittest

import numpy as np

from OpenAMM.core import Metamaterial

frequency = np.linspace(1, 1000, 100)


class TestMetamaterial(unittest.TestCase):
    def test_compute_response(self):
        """

        Returns:
            response:
        """
        global frequency
        properties = {'density': 1.2,
                      'type': 1}
        meta = Metamaterial(properties)
        response: object = meta.compute_response(frequency)
        resp = properties.get('density') * frequency
        self.assertTupleEqual(response,resp)


if __name__ == '__main__':
    unittest.main()
