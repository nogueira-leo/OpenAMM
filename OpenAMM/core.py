import logging
import numpy as np
import json
logger = logging.getLogger()
import utils

properties = ['air.json',
              'porous.json',
              'amm.json']
class CSAMM:
    def __init__(self, props:list[str]):
        """
        Initialize an instance of a Coiled Spaece Acoustic MetaMaterial with given properties.
        
        Args:
            properties (dict): A dictionary of material properties.
        """
        self.frequency = np.linspace(1,1000,100)
        self.airProps = {}
        self.porousProps = {}
        self.ammProps = {}
        self.props = [self.airProps,
                      self.porousProps, 
                      self.ammProps]
        
        try:
            for ii,path in enumerate(props):
                self.props[ii]=utils.get_json(path)
            
        except NameError:
            print("my_variable does not exist")
            with open("air.json") as varr:
                for key, value in json.load(varr).items():
                    properties[key] = value
        else:
            print("my_variable exists")
        self.properties = properties

    def compute_response(self) -> object:
        """
        Compute the response of the Metamaterial at a given frequency.
        Args:
            frequency (float): The frequency at which to compute the response.
        
        Returns:
            response (float): The computed response.
        """
        # Placeholder for actual computation logic
        response = self.airProps["rho_0"] * self.frequency
        return response

def example_function():
    return CSAMM(properties).compute_response()