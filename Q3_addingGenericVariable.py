import os
import pandas as pd
def add_Gen(folder_path):
    df_NIFTY = pd.read_csv(folder_path+"/^NSEI.csv", index_col='Date')
    df_NIFTYBANK = pd.read_csv(folder_path+"/^NSEBANK.csv", index_col='Date')
    df_NIFTY = df_NIFTY.rename(columns={"Close": "Close_NIFTY"})
    df_NIFTYBANK = df_NIFTYBANK.rename(columns={"Close": "Close_NIFTYBANK"})

    file_list = os.listdir(folder_path)
    print(file_list)
    df_merged = pd.DataFrame(columns=['Date'])
    df_merged=df_merged[['Date']]
    for i in file_list:
        df = pd.read_csv(folder_path+"/"+i)
        df_merged = pd.merge(df, df_NIFTY['Close_NIFTY'], on='Date')
        df_merged = pd.merge(df_merged, df_NIFTYBANK['Close_NIFTYBANK'], on='Date')
        stock_name=i.split(".csv")[0]

        df_merged.to_csv("./Q3_WithGEN/"+stock_name+"_gen.csv",index=False)

folder_path = "./20Num2Years"
add_Gen(folder_path)