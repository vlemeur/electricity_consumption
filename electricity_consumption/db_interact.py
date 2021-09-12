"""This module provides function to interact with Influx DB database
"""

from pathlib import Path

import pandas as pd

from electricity_consumption.paths import PATH_INFLUXDB_MK_FILE
from electricity_consumption.utils import get_variables_from_mk_file

DICT_INFLUXDB = get_variables_from_mk_file(path_mk_file=PATH_INFLUXDB_MK_FILE)


def get_df_from_raw_enedis(path_raw_enedis: Path) -> pd.DataFrame:
    """Read a csv generated for enedis and returns a DataFrame

    Parameters
    ----------
    path_raw_enedis : Path
        Path to the enedis csv

    Returns
    -------
    pd.DataFrame
        Pandas DataFrame with enedis sensor value as column
    """
    # Read csv
    df = pd.read_csv(path_raw_enedis, sep=";", encoding="latin-1")

    # Date conversion and index
    df["date"] = df["Date de la mesure"] + " " + df["Heure de la mesure"]
    df.index = pd.to_datetime(df["date"])

    # Filter empty values
    df = df[~df["Valeur"].isna()]

    return df[["Valeur"]].rename(columns={"Valeur": "Value"})
