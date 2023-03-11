import os
import pandas as pd
def merge_csv(folder_path):
    file_list = os.listdir(folder_path)
    print(file_list)
    df_merged = pd.DataFrame(columns=['Date'])
    df_merged=df_merged[['Date']]
    for i in file_list:
        df = pd.read_csv(folder_path+"/"+i)
        stock_name=i.split(".csv")[0]
        df = df.rename(columns={"Close": f"Close_{stock_name}"})
        df_merged = pd.merge(df_merged, df[['Date', f"Close_{stock_name}"]], on='Date', how='outer')
    df_merged=df_merged.sort_values('Date').fillna(0)
    print(df_merged)
    df_merged.to_csv("Q1_master.csv",index=False)

folder_path = "./20Num2Years"
merge_csv(folder_path)