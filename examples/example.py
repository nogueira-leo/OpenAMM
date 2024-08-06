from OpenAMM.core import Metamaterial

properties = {'density': 1.21,
              'type':       1}
meta = Metamaterial(properties)
response = meta.compute_response(10.0)
print(response)

