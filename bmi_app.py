import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="BMI Circular Tracker", page_icon="🎯")

st.title("🎯 Circular BMI Tracker")

# Sidebar Inputs
with st.sidebar:
    st.header("Your Details")
    weight = st.number_input("Weight (kg)", min_value=1.0, value=75.0, step=0.1)
    height = st.number_input("Height (m)", min_value=0.5, value=1.75, step=0.01)

# BMI Calculation Logic
if height > 0:
    bmi = round(weight / (height ** 2), 2)
    
    # Determine Category and Color
    if bmi < 18.5:
        category, color = "Underweight", "#3498db" # Blue
    elif 18.5 <= bmi < 25:
        category, color = "Normal", "#2ecc71"      # Green
    elif 25 <= bmi < 30:
        category, color = "Overweight", "#f1c40f"  # Yellow
    else:
        category, color = "Obese", "#e74c3c"       # Red

    # Create the Circular Gauge
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = bmi,
        title = {'text': f"Category: {category}", 'font': {'size': 24}},
        gauge = {
            'axis': {'range': [10, 45], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "black"}, # The needle/pointer color
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [10, 18.5], 'color': "#3498db"}, # Blue
                {'range': [18.5, 25], 'color': "#2ecc71"}, # Green
                {'range': [25, 30], 'color': "#f1c40f"},   # Yellow
                {'range': [30, 45], 'color': "#e74c3c"}    # Red
            ],
            'threshold': {
                'line': {'color': "white", 'width': 4},
                'thickness': 0.75,
                'value': bmi
            }
        }
    ))

    fig.update_layout(height=400, margin=dict(l=20, r=20, t=50, b=20))

    # Display in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # Summary box
    st.info(f"Your BMI is **{bmi}**, which puts you in the **{category}** category.")
