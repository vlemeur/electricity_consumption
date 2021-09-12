"""This module contains 'path lib' object of repository files
"""

from pathlib import Path

PATH_REPO = Path(__file__).parent.parent
PATH_INFLUXDB_MK_FILE = PATH_REPO / "influx_db_config.mk"
PATH_DATA = PATH_REPO / "data"
PATH_DATA_RAW = PATH_DATA / "raw"
