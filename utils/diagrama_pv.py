"""diagrama_pv.py: Method to generate a Pv Diagram"""

import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from utils import diagram


def diagrama_pv(v: [np.ndarray] or [list], P: [np.ndarray] or [list], title: str, hide_values: bool) -> (Figure, Axes):
    """
    Does a diagram, returning the Axes object

    :param v: List of four volume curves
    :param P: List of four pressure curves
    :param title: Title of graph
    :param hide_values: Whether or not hide values on ticks
    :return: Figure and Axes with cycle plotted
    """
    return diagram(v, P, title, "Pv", hide_values)
