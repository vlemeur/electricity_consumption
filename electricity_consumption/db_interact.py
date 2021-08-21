"""This module provides function to interact with Influx DB database
"""

from influxdb_client import InfluxDBClient

from electricity_consumption.constantes import INFLUXDB_TOKE, INFLUXDB_URL
from electricity_consumption.paths import PATH_INFLUXDB_MK_FILE
from electricity_consumption.utils import get_variables_from_mk_file

DICT_INFLUXDB = get_variables_from_mk_file(path_mk_file=PATH_INFLUXDB_MK_FILE)


def initiate_influxdb_client() -> InfluxDBClient:
    """Initiates influx db client

    Returns
    -------
    InfluxDBClient
        Influx db client initiated
    """
    return InfluxDBClient(
        url=INFLUXDB_URL, token=INFLUXDB_TOKE, org=DICT_INFLUXDB["DOCKER_INFLUXDB_INIT_ORG"], debug=False
    )
