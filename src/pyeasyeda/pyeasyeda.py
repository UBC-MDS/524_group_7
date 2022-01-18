import numpy as np
import pandas as pd
import seaborn as sns
import warnings
import matplotlib.pyplot as plt

def clean_up(df):
    """Takes a dataframe object and returns a cleaned version with the NaN values removed.
     It also prints a list of potential outliers for each explanatory variable, based on a
     threshold distance from the respective median value.
        Parameters
        ----------
        df : dataframe
            dataframe to be cleaned
    
        Returns
        -------
        df_clean
            same dataframe with all the NaN's removed
        Examples
        --------
        >>> df_clean = clean_up(df)
                
        '**The following potenital outliers were detected:**
        Variable X: 100002039.26, located at [0,4]
        Variable Y: .2, located at [3,56]'
    
    """
    return 

def birds_eye_view(df, n=20, var_list=None):
    """Takes in a pandas.DataFrame object, an optional integer for the histogram bin size, an optional custom variable list, and displays 3 different visualization sets.

    1. Histograms for each numeric variable
    2. A bar chart for each categorical variable
    3. A correlation heatmap of the numeric variables.

    The function also has built in warnings for identifying erroneous variables in the custom variable list, and which categorical variables are not suitable for bar charts based on their number of unique categories.

    Parameters
    ----------
    df : pandas.DataFrame
        dataframe to create the visualizations
    n : int
        bin size for histograms
    var_list : list
        a specific list of variables to examine, defaults to None

    Returns
    -------
    charts: list
        A list containing the plot objects created by this function

    Examples
    --------
    >>> birds_eye_view(df, n=30)

    """

    if not (type(df) == pd.DataFrame):
        raise TypeError("df must be input as a DataFrame.")

    if type(var_list) != list and var_list is not None:
        raise TypeError("var_list must be a list.")

    if type(n) != int:
        raise TypeError("n must be an integer.")

    # Generate the visualizations

    viz = {}
    heatmap_list = []
    heatmap = []
    histograms = []
    bar_charts = []

    # Defining the numeric and categorical variables
    numeric = df.select_dtypes(include=np.number).columns.tolist()
    categorical = df.select_dtypes(include=("object" or "string")).columns.to_list()

    # Plot all the variables
    if var_list is None:

        # Histograms
        for num_col in numeric:
            chart = sns.histplot(df, x=(num_col), bins=n, kde=True)
            plt.title("Histogram for " + num_col)
            plt.figure()
            histograms.append(chart)

        # Bar Charts
        for cat_col in categorical:
            if len(df[cat_col].value_counts()) > 10:
                message = (
                    "The variable "
                    + cat_col
                    + " has more than 10 "
                    + "unique values, and is not suitable for a bar chart."
                )
                warnings.warn(message, DeprecationWarning)
            else:
                chart = sns.countplot(data=df, x=(cat_col))
                plt.title("Bar Chart for " + cat_col)
                plt.figure()
                bar_charts.append(chart)

        # Heatmap
        corr_matrix = df[numeric].corr()
        mask = np.triu(np.ones_like(corr_matrix, dtype=np.bool_))
        chart = sns.heatmap(data=corr_matrix,
                            vmin=-1,
                            vmax=1,
                            annot=True,
                            cmap="BrBG",
                            mask=mask
        )
        plt.title("Heatmap of correlation between numeric features")
        plt.figure(figsize=(12, 6))
        print(chart)
        viz["heatmap"] = chart

    # Plot just the custom variables from var_list (if applicable)
    else:
        for custom_col in var_list:

            # Histograms
            if custom_col in numeric:
                heatmap_list.append(custom_col)
                chart = sns.histplot(df, x=(custom_col), bins=n, kde=True)
                plt.title("Histogram for " + custom_col)
                plt.figure()
                histograms.append(chart)

            # Bar Charts
            elif custom_col in categorical:
                if len(df[custom_col].value_counts()) > 10:
                    message = (
                        "The variable "
                        + custom_col
                        + " has more than 10 "
                        + "unique values, and is not suitable for a bar chart."
                    )
                    warnings.warn(message, DeprecationWarning)
                else:
                    chart = sns.countplot(data=df, x=(custom_col))
                    plt.title("Bar Chart for " + custom_col)
                    plt.figure()
                    bar_charts.append(chart)
            else:
                message2 = (
                    "Variable name "
                    + custom_col
                    + " not found in data frame, please check inputs in var_list."
                )
                warnings.warn(message2, DeprecationWarning)

        # Heatmap
        corr_matrix = df[heatmap_list].corr()
        mask = np.triu(np.ones_like(corr_matrix, dtype=np.bool_))
        chart = sns.heatmap(data=corr_matrix,
                            vmin=-1,
                            vmax=1,
                            annot=True,
                            cmap="BrBG",
                            mask=mask
        )
        plt.title("Heatmap of correlation between numeric features")
        plt.figure(figsize=(12, 6))
        viz["heatmap"] = chart

    viz["histograms"] = histograms
    viz["bar_charts"] = bar_charts
    
    return viz

def close_up(df, N=1):
    """Takes in a dataframe object and displays a scatterplot with a correlation trend 
    line visualization of the variable(s) most strongly correlated with the 
    dependent variable.
        Parameters
        ----------
        df : dataframe
            dataframe to create the visualization(s)
        N : number of visualizations of the variable(s) with the 
            strongest correlation to the dependent variable to be displayed,
            defaults to 1
        
        Examples
        --------
        >>> close_up(df_clean)
        
        (displays visualizations)
    
    """
    return

def summary_suggestions(df):
    """Takes a dataframe object and displays a table of summary statistics. 
    Underneath that table it prints analysis considerations that 
    help highlight potential issues, if applicable, and serves as a general 
    guideline for the analysis.
        Parameters
        ----------
        df : dataframe
            Dataframe to be examined
        
        Examples
        --------
        >>> summary_suggestions(df_clean)
        
        '(summary statistics)
        
        **Potential Analysis Considerations:**
        Please review, and take the following into consideration:
        
        Class Imbalance: There appears to be class imbalance in the variable X. 
        Unique Values: Variable X is comprised of 97% unique values in it's observations.'
    
    """
    return
