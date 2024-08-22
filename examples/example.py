import numpy as np
from numpy import ndarray, dtype, floating

from openamm.core import CSAMM

properties = {'density': 1.21,
              'type':       1}
meta = CSAMM(properties)
frequency = np.linspace(1, 1000, 100)
response = meta.compute_response(frequency)
print(response)
print(all(properties['density']*frequency==response))