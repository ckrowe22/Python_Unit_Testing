import pytest
from temp import *


@pytest.mark.celsius
def test_cel_to_fahr():
    assert cel_to_fahr(30) == 86
    assert cel_to_fahr(10) == 50


@pytest.mark.fahrenheit
def test_fahr_to_cel():
    assert fahr_to_cel(86) == 30
    assert fahr_to_cel(50) == 10


@pytest.mark.kelvin
def test_kelvin_to_rank():
    assert kelvin_to_rank(273) == 492.00000000000006
    assert kelvin_to_rank(295) == 531.6


@pytest.mark.rankine
def test_fahr_to_rank():
    assert fahr_to_rank(0) == 460
    assert fahr_to_rank(75) == 535


@pytest.mark.kelvin
def test_rank_to_kelvin():
    assert rank_to_kelvin(0) == -0.3333333333333333
    assert rank_to_kelvin(531.6) == 295


@pytest.mark.celsius
def test_cel_to_kelvin():
    assert cel_to_kelvin(0) == 273
    assert cel_to_kelvin(5) == 278


@pytest.mark.kelvin
def test_kelvin_to_cel():
    assert kelvin_to_cel(273) == 0
    assert kelvin_to_cel(278) == 5


@pytest.mark.kelvin
def test_kelvin_to_fahr():
    assert kelvin_to_fahr(273) == 32
    assert kelvin_to_fahr(296.8888889) == 75.00000001999997


@pytest.mark.fahrenheit
def test_fahr_to_kelvin():
    assert fahr_to_kelvin(75) == 296.8888888888889
    assert fahr_to_kelvin(32) == 273

