from genericpath import exists
import logging
import numpy as np


class Metamaterial:
    def __init__(self, properties):
        """
        Initialize the metamaterial with given properties.
        
        Args:
            properties (dict): A dictionary of material properties.
        """
        try:
            properties
        except NameError:
            print("my_variable does not exist")
        else:
            print("my_variable exists")
        self.properties = properties

    
    def compute_response(self, frequency: object) -> object:
        """
        Compute the response of the metamaterial at a given frequency.
        
        Args:
            frequency (float): The frequency at which to compute the response.
        
        Returns:
            response (float): The computed response.
        """
        # Placeholder for actual computation logic
        response = self.properties.get('density') * frequency
        return response

def example_function():

    properties = {'density':    1.21,
                  'type':       1}
    frequency = np.linspace(0.001, 6000, 50)
    return Metamaterial(properties).compute_response(frequency)