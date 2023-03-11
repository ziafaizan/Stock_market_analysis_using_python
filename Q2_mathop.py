import os
import pandas as pd
import numpy as np
import statistics as stats

def math_op(columns,folder_path):
    file_list = os.listdir(folder_path)
    print(file_list)
    df=pd.DataFrame()

    for i in file_list:
        stock_data = pd.read_csv(folder_path+"/"+i).dropna()
        for col in columns:
            all_val={'Name':i,
                    'MIN':stock_data[col].min(),
                    'MAX':stock_data[col].max(),
                    'AVG':stock_data[col].mean(),
                    'MODE':stats.mode(stock_data[col]),
                    'STD':stock_data[col].std(),
                    'PERCENTILE':np.round(np.percentile(stock_data[col],[25,50,75]),2)}
            df=df.append(all_val,ignore_index=True)
    df.to_csv('Q2_mathOP.csv',index=False)
# Add all the columns you want
columns=['Close']
folder_path = "./20Num2Years"

math_op(columns,folder_path)