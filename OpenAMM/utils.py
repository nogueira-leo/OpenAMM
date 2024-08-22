# OpenAMM/utils.py
import json
import numpy as np

def validate_properties(properties):
    """
    Validate the properties of a metamaterial.
    
    Args:
        properties (dict): A dictionary of material properties.
    
    Returns:
        bool: True if properties are valid, False otherwise.
    """
    # Placeholder for validation logic
    return isinstance(properties, dict)

def get_json(path: str):
    """Get dictionaire from json file
    Args:
        path (str): path to file

    Returns:
        dict: dictionaire from json
    """    
    var = {}
    with open(path) as varr:
                for key, value in json.load(varr).items():
                    var[key] = value
    return var

def stinson_square(self, f, params: dict, num=200):
    """_summary_

    Args:
        f (array): Frequency
        La (float): Channel Width
        Lb (float): Channel Height

    Returns:
        _type_: _description_
    """ 
    R = 0
    C = 0
    k = np.arange(0,num)
    n = np.arange(0,num)
    a = np.pi/La*(k+1/2)
    b = np.pi/Lb*(n+1/2)
    a2 = a[:, None] ** 2
    b2 = b[None, :] ** 2
    a2_plus_b2 = a2 + b2
    nuv_La2_Lb2 = nuv * La**2 * Lb**2
    nut_La2_Lb2 = nut * La**2 * Lb**2
    R = np.sum((a2 * b2 * (a2_plus_b2 + 1j * w / nuv)) ** -1)
    C = np.sum((a2 * b2 * (a2_plus_b2 + 1j * w * gamma / nut)) ** -1)
    r = rho_0 * (nuv_La2_Lb2 / (4 * 1j * w) * R ** -1)
    K = 1 / P_0 * (1 - (4j * w * (gamma - 1)) / (nut_La2_Lb2) * C)

    return r, K