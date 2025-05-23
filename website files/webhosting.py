from flask import Flask
from flask import request
from flask import render_template
from flask import current_app
#from validateData import validData
app = Flask(__name__)

#@app.route("/sendInfo", methods=["POST", "GET"])
def validData(ageInput,numVecInput,experienceInput,speedInput):
    if ageInput == "" or numVecInput == "" or experienceInput == "" or speedInput == "":
        return "Error: form inputs are blank. Please enter data"
    try:
        
        if int(ageInput) < 0 or int(numVecInput) < 0 or int(experienceInput) < 0 or int(speedInput) < 0:
            return "Error: inputs can't be negative"
    except ValueError:
        return "Error: incorrect format detected. Enter only numbers as the input values"
    return None

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
        print(error)
        if error == None:
            #add stuff here that gets returned by the AI algorithm
            return render_template("form.html")
        else:
            return render_template("errorForm.html", errorMSG=error)
        

#used to serve css files
@app.route('/styles')
def css():
    return current_app.send_static_file("style.css")

if __name__ == "__main__":
    app.run(debug=True)
    
#used to help validate errors within the data