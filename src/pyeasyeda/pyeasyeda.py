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
    return df_clean

def birds_eye_view(df):
    """Takes in a data frame object, and displays 3 different visualization sets; 
    a histogram for each numeric variable, a distribution for each categorical variable,
    and a correlation heatmap of the numeric variables

        Parameters
        ----------
        df : dataframe
            dataframe to create the visualizations
    
        Examples
        --------
        >>> birds_eye_view(df_clean)
        
        (displays visualizations)
    
    """
    return

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