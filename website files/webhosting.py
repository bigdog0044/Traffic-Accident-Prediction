from flask import Flask
from flask import render_template
from flask import request
import pickle
import numpy as np


app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def main(name =None):

    formData = np.array(gettingFormInfo())

    formData = formData.reshape(1,-1)
    print(formData)
    AI(formData)
    return render_template('index.html',person=name)


@app.route('/', methods=["POST"])
def gettingFormInfo():
        if request.method == "POST":
            driverAge = request.form.get("driverAge")
            numVechicles = request.form.get("numVechicle")
            driverExperience = request.form.get("experience")

            #validating userinput, this will be changed later on in the future
            if driverAge == "" or int(driverAge) < 0 or numVechicles == "" or int(numVechicles) < 0 or driverExperience == "" or int(driverExperience):
                driverAge = 0
                numVechicles = 0
                driverExperience = 0
            
            consumedAlcohol = int(request.form.get("alcohol-yes-or-no"))
            trafficDensity = int(request.form.get("traffic-density"))
            weather = int(request.form.get("weather"))
            roadType = int(request.form.get("road_type"))
            timeOfDay = int(request.form.get("time_of_day"))
            roadCondition = int(request.form.get("road_condition"))
            vehicleType = int(request.form.get("vehicle_type"))
            roadLightCondition = int(request.form.get("road_light_condition"))
            accidentSeverity = int(request.form.get("accident_severity"))
            speedLimit = int(request.form.get("speed_limit"))


            return [weather,roadType,timeOfDay,speedLimit,numVechicles,consumedAlcohol,accidentSeverity,roadCondition,vehicleType,driverAge,driverExperience,roadLightCondition]
            #return [driverAge,numVechicles,driverExperience,consumedAlcohol,trafficDensity,weather,roadType,timeOfDay,roadCondition,vehicleType,roadLightCondition,accidentSeverity,speedLimit]


def AI(data):
     model = pickle.load(open("model.pkl","rb"))
     #checks to make sure that blank data is not being predicted by the AI
     """if len(data[0]) != 1:
        print(model.predict(data.reshape(1,-1)))"""


#main method
if __name__ == "__main__":
    app.run()