import streamlit as st
import pandas as pd
import joblib
from io import BytesIO

# --- Custom CSS for Premium Design ---
# Implements glassmorphism, gradient text, centered layout, and custom components.
# Uses a dark theme with teal/cyan accents.
custom_css = """
<style>
    /* 1. Global Page Configuration & Centering */
    .main {
        background: linear-gradient(135deg, #1f2833 0%, #0d121c 100%);
        color: #E5E7EB; /* Light text for dark background */
        font-family: 'Inter', sans-serif;
    }
    .stApp {
        max-width: 1200px;
        margin: auto;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1, h2, h3, h4 {
        color: #FFFFFF;
    }

    /* 2. Gradient App Title */
    .app-title {
        font-size: 3rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #00C9FF, #92FE9D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.05em;
        text-align: center;
        padding-bottom: 0.5rem;
    }
    
    /* 3. Glassmorphic Card Styling (Inputs) */
    .stContainer {
        border-radius: 16px;
        background: rgba(255, 255, 255, 0.05);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    .stContainer:hover {
        box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.5);
    }
    
    /* 4. Custom Button Styling (Predict) */
    div.stButton > button {
        width: 100%;
        border: none;
        border-radius: 12px;
        padding: 10px 24px;
        font-size: 1.2rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        background: linear-gradient(90deg, #00C9FF 0%, #92FE9D 100%);
        color: #0d121c; /* Dark text for contrast */
        box-shadow: 0 4px 15px rgba(0, 201, 255, 0.4);
    }
    div.stButton > button:hover {
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0 8px 25px rgba(146, 254, 157, 0.6);
    }
    
    /* 5. Custom Success/Result Styling */
    .stSuccess > div {
        border-radius: 12px;
        background-color: rgba(146, 254, 157, 0.1);
        border-left: 5px solid #92FE9D;
        padding: 20px;
        color: #92FE9D;
        font-size: 1.1rem;
        font-weight: 600;
        margin-top: 15px;
    }
    
    /* 6. Footer Styling */
    .footer {
        text-align: center;
        margin-top: 40px;
        padding-top: 15px;
        border-top: 1px solid rgba(255, 255, 255, 0.05);
        color: #9CA3AF;
        font-size: 0.85rem;
    }
    
    /* 7. Input/Select Box Label Styling */
    .st-dl {
        font-weight: 500;
        color: #FFFFFF;
    }

</style>
"""

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# -----------------------------
# Placeholder for Model Loading
# NOTE: The joblib file must be present in the execution environment.
# Since we cannot save a dummy file here, we will mock the model object
# to ensure the script runs without error in the provided environment.
# -----------------------------
try:
    # Attempt to load the actual model (if available)
    model = joblib.load("xgboost_price_model.pkl")
except:
    # Mock model for execution environment where the file is missing
    class MockModel:
        def predict(self, df):
            # Simple mock prediction based on area for demonstration
            return [df['area'].iloc[0] * 50 + 1000000] # ₹5000/sqft base price logic

    model = MockModel()
    st.warning("⚠️ **Model File Not Found:** Using a mock predictor function to demonstrate the UI. Upload `random_forest_price_model.pkl` for real predictions.")


st.set_page_config(page_title="🏠 House Price Predictor", page_icon="🏡", layout="wide")

# -----------------------------
# App Title & Description (Gradient Text)
# -----------------------------
st.markdown('<div class="app-title">Predict Your Dream Home Price 💸</div>', unsafe_allow_html=True)
st.markdown(
    """
    <p style='text-align: center; color: #9CA3AF; font-size: 1.1rem;'>
    Enter the key specifications of the property below to generate an accurate price estimate.
    </p>
    """, unsafe_allow_html=True
)

st.divider()

# -----------------------------
# User Inputs
# -----------------------------
st.header("✨ Property Specifications")

# Use a styled container to wrap the input columns
with st.container():
    st.markdown('<div class="stContainer">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    # --- Column 1: Core Metrics ---
    with col1:
        st.subheader("📐 Core Metrics")
        area = st.number_input("Area (in sq. ft.)", min_value=500, max_value=20000, value=5000, help="Total livable area of the property.")
        bedrooms = st.number_input("🛏️ Bedrooms", min_value=1, max_value=10, value=3, help="Number of bedrooms.")
        bathrooms = st.number_input("🛁 Bathrooms", min_value=1, max_value=5, value=2, help="Number of full bathrooms.")
        stories = st.number_input("🏢 Stories", min_value=1, max_value=5, value=2, help="Number of floors/stories.")

    # --- Column 2: Location & Amenities 1 ---
    with col2:
        st.subheader("📍 Location & Comfort")
        mainroad = st.selectbox("🛣️ Main Road Access", ["Yes", "No"], help="Is the property connected to a main road?")
        guestroom = st.selectbox("🚪 Guest Room", ["Yes", "No"], help="Does the property include a dedicated guest room?")
        basement = st.selectbox("🕳️ Basement", ["Yes", "No"], help="Does the property have a basement?")
        hotwaterheating = st.selectbox("♨️ Hot Water Heating", ["Yes", "No"], help="Is there a dedicated hot water heating facility?")

    # --- Column 3: Convenience & Luxury ---
    with col3:
        st.subheader("💎 Features & Parking")
        airconditioning = st.selectbox("❄️ Air Conditioning", ["Yes", "No"], help="Is central air conditioning installed?")
        parking = st.slider("🚗 Parking Spaces", 0, 4, 2, help="How many car parking spaces are available?")
        prefarea = st.selectbox("⭐ Preferred Area", ["Yes", "No"], help="Is the property located in a highly preferred residential area?")

    st.markdown('</div>', unsafe_allow_html=True) # Close the custom container

st.divider()

# -----------------------------
# Data Preprocessing
# -----------------------------
def yes_no_to_int(x):
    return 1 if x == "Yes" else 0

input_dict = {
    "area": area,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "stories": stories,
    "mainroad": yes_no_to_int(mainroad),
    "guestroom": yes_no_to_int(guestroom),
    "basement": yes_no_to_int(basement),
    "hotwaterheating": yes_no_to_int(hotwaterheating),
    "airconditioning": yes_no_to_int(airconditioning),
    "parking": parking,
    "prefarea": yes_no_to_int(prefarea)
}

input_df = pd.DataFrame([input_dict])

# -----------------------------
# Predict button and Output
# -----------------------------
st.header("⬇️ Generate Estimate")
predict_col, _ = st.columns([1, 2])

with predict_col:
    if st.button("🔮 Predict Price"):
        # Prediction Logic
        try:
            price_pred = model.predict(input_df)[0]
            
            # Custom styled output
            st.markdown(
                f"""
                <div class="stSuccess">
                    <div>
                        <p style='margin: 0; font-size: 1.1rem;'>
                            Estimated House Price:
                        </p>
                        <p style='font-size: 2.2rem; font-weight: 800; margin: 0; padding-top: 5px;'>
                            ₹{price_pred:,.0f}
                        </p>
                    </div>
                </div>
                """, unsafe_allow_html=True
            )
            st.balloons()
            
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    """
    <div class="footer">
        Built with ❤️ using Streamlit, Pandas, and Scikit-Learn. | Designed for premium UX.
    </div>
    """, unsafe_allow_html=True
)
