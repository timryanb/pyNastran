"""
defines:
 - polar_to_real_imag
 - real_imag_to_mag_phase

"""

import numpy as np


def polar_to_real_imag(mag, phase):
    """
    Converts magnitude-phase to real-imaginary
    so all complex results are consistent

    Parameters
    ----------
    mag : float
        magnitude c^2
    phase : float
        phase angle phi (degrees; theta)

    Returns
    -------
    real_value : float
        the real component a of a+bi
    imag_value : float
        the imaginary component b of a+bi

    """
    rtheta = np.radians(phase)
    try:
        out = mag * (np.cos(rtheta) + 1.j * np.sin(rtheta))
    except FloatingPointError:
        phase2 = np.asarray(phase, dtype='float64')
        rtheta = np.radians(phase2)
        out = mag * (np.cos(rtheta) + 1.j * np.sin(rtheta)).asdtype('complex64')
    return out
    #return rect(mag, radians(phase))

def real_imag_to_mag_phase(real_imag):
    """returns the magnitude and phase (degrees) of a complex number"""
    return np.abs(real_imag), np.angle(real_imag, deg=True)
