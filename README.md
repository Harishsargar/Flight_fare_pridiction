# Flight Fare Prediction

This project aims to predict the flight fares based on various features such as journey date, departure time, duration of flight, airline, source, destination, and total stops.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Flight fare prediction is a machine learning project that utilizes historical flight data to build a regression model that can predict the fare for a given flight journey. The model is trained on a dataset containing various features that are known to influence the flight fare.

## Dataset

The dataset used for this project contains the following columns:

- `Journey Date`: The date of the flight journey.
- `Departure Time`: The departure time of the flight in 24-hour format.
- `Duration of Flight`: The duration of the flight in hours and minutes.
- `Airline`: The airline company operating the flight.
- `Source`: The source city from where the flight departs.
- `Destination`: The destination city of the flight.
- `Total Stops`: The total number of stops during the journey.

## Installation

To run this project locally, follow these steps:

1. Clone this repository to your local machine:
```bash
https://github.com/Harishsargar/Flight_fare_pridiction.git

```
2. Install the required dependencies:


3. Download the dataset and place it in the project directory.

## Usage

To use the trained model for flight fare prediction, you can make use of the provided web application. Follow the steps below:

1. Run the Flask web application:
```
python app.py

```

2. Open your web browser and go to `http://localhost:5000` to access the web application.

3. Fill in the flight details in the form and click on the "Predict" button.

4. The web application will display the predicted flight fare based on the input provided.

## Model Training

The machine learning model for flight fare prediction is trained using the scikit-learn library. The data preprocessing, feature selection, and hyperparameter tuning are performed to optimize the model's performance.

## Evaluation

The model's performance is evaluated using various metrics such as mean absolute error, mean squared error, and R-squared value. The best model is selected based on its performance on a hold-out validation set.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

By following the instructions provided in the `README.md` file, users will be able to understand the purpose of the project, its dataset, and how to use the provided web application for flight fare prediction. It also outlines the steps to run the project locally, contributing guidelines, and licensing information.
