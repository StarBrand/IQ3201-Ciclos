"""diagrama_ts.py: Method to generate a TS Diagram"""

import numpy as np
from matplotlib.axes import Axes
from utils import diagram


def diagrama_ts(S: [np.ndarray] or [list], T: [np.ndarray] or [list], title: str, hide_values: bool) -> Axes:
    """
    Does a diagram, returning the Axes object

    :param S: List of four entropy curves
    :param T: List of four temperature curves
    :param title: Title of graph
    :param hide_values: Whether or not hide values on ticks
    :return: Axes with cycle plotted
    """
    return diagram(S, T, title, "TS", hide_values)
