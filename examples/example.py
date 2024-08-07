from typing import Any

import numpy as np
from numpy import ndarray, dtype, floating

from OpenAMM.core import Metamaterial

properties = {'density': 1.21,
              'type':       1}
meta = Metamaterial(properties)
frequency: ndarray[Any, dtype[floating[Any]]] = np.linspace(1, 1000, 100)
response = meta.compute_response(frequency)
print(response)
