# Licensed under a 3-clause BSD style license - see LICENSE.rst
import numpy as np
import pytest
from .. import measure

try:
    import scipy
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False


def generate_example_image():
    """
    Generate some greyscale image to run the detection on.
    """
    x = y = np.linspace(0, 3 * np.pi, 100)
    X, Y = np.meshgrid(x, y)
    image = X * Y * np.sin(X) ** 2 * np.sin(Y) ** 2

    return image

@pytest.mark.skipif('not HAS_SCIPY')
def test_measure():
    image = generate_example_image()
    labels = np.zeros_like(image, dtype=int)
    labels[10:20, 20:30] = 1
    results = measure.measure_labeled_regions(image, labels)

    # TODO: check output!
