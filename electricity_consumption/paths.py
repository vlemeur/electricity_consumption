"""This module contains 'path lib' object of repository files
"""

from pathlib import Path

PATH_REPO = Path(__file__).parent
PATH_INFLUXDB_MK_FILE = PATH_REPO / "influx_db_config.mk"
