from flask import Flask
from flask import request
from flask import render_template
from flask import current_app
import pickle
import numpy as np
#from validateData import validData
app = Flask(__name__)

def AIProcessing( age, totalVehicle, experience, alcoholConsumption, trafficDensity, weather, roadType,
            timeOfDay, roadCondition, vehicleType, roadLightCondition, speedLimit, accidentSeverity):
    model = pickle.load(open("model.pkl", "rb"))
    data = np.array([weather, roadType, timeOfDay,trafficDensity,
                speedLimit, totalVehicle, alcoholConsumption, accidentSeverity,
                roadCondition, vehicleType, age, experience,
                roadLightCondition])
    print(data)
    result = model.predict(data.reshape(-1,1))
    print(result)
    return 0

#@app.route("/sendInfo", methods=["POST", "GET"])
def validData(ageInput,numVecInput,experienceInput,speedInput):
    if ageInput == "" or numVecInput == "" or experienceInput == "" or speedInput == "":
        return "Error: form inputs are blank. Please enter data"
    try:
        
        if int(ageInput) < 0 or int(numVecInput) < 0 or int(experienceInput) < 0 or int(speedInput) < 0:
            return "Error: inputs can't be negative"
    except ValueError:
        return "Error: incorrect format detected. Enter only numbers as the input values"
    
    return None #None is used to indicate no error has happened

@app.route("/", methods=["POST", "GET"])
def mainPage(name=None):
    if request.method == "GET":
        print("using GET method")
        return render_template('form.html')
    else:
        print("not using get method")
        error = validData(request.form.get('driverAge'),
            request.form.get('numVechicle'),
                request.form.get('experience'), 
                    request.form.get('speed_limit'))
        if error == None:
            age = request.form.get('driverAge')
            totalVehicle = int(request.form.get('numVechicle'))
            experience = int(request.form.get('experience'))
            alcoholConsumption = int(request.form.get('alcohol-yes-or-no'))
            trafficDensity = int(request.form.get('traffic-density'))
            weather = int(request.form.get('weather'))
            roadType = int(request.form.get('road_type'))
            timeOfDay = int(request.form.get('time_of_day'))
            roadCondition = int(request.form.get('road_condition'))
            vehicleType = int(request.form.get('vehicle_type'))
            roadLightCondition = int(request.form.get('road_light_condition'))
            speedLimit = int(request.form.get('speed_limit'))
            accidentSeverity = int(request.form.get('accident_severity'))
            
            
            AIProcessing(age, totalVehicle, experience, alcoholConsumption, trafficDensity, weather,
                         roadType, timeOfDay, roadCondition, vehicleType, roadLightCondition,
                         speedLimit, accidentSeverity)
            #add stuff here that gets returned by the AI algorithm
            return render_template("form.html", result = 1)
        else:
            return render_template("form.html", errorMSG=error)
        

#used to serve css files
@app.route('/styles')
def css():
    return current_app.send_static_file("style.css")

if __name__ == "__main__":
    app.run(debug=True)
    
#used to help validate errors within the data