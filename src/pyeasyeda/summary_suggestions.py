import pandas as pd
import numpy as np

def summary_suggestions(df, threshold = 0.8):
    """Takes a dataframe object and displays a table of summary statistics. 
    Underneath that table it prints analysis considerations that 
    help highlight potential issues, if applicable, and serves as a general 
    guideline for the analysis.

    Parameters
    ----------
    df : pandas dataframe
        Dataframe to be examined

    threshold : float
        threshold for considering class imbalance

    Returns
    -------

    numeric_summary_df : pandas dataframe
        Dataframe for summary statistics of numeric variables

    categorical_summary_df : pandas dataframe
        Dataframe for summary statistics of categorical variables

    Examples
    --------
    >>> summary_suggestions(df)

    (summary statistics for numeric variables)
        
    ** Potential Analysis Considerations: **
    Please review and take the following into consideration:
    
    Class Imbalance: There appears to be class imbalance in the variable X. 
    Unique Values: Variable X is comprised of 97% unique values in it's observations.'
    
    """

    # check if input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input df must be a pandas dataframe object")

    if type(threshold) != int:
        raise TypeError("Input threshold must be an integer")

    if not isinstance(numeric_summary_df, pd.DataFrame):
        raise TypeError("Output summary dataframe df for numeric columns must be a pandas dataframe object")

    if not isinstance(categorical_summary_df, pd.DataFrame):
        raise TypeError("Output summary dataframe df for categorical columns must be a pandas dataframe object")

    numeric_summary_df = df.select_dtypes(include=np.number).describe()
    categorical_summary_df = df.select_dtypes(include=np.object_).describe()

    print("** Potential Analysis Considerations: ** \n \
    Please review and take the following into consideration:")

    print(f"Summary statistics for numeric columns of the dataframe: \n\n {numeric_summary_df} \n\n")
    print(f"Summary statistics for categorical columns of the dataframe: \n\n {categorical_summary_df} \n\n")

    class_imbalance_df = categorical_summary_df[categorical_summary_df.index == 'unique']/len(df)
    filtered_class_imbalance_df = class_imbalance_df.loc['unique'] > threshold
    class_imbalance_vars = [*filter(class_imbalance_df.get, class_imbalance_df.index)]
    
    for var in class_imbalance_vars:
        print(f"There appears to be class imbalance in variable {var} \
        which comprises of {round(class_imbalance_df[var]['unique']*100)}% unique values. \n ")

