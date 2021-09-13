from electricity_consumption.db_interact import get_df_from_raw_enedis, upload_df_to_influxdb
from electricity_consumption.paths import PATH_DATA_RAW

#######################################################################################################################
# TO BE FILLED - START
#######################################################################################################################
file_name = "" # Name of enedis csv file data/raw folder


#######################################################################################################################
# TO BE FILLED - END
#######################################################################################################################

if __name__ == "__main__":


    path_enedis_data = PATH_DATA_RAW / file_name

    df = get_df_from_raw_enedis(path_raw_enedis=path_enedis_data)

    upload_df_to_influxdb(df=df)
