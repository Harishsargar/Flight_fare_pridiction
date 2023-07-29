
    
from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd


app = Flask(__name__)
model = pickle.load(open('c2_1_flight_rf.pkl', "rb"))
    
    
    #_ _ _ _ _Harish Sargar_ _ _ _ _

@app.route("/")
@cross_origin()
def home():
    return render_template("flight.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure_time
        
        Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_minute = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        # print("Departure : ",Dep_hour, Dep_min)

    
        # Duration
       
        total_minutes = int(request.form["duration"])
        

        # Total Stops
        Total_Stop = int(request.form["total_stops"])
        # print(Total_stops)



        airline=request.form['airline']
        if(airline=='Jet Airways'):
            airline_Encoded=1

        elif (airline=='IndiGo'):
            airline_Encoded=2

        elif (airline=='Air India'):
            airline_Encoded=3
            
        elif (airline=='Multiple carriers'):
            airline_Encoded=4
            
        elif (airline=='SpiceJet'):
            airline_Encoded=5
            
        elif (airline=='Vistara'):
            airline_Encoded=6
        
        elif (airline=='Air Asia'):
            airline_Encoded=7

        elif (airline=='GoAir'):
            airline_Encoded=8
            
        elif (airline=='Multiple carriers Premium economy '):
            airline_Encoded=9
            
        elif (airline=='Jet Airways Business'):
            airline_Encoded=10

        elif (airline=='Vistara Premium economy '):
            airline_Encoded=11

        elif (airline=='Trujet'):
            airline_Encoded=12

        Source = request.form["source"]
        if (Source == 'Delhi'):
            Source_Encoded=1

        elif (Source == 'Kolkata'):
            Source_Encoded=2

        elif (Source == 'Banglore'):
            Source_Encoded=3
            
        elif (Source == 'Mumbai'):
            Source_Encoded=4   

        elif (Source == 'Chennai'):
            Source_Encoded=5

        
        Source = request.form["destination"]
        if (Source == 'Cochin'):
            Destination_Encoded=6
            
        elif (Source == 'Banglore'):
            Destination_Encoded=7
        
        elif (Source == 'Delhi'):
            Destination_Encoded=8
            
        elif (Source == 'New Delhi'):
            Destination_Encoded=9

        elif (Source == 'Hyderabad'):
            Destination_Encoded=10

        elif (Source == 'Kolkata'):
            Destination_Encoded=11



        prediction=model.predict([[journey_day, journey_month,
   Dep_minute, Dep_hour, total_minutes, airline_Encoded,
   Source_Encoded, Destination_Encoded, Total_Stop        ]])

        output=round(prediction[0],2)

        return render_template('flight.html',prediction_text="Your Flight price is Rs. {}".format(output))


    return render_template("flight.html")




if __name__ == "__main__":
    app.run(debug=True)
