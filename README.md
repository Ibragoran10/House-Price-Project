#  House Price Prediction Project

This repository contains a complete end-to-end Machine Learning project that analyzes and predicts house prices using historical data from India. It features a full data exploration workflow and a live web application for interactive predictions.

##  Repository Structure

* `Notebook.ipynb`: The Jupyter Notebook containing Data Cleaning, Exploratory Data Analysis (EDA), Feature Engineering, and Model Training.
* `House price india.csv`: The historical dataset used for training and testing the machine learning model.
* `model.pkl`: The final trained and optimized machine learning model serialized using Joblib.
* `app.py`: The Streamlit web application that serves as the user interface for the model.

##  Features
* **Exploratory Data Analysis:** Comprehensive charts and data insights in the Jupyter notebook.
* **Interactive Web App:** Easy-to-use sliders and inputs to calculate real-time price predictions.
* **Optimized ML Pipeline:** The model processes inputs smoothly using Python's data science ecosystem.

##  App Inputs (Features)
The web application accepts the following house characteristics to forecast the price:
1. **Number of Bedrooms**
2. **Number of Bathrooms**
3. **Living Area** (Square footage)
4. **Condition of the House**
5. **Number of Schools Nearby**

##  Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ibragoran10/House-Price-Project.git
