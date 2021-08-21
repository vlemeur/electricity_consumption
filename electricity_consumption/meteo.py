"""This module provides functions to get meteorological data
"""
from typing import Optional

import pandas as pd

METEO_FRANCE_URL = "https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/Archive/synop.{}{}.csv.gz"


def get_meteorological_month_data(
    year_str: int, month_str: int, station_id: Optional[str] = "07149", freq_min: Optional[int] = 30
) -> pd.DataFrame:
    """Gets humidity, pressure, and temperature data from France meteorological
     using a year, month, station id and interpolation frequency.

    Parameters
    ----------
    year_str : int
        int of year to target
    month_str : int
        int of month to target
    station_id : str, optional
        Station number to target. Other numbers are available
        at https://donneespubliques.meteofrance.fr/?fond=produit&id_produit=90&id_rubrique=32, by default '07149'
    freq_min : int, optional
        Frequency in minutes to target, by default 30

    Returns
    -------
    pd.DataFrame
        pd.Dataframe containing temperature, humidity, and pressure data at input frequency in minutes
    """
    month_str_reformat = "{:02d}".format(month_str)
    df = pd.read_csv(METEO_FRANCE_URL.format(year_str, month_str_reformat), sep=";", dtype=str)
    df = df.loc[df["numer_sta"] == station_id, ["date", "t", "u", "pres"]]
    df.index = pd.to_datetime(df["date"])
    df = df.drop("date", axis=1).astype("float")
    return df.resample(f"{freq_min}min").interpolate()
