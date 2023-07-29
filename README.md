# Flight_fare_pridiction

This project aims to predict the flight fares based on various features such as journey date, departure time, duration of flight, airline, source, destination, and total stops.

Table of Contents
1.	Introduction
2.	Dataset
3.	Installation
4.	Usage
5.	Model Training
6.	Evaluation
7.	Contributing
8.	License
Introduction
Flight fare prediction is a machine learning project that utilizes historical flight data to build a regression model that can predict the fare for a given flight journey. The model is trained on a dataset containing various features that are known to influence the flight fare.

Dataset
The dataset used for this project contains the following columns:
•	Journey Date: The date of the flight journey.
•	Departure Time: The departure time of the flight in 24-hour format.
•	Duration of Flight: The duration of the flight in hours and minutes.
•	Airline: The airline company operating the flight.
•	Source: The source city from where the flight departs.
•	Destination: The destination city of the flight.
•	Total Stops: The total number of stops during the journey.
To use the trained model for flight fare prediction, you can make use of the provided web application. 

Open your web browser and go to http://localhost:5000 to access the web application.

Fill in the flight details in the form and click on the "Predict" button.

The web application will display the predicted flight fare based on the input provided.

Model Training
The machine learning model for flight fare prediction is trained using the scikit-learn library. The data preprocessing, feature selection, and hyperparameter tuning are performed to optimize the model's performance.

Evaluation
The model's performance is evaluated using various metrics such as mean absolute error, mean squared error, and R-squared value. The best model is selected based on its performance on a hold-out validation set.

Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.


By following the instructions provided in the README.md file, users will be able to understand the purpose of the project, its dataset, and how to use the provided web application for flight fare prediction. It also outlines the steps to run the project locally, contributing guidelines, and licensing information.
