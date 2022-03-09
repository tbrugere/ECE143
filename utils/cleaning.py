"""functions used to clean up the datasets"""
from collections.abc import Collection
import string

import pandas as pd
from unidecode import unidecode


#data clean up
def clean(df: pd.DataFrame, col: Collection[str]):
    """
    data clean up
    :param df: pd data frame
    :param col: list of columns to clean up
    :return: df: pd data fram 
    """
    assert all(i in df.columns for i in col), "No such column"

    for i in df.columns:
        if i in col:
            df[i] = df[i].str.replace('[', '', regex=False)
            df[i] = df[i].str.replace(']', '', regex=False)
            df[i] = df[i].str.replace('\\s+', ' ', regex=True)
            df[i] = df[i].str.lstrip("'")
            df[i] = df[i].str.rstrip("'")
            df[i] = df[i].str.strip("'")
            df[i] = df[i].str.translate(str.maketrans('', '', string.punctuation))
            df[i] = df[i].str.lower()
            df[i] = df[i].apply(unidecode) #removes accents and other things


    return df

def decode(df: pd.DataFrame, col: Collection[str]):
    """
    decode a column intepreted as bytes
    :param df: pd data frame
    :param col: clean up column
    :return: df: pd data fram 
    """
    assert all(i in df.columns for i in col), "No such column"

    for i in df.columns:
        if i in col:
          df[i] = df[i].str.decode("utf-8")

def spotify_clean_up(df: pd.DataFrame, col: Collection[str]):
    """
    data clean up for spotify dataset
    :parm df: pd data frame
    :col: clean up column
    :return: df: pd data fram 
    """
    assert all(i in df.columns for i in col), "No such column"

    for i in df.columns:
        if i in col:
            df[i].fillna(0)
            df[i] = df[i].str.replace('[', '', regex=False)
            df[i] = df[i].str.replace(']', '', regex=False)
            df[i] = df[i].str.replace('\\s+', ' ', regex=True)
            df[i] = df[i].str.lstrip("'")
            df[i] = df[i].str.rstrip("'")
            df[i] = df[i].str.strip("'")          
            df[i] = df[i].str.translate(str.maketrans('', '', string.punctuation))
            df[i] = df[i].str.lower()
        else:
            df[i] = df[i]

    return df
