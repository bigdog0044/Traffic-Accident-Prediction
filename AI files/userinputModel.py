import pickle

model = pickle.load(open('model.pkl','rb'))

#gives the models prediction on the user's input
def predictInput(age,numVechicle,driverExperienc,driverAlcohol,trafficDensity,weatherCondiction, roadType)


while True:
    