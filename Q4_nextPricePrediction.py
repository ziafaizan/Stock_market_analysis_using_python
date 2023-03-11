import os
import pandas as pd
from sklearn.linear_model import LinearRegression

def predictPrice(folder_path):
    file_list = os.listdir(folder_path)
    print(file_list)
    df=pd.DataFrame(columns=['Name','Predicted price','Real price'])
    for i in file_list:
        stock_data = pd.read_csv(folder_path+"/"+i).dropna()
        X = stock_data.drop(['Date', 'Close'], axis=1)
        y = stock_data['Close']
        # here I have removed the last value for training,so that we can find analyse our model according to the last value
        X_train, y_train = X[:len(X)-1], y[:len(X)-1]
        X_test, y_test = X[len(X)-1:], y[len(X)-1:]
        model = LinearRegression()
        model.fit(X_train, y_train)
        next_day_price = model.predict(X_test)
        df.loc[len(df.index)] = [i.split(".csv")[0], next_day_price[0], y_test.iloc[0]] 
    print(df)
    df.to_csv("Q4_stock_prediction.csv",index=False)
# here i have used data with  generic level variables
folder_path = "./Q3_WithGEN"
predictPrice(folder_path)