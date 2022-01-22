import pandas as pd
import numpy as np
import altair as alt
from pyeasyeda.close_up import close_up
import pytest


def test_close_up():
    """Tests close_up from a toy dataset."""

    # create toy_data
    toy_data = {
        "income": [5, 8, 10, 12, 17, 19],
        "house_size": [700, 600, 900, 1000, 1200, 1500],
        "views": ["mountain", "river", "sea", "mountain", "urban", "forest"],
        "price": [65, 50, 80, 98.5, 112, 133],
        "doctor_visits": [6, 8, 4, 5, 3, 2],
    }
    df = pd.DataFrame(toy_data)

    # unit tests - returned altair chart object
    fig = close_up(df, 1)
    assert isinstance(
        fig, alt.vegalite.v4.api.LayerChart
    ), "n=1 should return a LayerChart"
    actual = str(type(close_up(df, 1)))

    fig = close_up(df, 4)
    assert isinstance(
        fig, alt.vegalite.v4.api.VConcatChart
    ), "n>1 should return a VConcatChart"

    assert len(fig.vconcat) == 4, "Incorrect number of subplots!"

    assert (fig.data == df).sum().sum(
    ) == 30, "Data used in plot is different."


def test_close_up_error():
    """Check TypeError and ValueError raised when inputs are not appropriate."""
    with pytest.raises(TypeError):
        numpy_array = np.ones((3, 3))
        close_up(numpy_array)

    # create toy_data
    toy_data = {
        "income": [5, 8, 10, 12, 17, 19],
        "house_size": [700, 600, 900, 1000, 1200, 1500],
        "views": ["mountain", "river", "sea", "mountain", "urban", "forest"],
        "price": [65, 50, 80, 98.5, 112, 133],
        "doctor_visits": [6, 8, 4, 5, 3, 2],
    }
    df = pd.DataFrame(toy_data)

    with pytest.raises(TypeError):
        float_num = 2.3
        close_up(df, n=2.3)

    with pytest.raises(ValueError):
        big_int = 10
        close_up(df, n=big_int)
