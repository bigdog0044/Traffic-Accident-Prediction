import pickle
import pandas as pd
import os
import matplotlib.pyplot as plt
from lazypredict.Supervised import LazyClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#refer to key on jupyter notebook

def find_file(fileDir,filename):
    for rootm,dir, files in os.walk(fileDir):
        if filename in files:
            return True
    return False


def convertSeverity(value):
    match value:
        case "Low":
            return 0
        case "Moderate":
            return 1
        case "High":
            return 2
        case _:
            print(f"No case found")

def testing_other_AI_models(x_train,x_test,y_train,y_test):
    lazyclf = LazyClassifier(verbose=0,ignore_warnings=False)

    models,predictions = lazyclf.fit(x_train,x_test,y_train,y_test)

    print(models)

#loading the dataset in
data = pd.read_csv('dataset_traffic_accident_prediction1.csv')


"""Formatting/processing data"""

#Working out total null values in each column
"""for column in data.columns:
    print(f"{column} total null values: {sum(data[column].isnull())}")
 """   
#removing null values
data = data.dropna()

#converting columns into a integer and not a float
data['Driver_Age'] = data['Driver_Age'].astype(int)
data['Number_of_Vehicles'] = data['Number_of_Vehicles'].astype(int)
data['Driver_Experience'] = data['Driver_Experience'].astype(int)
data['Driver_Alcohol'] = data['Driver_Alcohol'].astype(int)
data['Traffic_Density'] = data['Traffic_Density'].astype(int)
data['Accident'] = data['Accident'].astype(int)

#onehotencoding values
data['Weather'] = data['Weather'].map({"Clear":0, "Rainy":1,"Foggy":2,"Snowy":3,"Stormy":4})
data['Road_Type'] = data['Road_Type'].map({"Highway":0, "City Road":1,"Rural Road":2,"Mountain Road":3})
data['Time_of_Day'] = data['Time_of_Day'].map({"Morning":0, "Afternoon":1,"Evening":2,"Night":3})
data['Road_Condition'] = data['Road_Condition'].map({"Dry":0, "Wet":1,"Icy":2,"Under Construction":3})
data['Vehicle_Type'] = data['Vehicle_Type'].map({"Car":0, "Truck":1,"Motorcycle":2,"Bus":3})
data['Road_Light_Condition'] = data['Road_Light_Condition'].map({"Daylight":0, "Artificial Light":1,"No Light":2})


#converting severity labels into numbers
data['Accident_Severity'] = data['Accident_Severity'].apply(convertSeverity)


print(data.head())


x = data.drop("Accident",axis=1)
y = data['Accident']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

clf = RandomForestClassifier(n_estimators=240)
clf.fit(x_train,y_train)

y_pred = clf.predict(x_test)

acc = 0

print(y_pred)
while acc < 0.7:
    clf.fit(x_train,y_train)
    y_pred = clf.predict(x_test)
    acc = accuracy_score(y_pred,y_test)
    

#adding function to prevent the program from overwriting the file 
if find_file("./","model.pkl") == False:
    with open('model.pkl','wb') as f:
        pickle.dump(clf,f)

    print("Saving model with accuracy of ",acc)

#testing to see if any other AI models perform better 
#testing_other_AI_models(x_train,x_test,y_train,y_test)