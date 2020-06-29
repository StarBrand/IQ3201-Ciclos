"""campana_saturacion.py: Saturated function of steam"""

import os
import numpy as np
import pandas as pd

PATH = os.path.dirname(os.path.abspath(__file__))
TABLES = os.path.join(PATH, os.pardir, "Tablas")
SATURATED_VALUES = pd.read_csv(os.path.join(TABLES, "agua_saturada_temperatura.csv"))


def saturated_diagram_pv(init_vol: float, final_vol: float) -> (np.ndarray, np.ndarray):
    """
    Gets saturated function values of volume and pressure,
    in a given range of volume

    :param init_vol: Initial volume of function to gets
    :param final_vol: FInal volume of function to gets
    :return: A tuple of array of volume and pressure
    """
    vf = list(SATURATED_VALUES["vf[m3/kg]"])
    vg = reversed(list(SATURATED_VALUES["vg[m3/kg]"]))
    volume = vf + list(vg)
    pressure = list(SATURATED_VALUES["P[kPa]"])
    pressure += list(reversed(pressure))
    return(__abstract_selection(init_vol, final_vol, volume, pressure))


def saturated_diagram_ts(init_entropy: float, final_entropy: float) -> (np.ndarray, np.ndarray):
    """
    Gets saturated function values of entropy and temperature,
    in a given range of entropy

    :param init_entropy: Initial entropy of function to gets
    :param final_entropy: FInal entropy of function to gets
    :return: A tuple of array of entropy and temperature
    """
    sf = list(SATURATED_VALUES["sf[kJ/kg·K]"])
    sg = reversed(list(SATURATED_VALUES["sg[kJ/kg·K]"]))
    entropy = sf + list(sg)
    temperature = list(SATURATED_VALUES["T[°C]"])
    temperature += list(reversed(temperature))
    return(__abstract_selection(init_entropy, final_entropy, entropy, temperature))


def __abstract_selection(init_value: float, final_value: float, values: [float], function: [float]) -> (np.ndarray, np.ndarray):
    """
    Get values and function on the interval of values selected

    :param init_value: Initial value of function to gets
    :param final_value: FInal value of function to gets
    :param values: Whole interval values
    :param function: Function values
    :return: A tuple of array of values and functions
    """
    if init_value in values:
        init = values.index(init_value)
        values = values[init:]
        function = function[init:]
    else:
        value0 = init_value
        f0 = np.interp(value0, values, function)
        numpy_values = np.array(values)
        init = values.index(min(numpy_values[numpy_values >= init_value]))
        values = [value0] + values[init:]
        function = [f0] + function[init:]
    if final_value in values:
        final = values.index(final_value)
        values = values[:final + 1]
        function = function[:final + 1]
    else:
        value = final_value
        f = np.interp(value, values, function)
        numpy_value = np.array(values)
        try:
            final = values.index(max(numpy_value[numpy_value <= final_value]))
        except ValueError:
            raise ValueError("Wrong interval initial value: {} > final value: {}".format(init_value, final_value))
        values = values[:final + 1] + [value]
        function = function[:final + 1] + [f]
    return np.array(values), np.array(function)
