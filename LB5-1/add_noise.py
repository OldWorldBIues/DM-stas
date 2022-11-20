'''
set of functions to randomly modify given pandas dataset
'''
import numpy as np
import pandas as pd


def add_feauture_err(df:pd.DataFrame=None, *, column_name: str,
                     err_level: float, err_filler: any ):
    '''
    fill randomly `err_level`% feautures in the `column_name` with `err`
    and return modified dataframe
    '''
    err_count = len(df) * err_level
    err_count = 1 if err_count <= .5 else round(err_count)
    err_indices_list = np.random.randint(0, len(df), err_count)

    # get colum_name index
    column_idx = df.columns.get_loc(column_name)
    # replace cells with err_filler
    df.iloc[err_indices_list, column_idx] = err_filler

    return df

if __name__ == '__main__':
    pass
