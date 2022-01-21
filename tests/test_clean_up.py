import pandas as pd
import numpy as np
import pytest
from pytest import raises
from scipy import stats
import io
import sys
from pyeasyeda.clean_up import clean_up


def test_clean_up():
    """tests the new dataset and output outliers of clean_up from a toy dataset."""
    
    # Load toy dataset
    data = {
        "neighbourhood": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
        "price": [100, 120, 150, 90, 150000, np.NaN, 200, 300, 500, 50, 300, 100, 200],
        "number_of_reviews": [600, 1, 27000000, 1, 1, 2, 1, 2, 0, np.NaN, 2, 100, 500]
    }

    df = pd.DataFrame(data)

    clean = pd.DataFrame(
        {
        "neighbourhood": ["A", "B", "C", "D", "E", "G", "H", "I", "K", "L", "M"],
        "price": [100.0, 120.0, 150.0, 90.0, 150000.0, 200.0, 300.0, 500.0, 300.0, 100.0, 200.0],
        "number_of_reviews": [600.0, 1.0, 27000000.0, 1.0, 1.0, 1.0, 2.0, 0.0, 2.0, 100.0, 500.0]
        }
    )

    # Test the returned dataframe
    assert pd.DataFrame.equals(
        clean_up(df), clean
    ), "The returned dataframe using clean_up is not correct"
    
    # Create StringIO object
    capturedOutput = io.StringIO()
    
    # Redirect stdout
    sys.stdout = capturedOutput
    
    # Call clean_up on toy dataset
    clean_up(df)
    
    # Reset redirect
    sys.stdout = sys.__stdout__
    
    # Store print output in statement as a string
    statement = str(capturedOutput.getvalue())
    
    # Check if the statement contains the correct outliers
    assert (
        '27000000' in statement
    ), "Outlier should contain 27000000"
    assert (
        '150000' in statement
    ), "Outlier should contain 150000"

def test_clean_up_error():
    """Check TypeError and ValueError raised when inputs are not appropriate."""

   # Load toy dataset
    data = {
        "neighbourhood": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
        "price": [100, 120, 150, 90, 150000, np.NaN, 200, 300, 500, 50, 300, 100, 200],
        "number_of_reviews": [600, 1, 27000000, 1, 1, 2, 1, 2, 0, np.NaN, 2, 100, 500]
    }

    df = pd.DataFrame(data)

    # Tests if the input is not dataframe
    with raises (TypeError):
        clean_up("not dataframe")
