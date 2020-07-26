"""diagrama_ph.py: Method to generate a Ph Diagram"""

import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from utils import diagram


def diagrama_ph(h: [np.ndarray] or [list], P: [np.ndarray] or [list], title: str, hide_values: bool) -> (Figure, Axes):
    """
    Does a diagram, returning the Axes object

    :param h: List of four entalpy curves
    :param P: List of four pressure curves
    :param title: Title of graph
    :param hide_values: Whether or not hide values on ticks
    :return: Figure and Axes with cycle plotted
    """
    return diagram(h, P, title, "Ph", hide_values)
