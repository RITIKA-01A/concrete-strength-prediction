# 🏗️ Concrete Strength Prediction

This project predicts the **compressive strength of concrete** based on its ingredient composition using a machine learning regression model. The model is trained on historical data and deployed using **Render**.


## 📌 Problem Statement

Accurate prediction of concrete strength is essential in civil engineering to ensure both safety and cost-efficiency. This project uses features like cement, fly ash, water, aggregate, and age to predict compressive strength (in MPa).


## 🧪 Input Features

- Cement (kg/m³)
- Blast Furnace Slag (kg/m³)
- Fly Ash (kg/m³)
- Water (kg/m³)
- Superplasticizer (kg/m³)
- Coarse Aggregate (kg/m³)
- Fine Aggregate (kg/m³)
- Age (days)
  

## 🧠 Model Information

- **Type:** Regression
- **ML Algorithm:** (e.g., Random Forest Regressor / Linear Regression / XGBoost – specify what you used)
- **Preprocessing:** 
  - Power Transformer (`power_transformer.pkl`)
  - Scaler (`scaler.pkl`)
- **Deployment:** Flask + Render
  

## 🚀 Live Demo

🌐 [Visit the App on Render](https://concrete-strength-prediction-cg74.onrender.com)  



## 📂 Directory Structure

├── app.py # Main Flask application

├── concrete-strength-prediction-model.ipynb # Jupyter notebook for model training

├── model.pkl # Trained regression model

├── power_transformer.pkl # Power transformer used in preprocessing

├── scaler.pkl # Scaler used in preprocessing

├── requirements.txt # Python dependencies

├── templates/
│ └── index.html # HTML frontend

├── .gitignore

├── LICENSE

└── README.md



## ⚙️ How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/concrete-strength-predictor.git
   cd concrete-strength-predictor

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the Flask app:
   ```bash
   python app.py
5. Open your browser at:
   ```bash
   http://localhost:5000
   
## 📄 License

This project is licensed under the MIT License.

   





