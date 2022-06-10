# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 09:21:50 2021

@author: fflattery
"""
from math import sqrt, pi, tanh

def calc_wave_velocity(wavelength, density, surface_tension, depth, gravity=9.81):
    '''
    Calculate velocity of a surface wave

    Parameters
    ----------
    wavelength : float
        wavelength of the wave.
    density : float
        density of the water.
    surface_tension : float
        surface tension of the water.
    depth : float
        the depth of the water.
    gravity : float, optional
        the acceleration due to gravity. The default is 9.81.

    Returns
    -------
    float
        the velocity of the surface wave.

    '''
    return sqrt(  (gravity*wavelength/(2*pi) + 2*pi*surface_tension/(density*wavelength) ) * tanh(2*pi*depth/wavelength))

if __name__ == "__main__":
    print(round(calc_wave_velocity(0.5, 1, 1.1, 2),2))