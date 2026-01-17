# 🔥 Forest Fire Prediction

A machine learning model to predict forest fire occurrence based on environmental conditions (Oxygen, Temperature, and Humidity).

## Features

- Predicts forest fire risk based on environmental parameters
- Interactive web interface using Streamlit
- Real-time risk assessment with visual indicators
- Fire prevention recommendations

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Web Application

1. Navigate to the project directory:
```bash
cd "Forest FIre Prediction"
```

2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. The application will open in your default web browser automatically. If not, navigate to the URL shown in the terminal (typically `http://localhost:8501`)

## Usage

1. Enter the environmental parameters:
   - **Oxygen Level**: Percentage of oxygen (0-100%)
   - **Temperature**: Ambient temperature in Celsius (0-100°C)
   - **Humidity**: Humidity percentage (0-100%)

2. Click the **"Predict Fire Risk"** button

3. View the prediction results:
   - **🟢 LOW RISK**: 0-40% probability
   - **🟡 MODERATE RISK**: 40-70% probability
   - **🔴 HIGH RISK**: 70-100% probability

## Model Information

- **Algorithm**: Linear Regression
- **Input Features**: Oxygen (%), Temperature (°C), Humidity (%)
- **Output**: Fire occurrence probability (0-1)

## Deployment

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md).

**Quick Deploy to Streamlit Cloud (Recommended):**
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub and deploy your app
4. Set main file path: `Forest FIre Prediction/app.py`

Your app will be live in minutes! 🚀

## Files

- `app.py` - Streamlit web application
- `model.pkl` - Trained machine learning model
- `forest_fire.csv` - Training dataset
- `Forest Fire Prediction.ipynb` - Jupyter notebook with model training code
- `requirements.txt` - Python dependencies