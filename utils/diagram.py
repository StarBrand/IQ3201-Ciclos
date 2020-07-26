"""diagrama.py: Method to generate a Diagram"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from utils import FIGSIZE, MARKER_SIZE, LABEL_SIZE, TITLE_SIZE


def diagram(x: [np.ndarray] or [list], y: [np.ndarray] or [list], title: str, diagram: str, hide_values: bool) -> (Figure, Axes):
    """
    Does a diagram, returning the Axes object

    :param x: List of four x curves
    :param y: List of four y curves
    :param title: Title of graph
    :param diagram: Type of diagram
    :param hide_values: Whether or not hide values on ticks
    :return: Figure and Axes with cycle plotted
    """
    fig, ax = plt.subplots(figsize=FIGSIZE)

    ax.plot(x[0], y[0], 'b', label="Etapa 1", linewidth=3)
    ax.plot(x[1], y[1], 'r', label="Etapa 2", linewidth=3)
    ax.plot(x[2], y[2], 'g', label="Etapa 3", linewidth=3)
    ax.plot(x[3], y[3], 'k', label="Etapa 4", linewidth=3)

    ax.scatter(x[0][0], y[0][0], marker='$1$', color='k', s=MARKER_SIZE)
    ax.scatter(x[1][0], y[1][0], marker='$2$', color='k', s=MARKER_SIZE)
    ax.scatter(x[2][0], y[2][0], marker='$3$', color='k', s=MARKER_SIZE)
    ax.scatter(x[3][0], y[3][0], marker='$4$', color='k', s=MARKER_SIZE)

    ax.set_title("{}: Diagrama {}\n".format(title, diagram), fontsize=TITLE_SIZE)
    ax.set_xlabel(diagram[1], fontsize=LABEL_SIZE)
    ax.set_ylabel(diagram[0], fontsize=LABEL_SIZE)
    if hide_values:
        ax.tick_params(
            which='both',
            bottom=False,
            top=False,
            right=False,
            left=False,
            labelbottom=False,
            labelleft=False)
    ax.grid()
    ax.legend(fontsize=LABEL_SIZE)
    return fig, ax
