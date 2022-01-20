import pandas as pd
import numpy as np
import altair as alt
from pyeasyeda.close_up import close_up
import pytest


def test_csummary_suggestions_error():
    """Checks TypeError and ValueError raised when inputs are not erroneous."""

    # create toy_data
    toy_data = {
        "income": [5, 8, 10, 12, 17, 19],
        "house_size": [700, 600, 900, 1000, 1200, 1500],
        "views": ["mountain", "river", "sea", "mountain", "urban", "forest"],
        "price": [65, 50, 80, 98.5, 112, 133],
        "doctor_visits": [6, 8, 4, 5, 3, 2],
    }
    df = pd.DataFrame(toy_data)

    # Checking invalid inputs
    with raises(TypeError):
        pytest.summary_suggestions(1)

    with raises(TypeError):
        pytest.summary_suggestions(df, threshold = "a")

    with raises(TypeError):
        pytest.summary_suggestions(df, threshold = [0.8])


def test_summary_suggestions():
    """Tests summary_suggestions from a toy dataset"""

    toy_data = {
        "income": [5, 8, 10, 12, 17, 19],
        "house_size": [700, 600, 900, 1000, 1200, 1500],
        "views": ["mountain", "river", "sea", "mountain", "urban", "forest"],
        "price": [65, 50, 80, 98.5, 112, 133],
        "doctor_visits": [6, 8, 4, 5, 3, 2],
    }
    df = pd.DataFrame(toy_data)

    # unit tests - returned pandas dataframe object
    results = summary_suggestions(df)

    assert results[3] == ['views']
    , "Variables with large number of unique values incorrectly identified"

    assert results[0]['income'].sum() == 82.42811271761728
    , "Wrong summary statistics for 'income' variable"

    assert results[2]['views']['unique'] == 0.8333333333333334
    , "Percentage of unique values incorrectly calculated for variable 'views'"

    assert (
        len(results[3]) == 1
    ), "Number of variables with large number of unique values should be 1" 

    