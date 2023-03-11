import pandas as pd
def compare():
    df=pd.read_csv('Q4_stock_prediction.csv')
    df['Difference']=round((df['Real price'] - df['Predicted price']),3)
    df['Percentage']=df['Difference']/df['Predicted price']
    print(df[['Name','Percentage']])
    df.to_csv("Q5_compareREALvsPRED.csv",index=False)
# this function will provide us we a csv in which we can check the percentage difference between the real price and predicted price
compare()


'''
For better accuracy,

We can have more historic data.

Adding indicator values while training (EMA, RSI, MACD).

Trying different models for better accuracy

Adding a variable that has the average of the last 10 values

'''