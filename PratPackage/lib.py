# -*- coding: UTF-8 -*-

from os.path import abspath
from os.path import dirname
import pandas as pd


def tryme():
    """ Create data
    """
    return "Yuhuu,My very first package"


if __name__ == "__main__":
    # For introspections purpose to quickly get this functions on ipython
    # with data
    import packgenlite

    datapath = dirname(abspath(packgenlite.__file__)) + "/data"
    data = "{}/data.csv".format(datapath)
    df = pd.read_csv(data)
    data = tryme()
    print("df, data made")
