# Food Delivery Time Prediction

## Project Description
This project predicts the time required to deliver a food order using Machine Learning.

The model uses different factors such as traffic level, weather, road distance, rider experience, restaurant preparation time, and other delivery-related information to predict the delivery time in minutes.

## Technologies Used
- Python
- Machine Learning
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- HTML
- JavaScript

## Dataset
The project uses a food delivery dataset containing 50,000 records and 24 columns.

The dataset includes information about:
- Order details
- Weather conditions
- Pickup and drop-off zones
- Rider experience and ratings
- Restaurant ratings
- Traffic conditions
- Road distance
- Preparation time
- Delivery time

**Target Variable:** `Time_taken_min`

## Model Training
The Machine Learning model was trained using the collected dataset.

The training process includes:
1. Data Collection
2. Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Model Saving

The trained model is saved as `delivary_time.pkl` and used by the FastAPI backend for predictions.

## Project Structure

```text
Food-Delivery-Prediction/
│
├── main.py
├── delivary_time.pkl
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── training/
│   └── food.ipynb
│
└── dataset/
    └── Food_Delivery_Time_Prediction.csv
```

## How to Run the Project

### 1. Install the required packages

```bash
pip install -r requirements.txt
```

### 2. Start the FastAPI application

```bash
uvicorn main:app --reload
```

### 3. Open the application

Open the following URL in your browser:

```text
http://127.0.0.1:8000/
```

### 4. API Documentation

FastAPI provides interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

## Application Workflow

1. User enters delivery details through the HTML frontend.
2. JavaScript collects the input values.
3. The input data is sent to the FastAPI backend.
4. FastAPI passes the input to the trained Machine Learning model.
5. The model predicts the delivery time.
6. The prediction is displayed on the webpage.

## Project Objective

The main objective of this project is to estimate food delivery time using Machine Learning and provide predictions through a web application.

---

**Project:** Food Delivery Time Prediction  
**Backend:** FastAPI  
**Frontend:** HTML and JavaScript  
**Model:** Machine Learning