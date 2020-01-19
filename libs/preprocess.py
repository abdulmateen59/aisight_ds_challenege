import numpy as np
import pandas as pd

from datetime import datetime
from statistics import mean


class Preprocessor:

    def __init__(self):
        pass

    def read_csv(self,filename):
        try:
            columns_=['Unix_Timestamp', 'Amount_of_Samples', 'Time_Period', 'Sampling_Rate', 'Sensor_Data']
            TextFileReaderObject = pd.read_csv('DataSet/project_pump.csv',
                                                        sep = ';',
                                                        header = None, 
                                                        chunksize = 300,
                                                        names = columns_,
                                                        #low_memory = False,
                                                        converters={'Sensor_Data': eval}, 
                                                        verbose = True)
            df = pd.concat(chunk for chunk in TextFileReaderObject)
            #print(df)
            return df
        except IOError as err:
            print('Error while reading file... \n ' , err )

    def unix_time(self,df):
        for i in range(df.shape[0]):
            df.loc[i, 'Unix_Timestamp'] = datetime.fromtimestamp(df.loc[i, 'Unix_Timestamp']).strftime('%Y-%m-%d %H:%M:%S')   #for analysis purpose 
        return df

    def data_mean(self,df):
        for i in range(df.shape[0]):
            df.loc[i, 'Sensor_Data'] = mean(df.loc[i, 'Sensor_Data'])
        return df

    def data_sum(self,df):
        for i in range(df.shape[0]):
            df.loc[i, 'Sensor_Data'] = sum(df.loc[i, 'Sensor_Data'])
        return df

    def data_max(self,df):
        for i in range(df.shape[0]):
            df.loc[i, 'Sensor_Data'] = max(df.loc[i, 'Sensor_Data'])
        return df

    def data_min(self,df):
        for i in range(df.shape[0]):
            df.loc[i, 'Sensor_Data'] = min(df.loc[i, 'Sensor_Data'])
        return df
