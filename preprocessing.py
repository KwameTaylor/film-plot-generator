import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def plots_split(df, target):
    '''
    This function takes in a dataframe and the string name of the target variable
    and splits it into test (15%), validate (15%), and train (70%). 
    It also splits test, validate, and train into X and y dataframes.
    Returns X_train, y_train, X_validate, y_validate, X_test, y_test, train, validate, test.
    '''
    # split df into test (15%) and train_validate (85%)
    train_validate, test = train_test_split(df, test_size=.15, stratify=df['Release Year'], random_state=666)

    # split train_validate off into train (82.35% of 85% = 70%) and validate (17.65% of 85% = %15)
    train, validate = train_test_split(train_validate, test_size=.1765, random_state=666)

    # split train into X & y
    X_train = train.drop(columns=[target])
    y_train = train[target]
    
    # split validate into X & y
    X_validate = validate.drop(columns=[target])
    y_validate = validate[target]
    
    # split test into X & y
    X_test = test.drop(columns=[target])
    y_test = test[target]
    
    print('Shape of train:', X_train.shape, '| Shape of validate:', X_validate.shape, '| Shape of test:', X_test.shape)
    print('Percent train:', round(((train.shape[0])/df.count()[0]),2) * 100, '       | Percent validate:', round(((validate.shape[0])/df.count()[0]),2) * 100, '      | Percent test:', round(((test.shape[0])/df.count()[0]),2) * 100)

    return X_train, y_train, X_validate, y_validate, X_test, y_test, train, validate, test