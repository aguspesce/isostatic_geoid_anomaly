"""
Function to calculate the geoid anomaly using the Ary hipotesis
"""

import numpy as np
from scipy.constants import G


def airy_root(rho_c, rho_m, h_topo):
    """
    Compute the root thickness based on Airy isostasy.

    Parameters:
    - rho_crust: Density of the crust (kg/m^3)
    - rho_mantle: Density of the mantle (kg/m^3)
    - topo_height: Topographic height (m)

    Returns:
    - root_thickness: Root thickness (m)
    """
    root = rho_c * h_topo / (rho_m - rho_c)

    return root


def calculate_geoid_anomaly(rho_c, rho_m, crust_thickness, h_topo, g_ref_mgal):
    """
    Calculate the geoid anomaly using the analytical Airy isostasy formula.

    Parameters:
    - rho_crust: Density of the crust (kg/m^3)
    - rho_mantle: Density of the mantle (kg/m^3)
    - crust_thickness: Thickness of the crust (m)
    - topo_height: Elevation (m)
    - g_ref_mgal: Normal gravity (mGal)

    Returns:
    - Geoid anomaly (m)
    """
    # Mgal to m/s2
    g_ref = g_ref_mgal * 1.0e-5

    geoid = (np.pi * G * rho_c / g_ref) * (
        rho_m * h_topo**2 / (rho_m - rho_c) + 2 * crust_thickness * h_topo
    )

    return geoid

