# Licensed under a 3-clause BSD style license - see LICENSE.rst
from numpy.testing import assert_approx_equal
from ..const import conversion_factor as cf

def test_conversion_factor():
    assert_approx_equal(cf('erg', 'GeV'), 624.150947961)
