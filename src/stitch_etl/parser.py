import pandas as pd

def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df

def split_names(df, column_name, output_column_name):
    """
    simple transformation of data
    """
    df[output_column_name] = df[column_name].split(",")

def map_to_model(df):
    """
    parse the rows of data and map to the model classes
    """
    pass
