from flask import Flask
from flask import render_template
from flask import request
import pickle


app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def main(name =None):

    formData = gettingFormInfo()
    print(formData)
    #AI(formData)
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

            return [driverAge,numVechicles,driverExperience,consumedAlcohol,trafficDensity,weather,roadType,timeOfDay,roadCondition,vehicleType,roadLightCondition]


def AI(data):
     model = pickle.load(open("model.pkl","rb"))
     print(model.predict(data))
if __name__ == "__main__":
    app.run()