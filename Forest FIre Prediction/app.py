import streamlit as st
import pickle
import numpy as np
import pandas as pd
import warnings

# Suppress sklearn version and validation warnings for unpickled models
warnings.filterwarnings('ignore', category=UserWarning, module='sklearn')
warnings.filterwarnings('ignore', message='.*Trying to unpickle estimator.*')

# Set page config
st.set_page_config(
    page_title="Forest Fire Prediction",
    page_icon="🔥",
    layout="centered"
)

# Load the model
@st.cache_resource
def load_model():
    try:
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        st.error("Model file (model.pkl) not found. Please ensure the model is in the same directory.")
        return None

# Title and description
st.title("🔥 Forest Fire Prediction System")
st.markdown("---")
st.markdown("Enter environmental conditions to predict the likelihood of a forest fire occurrence.")

# Load model
model = load_model()

if model is not None:
    # Create input form
    with st.form("prediction_form"):
        st.subheader("Environmental Parameters")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            oxygen = st.number_input(
                "Oxygen Level (%)",
                min_value=0.0,
                max_value=100.0,
                value=50.0,
                step=1.0,
                help="Oxygen percentage in the environment"
            )
        
        with col2:
            temperature = st.number_input(
                "Temperature (°C)",
                min_value=0.0,
                max_value=100.0,
                value=30.0,
                step=1.0,
                help="Ambient temperature"
            )
        
        with col3:
            humidity = st.number_input(
                "Humidity (%)",
                min_value=0.0,
                max_value=100.0,
                value=30.0,
                step=1.0,
                help="Humidity percentage in the environment"
            )
        
        st.markdown("---")
        submit_button = st.form_submit_button("Predict Fire Risk", use_container_width=True)
    
    # Make prediction when form is submitted
    if submit_button:
        # Prepare input data as DataFrame with feature names (matches training data)
        input_data = pd.DataFrame({
            'Oxygen': [oxygen],
            'Temperature': [temperature],
            'Humidity': [humidity]
        })
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        
        # Display results
        st.markdown("### Prediction Results")
        
        # Determine fire risk level
        if prediction >= 0.7:
            risk_level = "🔴 HIGH RISK"
            risk_color = "danger"
            message = f"Fire occurrence probability: **{prediction:.2%}**"
            st.error(risk_level)
        elif prediction >= 0.4:
            risk_level = "🟡 MODERATE RISK"
            risk_color = "warning"
            message = f"Fire occurrence probability: **{prediction:.2%}**"
            st.warning(risk_level)
        else:
            risk_level = "🟢 LOW RISK"
            risk_color = "success"
            message = f"Fire occurrence probability: **{prediction:.2%}**"
            st.success(risk_level)
        
        st.markdown(message)
        
        # Show input summary
        with st.expander("View Input Summary"):
            input_df = pd.DataFrame({
                'Parameter': ['Oxygen (%)', 'Temperature (°C)', 'Humidity (%)'],
                'Value': [oxygen, temperature, humidity]
            })
            st.dataframe(input_df, width='stretch', hide_index=True)
        
        # Fire prevention tips
        if prediction >= 0.5:
            st.markdown("---")
            st.markdown("### 🛡️ Fire Prevention Recommendations")
            st.info("""
            - Monitor conditions closely and implement fire prevention measures
            - Ensure fire-fighting equipment is ready and accessible
            - Consider implementing temporary restrictions on activities that could spark fires
            - Maintain clear communication channels for emergency response
            - Check weather forecasts regularly for changing conditions
            """)

# Sidebar information
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This application uses a machine learning model to predict forest fire occurrence based on:
    - **Oxygen Level**: Percentage of oxygen in the environment
    - **Temperature**: Ambient temperature in Celsius
    - **Humidity**: Percentage of humidity in the environment
    
    The model outputs a probability score indicating the likelihood of a fire occurrence.
    """)
    
    st.markdown("---")
    st.markdown("### 📊 Risk Levels")
    st.markdown("""
    - **🟢 LOW**: 0% - 40% probability
    - **🟡 MODERATE**: 40% - 70% probability
    - **🔴 HIGH**: 70% - 100% probability
    """)
