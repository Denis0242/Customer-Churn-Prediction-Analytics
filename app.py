




import os
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📞",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# COLOR TOKENS — LIGHT + TEAL THEME
# -----------------------------
C = {
    "bg_1": "#f8fafc",
    "bg_2": "#eef4f7",
    "card": "#ffffff",
    "card_2": "#f8fbfd",
    "border": "#d9e2ec",
    "text": "#102a43",
    "muted": "#627d98",
    "blue": "#2f6fed",
    "blue_dark": "#1d4ed8",
    "teal": "#0f766e",
    "teal_light": "#ccfbf1",
    "green": "#2f855a",
    "amber": "#b7791f",
    "red": "#c53030",
    "purple": "#6b46c1"
}

STATE_LIST = [
    'OH', 'NJ', 'OK', 'AL', 'MA', 'MO', 'LA', 'WV', 'IN', 'RI',
    'IA', 'MT', 'NY', 'ID', 'VT', 'VA', 'TX', 'FL', 'CO', 'AZ',
    'SC', 'NE', 'WY', 'HI', 'IL', 'NH', 'GA', 'AK', 'MD', 'AR',
    'WI', 'OR', 'MI', 'DE', 'UT', 'CA', 'MN', 'SD', 'NC', 'WA',
    'NM', 'NV', 'DC', 'KY', 'ME', 'MS', 'TN', 'PA', 'CT', 'KS', 'ND'
]
AREA_CODES = ['415', '408', '510']

# -----------------------------
# PLOTLY STYLE HELPER
# -----------------------------
def style_plotly(fig):
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color=C["text"]),
        title_font=dict(color=C["text"]),
        xaxis=dict(showgrid=True, gridcolor="#e2e8f0", zeroline=False),
        yaxis=dict(showgrid=True, gridcolor="#e2e8f0", zeroline=False)
    )
    return fig

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
}}

.stApp {{
    background:
        radial-gradient(circle at top left, rgba(15,118,110,0.08), transparent 25%),
        radial-gradient(circle at top right, rgba(47,111,237,0.05), transparent 22%),
        linear-gradient(180deg, {C["bg_1"]} 0%, {C["bg_2"]} 100%);
    color: {C["text"]};
}}

section[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, #16324f 0%, #102a43 100%);
    border-right: 1px solid rgba(255,255,255,0.08);
}}

section[data-testid="stSidebar"] * {{
    color: white !important;
}}

.main-header {{
    font-size: 2.7rem;
    font-weight: 800;
    color: {C["text"]};
    text-align: center;
    margin-bottom: 0.35rem;
    letter-spacing: -0.03em;
}}

.sub-header {{
    font-size: 1.1rem;
    color: {C["muted"]};
    text-align: center;
    margin-bottom: 2rem;
}}

.hero-box {{
    background: linear-gradient(135deg, #ffffff 0%, #f2fffc 100%);
    border: 1px solid {C["border"]};
    border-radius: 22px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 28px rgba(16,42,67,0.08);
}}

.metric-card {{
    background: {C["card"]};
    padding: 1rem 1rem;
    border-radius: 18px;
    border: 1px solid {C["border"]};
    box-shadow: 0 8px 22px rgba(16,42,67,0.06);
    min-height: 135px;
    border-top: 4px solid {C["teal"]};
}}

.metric-card h3 {{
    margin-bottom: 0.35rem;
    color: {C["text"]};
}}

.metric-card p {{
    color: {C["muted"]};
    margin-bottom: 0;
}}

.prediction-box {{
    padding: 2rem;
    border-radius: 1rem;
    text-align: center;
    font-size: 1.5rem;
    font-weight: 800;
    border: 1px solid {C["border"]};
    box-shadow: 0 10px 24px rgba(16,42,67,0.08);
}}

.churn-yes {{
    background: #fff5f5;
    color: {C["red"]};
    border: 1px solid #f5c2c7;
}}

.churn-no {{
    background: #f0fffb;
    color: {C["teal"]};
    border: 1px solid #99f6e4;
}}

.glass-box {{
    background: {C["card_2"]};
    border: 1px solid {C["border"]};
    border-radius: 18px;
    padding: 1rem 1.2rem;
    margin-bottom: 1rem;
}}

.section-title {{
    font-size: 1.05rem;
    font-weight: 700;
    color: {C["teal"]};
    margin-bottom: 0.8rem;
}}

.small-label {{
    color: {C["teal"]};
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-weight: 700;
}}

div[data-testid="stMetric"] {{
    background: {C["card"]};
    border: 1px solid {C["border"]};
    border-radius: 18px;
    padding: 12px 16px;
    box-shadow: 0 8px 22px rgba(16,42,67,0.06);
}}

div[data-testid="stMetricLabel"] {{
    color: {C["muted"]};
    font-weight: 600;
}}

div[data-testid="stMetricValue"] {{
    color: {C["text"]};
    font-weight: 800;
}}

.stButton > button {{
    background: linear-gradient(135deg, {C["teal"]}, {C["blue"]});
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: 700;
    padding: 0.7rem 1.1rem;
    box-shadow: 0 8px 20px rgba(15,118,110,0.16);
}}

.stButton > button:hover {{
    filter: brightness(1.03);
}}

.stDownloadButton > button {{
    background: linear-gradient(135deg, {C["teal"]}, #0b5e58);
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: 700;
    padding: 0.7rem 1.1rem;
}}

div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div,
div[data-baseweb="textarea"] > div {{
    background: white !important;
    border: 1px solid {C["border"]} !important;
    border-radius: 12px !important;
    color: {C["text"]} !important;
}}

input, textarea {{
    color: {C["text"]} !important;
}}

.stNumberInput label, .stSelectbox label, .stMultiSelect label, .stFileUploader label {{
    color: {C["text"]} !important;
    font-weight: 600;
}}

[data-testid="stDataFrame"] {{
    border: 1px solid {C["border"]};
    border-radius: 16px;
    overflow: hidden;
    background: white;
}}

hr {{
    border-color: {C["border"]};
}}

.block-container {{
    padding-top: 2rem;
    padding-bottom: 2rem;
}}

.insight-pill {{
    display: inline-block;
    background: {C["teal_light"]};
    color: {C["teal"]};
    border: 1px solid #99f6e4;
    border-radius: 999px;
    padding: 0.35rem 0.8rem;
    font-size: 0.8rem;
    font-weight: 700;
    margin-right: 0.4rem;
    margin-bottom: 0.5rem;
}}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD MODEL
# -----------------------------
@st.cache_resource
def load_model():
    try:
        return joblib.load("churn_model.pkl")
    except FileNotFoundError:
        st.error("Model file not found. Please make sure 'churn_model.pkl' is in the app folder.")
        return None

# -----------------------------
# LOAD BUILT-IN PREPROCESSED BATCH DATA
# -----------------------------
@st.cache_data
def load_builtin_batch_data():
    candidate_paths = [
        os.path.join("data", "churn_preprocessed.csv"),
        "churn_preprocessed.csv",
    ]

    for path in candidate_paths:
        if os.path.exists(path):
            df = pd.read_csv(path)
            return df, path

    raise FileNotFoundError(
        "Built-in dataset not found. Expected 'data/churn_preprocessed.csv' or 'churn_preprocessed.csv'."
    )

# -----------------------------
# PREPROCESS SINGLE INPUT
# -----------------------------
def preprocess_input(input_df, feature_names):
    processed_df = pd.DataFrame(0, index=[0], columns=feature_names)

    for col in input_df.columns:
        if col in processed_df.columns:
            processed_df[col] = input_df[col].values[0]

    return processed_df

# -----------------------------
# DETECT WHETHER DATA IS ALREADY PREPROCESSED
# -----------------------------
def is_preprocessed_dataset(df, feature_names):
    feature_overlap = sum(col in df.columns for col in feature_names)
    ratio = feature_overlap / max(len(feature_names), 1)
    return ratio >= 0.6

# -----------------------------
# PREPROCESS BATCH INPUT
# -----------------------------
def preprocess_batch_data(df, feature_names):
    df_processed = df.copy()

    # If this dataset already looks like the model-ready engineered dataset,
    # just drop target-like columns and align to feature_names.
    if is_preprocessed_dataset(df_processed, feature_names):
        cols_to_drop = [c for c in ["Churn", "Churn?", "Phone"] if c in df_processed.columns]
        if cols_to_drop:
            df_processed = df_processed.drop(columns=cols_to_drop)

        for col in feature_names:
            if col not in df_processed.columns:
                df_processed[col] = 0

        return df_processed[feature_names]

    # Otherwise treat it like raw uploaded telecom churn data.
    if 'Phone' in df_processed.columns:
        df_processed = df_processed.drop('Phone', axis=1)

    if 'Churn?' in df_processed.columns:
        df_processed = df_processed.drop('Churn?', axis=1)

    if 'Churn' in df_processed.columns:
        df_processed = df_processed.drop('Churn', axis=1)

    binary_cols = ["Int'l Plan", 'VMail Plan']
    for col in binary_cols:
        if col in df_processed.columns:
            df_processed[col] = df_processed[col].map({'yes': 1, 'no': 0})

    if 'State' in df_processed.columns:
        df_processed = pd.get_dummies(df_processed, columns=['State'], prefix='State')

    if 'Area Code' in df_processed.columns:
        df_processed = pd.get_dummies(df_processed, columns=['Area Code'], prefix='AreaCode')

    if 'Day Mins' in df_processed.columns and 'Day Calls' in df_processed.columns:
        df_processed['Avg_Day_Call_Duration'] = df_processed['Day Mins'] / (df_processed['Day Calls'] + 1)

    if 'Eve Mins' in df_processed.columns and 'Eve Calls' in df_processed.columns:
        df_processed['Avg_Eve_Call_Duration'] = df_processed['Eve Mins'] / (df_processed['Eve Calls'] + 1)

    if 'Night Mins' in df_processed.columns and 'Night Calls' in df_processed.columns:
        df_processed['Avg_Night_Call_Duration'] = df_processed['Night Mins'] / (df_processed['Night Calls'] + 1)

    charge_cols = [c for c in df_processed.columns if 'Charge' in c]
    if charge_cols:
        df_processed['Total_Charge'] = df_processed[charge_cols].sum(axis=1)

    mins_cols = [c for c in df_processed.columns if 'Mins' in c]
    if mins_cols:
        df_processed['Total_Mins'] = df_processed[mins_cols].sum(axis=1)

    calls_cols = [c for c in df_processed.columns if 'Calls' in c and c != 'CustServ Calls']
    if calls_cols:
        df_processed['Total_Calls'] = df_processed[calls_cols].sum(axis=1)

    for col in feature_names:
        if col not in df_processed.columns:
            df_processed[col] = 0

    return df_processed[feature_names]

# -----------------------------
# MAIN APP
# -----------------------------
def main():
    st.markdown("""
        <div class="hero-box">
            <h1 class="main-header">📞 Customer Churn Prediction System</h1>
            <p class="sub-header">AI-Powered Customer Retention Analytics Dashboard</p>
            <div style="text-align:center;">
                <span class="insight-pill">Churn Risk Scoring</span>
                <span class="insight-pill">Batch Prediction</span>
                <span class="insight-pill">Feature Insights</span>
                <span class="insight-pill">Retention Analytics</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    model_data = load_model()
    if model_data is None:
        st.stop()

    model = model_data['model']
    scaler = model_data['scaler']
    feature_names = model_data['feature_names']

    st.sidebar.markdown("## 📡 Navigation")
    page = st.sidebar.radio(
        "Go to",
        ["🏠 Home", "🔮 Single Prediction", "📊 Batch Prediction", "📈 Model Analytics"]
    )

    if page == "🏠 Home":
        st.write("---")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
                <div class="metric-card">
                    <h3>🎯 Objective</h3>
                    <p>Predict customer churn to enable proactive retention strategies</p>
                </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
                <div class="metric-card">
                    <h3>🤖 Model Type</h3>
                    <p>Gradient Boosting / Random Forest Classifier</p>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
                <div class="metric-card">
                    <h3>📊 Features</h3>
                    <p>Model-ready customer churn attributes and engineered signals</p>
                </div>
            """, unsafe_allow_html=True)

        st.write("---")

        st.markdown('<div class="section-title">🚀 Quick Start Guide</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="glass-box">
        1. <strong>Single Prediction</strong>: Analyze one customer at a time<br><br>
        2. <strong>Batch Prediction</strong>: Use the built-in preprocessed dataset or upload your own CSV<br><br>
        3. <strong>Model Analytics</strong>: View feature importance and business insights
        </div>
        """, unsafe_allow_html=True)

    elif page == "🔮 Single Prediction":
        st.markdown('<div class="section-title">🔮 Predict Churn for Individual Customer</div>', unsafe_allow_html=True)
        st.write("Enter customer information to predict churn probability")

        st.write("---")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown('<div class="small-label">📍 Location & Account Info</div>', unsafe_allow_html=True)
            state = st.selectbox("State", STATE_LIST)
            account_length = st.number_input("Account Length (days)", min_value=1, max_value=300, value=100)
            area_code = st.selectbox("Area Code", AREA_CODES)

        with col2:
            st.markdown('<div class="small-label">📞 Service Plans</div>', unsafe_allow_html=True)
            intl_plan = st.selectbox("International Plan", ["no", "yes"])
            vmail_plan = st.selectbox("Voice Mail Plan", ["no", "yes"])
            vmail_message = st.number_input("Voice Mail Messages", min_value=0, max_value=60, value=0)
            custserv_calls = st.number_input("Customer Service Calls", min_value=0, max_value=10, value=1)

        with col3:
            st.markdown('<div class="small-label">⏰ Usage Patterns</div>', unsafe_allow_html=True)
            day_mins = st.number_input("Day Minutes", min_value=0.0, max_value=400.0, value=180.0)
            day_calls = st.number_input("Day Calls", min_value=0, max_value=200, value=100)
            eve_mins = st.number_input("Evening Minutes", min_value=0.0, max_value=400.0, value=200.0)
            eve_calls = st.number_input("Evening Calls", min_value=0, max_value=200, value=100)

        col4, col5 = st.columns(2)
        with col4:
            night_mins = st.number_input("Night Minutes", min_value=0.0, max_value=400.0, value=200.0)
            night_calls = st.number_input("Night Calls", min_value=0, max_value=200, value=100)
        with col5:
            intl_mins = st.number_input("International Minutes", min_value=0.0, max_value=30.0, value=10.0)
            intl_calls = st.number_input("International Calls", min_value=0, max_value=30, value=3)

        st.write("---")

        day_charge = day_mins * 0.17
        eve_charge = eve_mins * 0.085
        night_charge = night_mins * 0.045
        intl_charge = intl_mins * 0.27

        input_data = {
            'Account Length': account_length,
            "Int'l Plan": 1 if intl_plan == 'yes' else 0,
            'VMail Plan': 1 if vmail_plan == 'yes' else 0,
            'VMail Message': vmail_message,
            'Day Mins': day_mins,
            'Day Calls': day_calls,
            'Day Charge': day_charge,
            'Eve Mins': eve_mins,
            'Eve Calls': eve_calls,
            'Eve Charge': eve_charge,
            'Night Mins': night_mins,
            'Night Calls': night_calls,
            'Night Charge': night_charge,
            'Intl Mins': intl_mins,
            'Intl Calls': intl_calls,
            'Intl Charge': intl_charge,
            'CustServ Calls': custserv_calls
        }

        input_df = pd.DataFrame([input_data])

        for s in STATE_LIST:
            input_df[f'State_{s}'] = 1 if state == s else 0

        for ac in AREA_CODES:
            input_df[f'AreaCode_{ac}'] = 1 if str(area_code) == str(ac) else 0

        input_df['Avg_Day_Call_Duration'] = day_mins / (day_calls + 1)
        input_df['Avg_Eve_Call_Duration'] = eve_mins / (eve_calls + 1)
        input_df['Avg_Night_Call_Duration'] = night_mins / (night_calls + 1)
        input_df['Total_Charge'] = day_charge + eve_charge + night_charge + intl_charge
        input_df['Total_Mins'] = day_mins + eve_mins + night_mins + intl_mins
        input_df['Total_Calls'] = day_calls + eve_calls + night_calls + intl_calls

        if st.button("🔮 Predict Churn", type="primary", use_container_width=True):
            processed_input = preprocess_input(input_df, feature_names)
            input_scaled = scaler.transform(processed_input)

            prediction = model.predict(input_scaled)[0]
            probability = model.predict_proba(input_scaled)[0]

            churn_prob = probability[1] * 100
            no_churn_prob = probability[0] * 100

            st.write("---")
            result_col1, result_col2 = st.columns(2)

            with result_col1:
                if prediction == 1:
                    st.markdown("""
                        <div class="prediction-box churn-yes">
                            ⚠️ HIGH RISK<br>
                            Customer Likely to Churn
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                        <div class="prediction-box churn-no">
                            ✅ LOW RISK<br>
                            Customer Likely to Stay
                        </div>
                    """, unsafe_allow_html=True)

            with result_col2:
                fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=churn_prob,
                    title={'text': "Churn Probability", 'font': {'color': C["text"], 'size': 22}},
                    domain={'x': [0, 1], 'y': [0, 1]},
                    gauge={
                        'axis': {'range': [None, 100], 'tickcolor': C["muted"]},
                        'bar': {'color': C["red"] if churn_prob > 50 else C["teal"]},
                        'bgcolor': "#f8fbfd",
                        'borderwidth': 1,
                        'bordercolor': C["border"],
                        'steps': [
                            {'range': [0, 30], 'color': "rgba(15,118,110,0.18)"},
                            {'range': [30, 70], 'color': "rgba(183,121,31,0.18)"},
                            {'range': [70, 100], 'color': "rgba(197,48,48,0.18)"}
                        ],
                        'threshold': {'line': {'color': C["red"], 'width': 4}, 'thickness': 0.75, 'value': 50}
                    }
                ))
                fig.update_layout(height=300, paper_bgcolor='rgba(0,0,0,0)', font={'color': C["text"]})
                st.plotly_chart(fig, use_container_width=True)

            st.write("---")
            prob_col1, prob_col2 = st.columns(2)
            with prob_col1:
                st.metric("Probability of Churn", f"{churn_prob:.2f}%")
            with prob_col2:
                st.metric("Probability of Retention", f"{no_churn_prob:.2f}%")

    elif page == "📊 Batch Prediction":
        st.markdown('<div class="section-title">📊 Batch Prediction for Multiple Customers</div>', unsafe_allow_html=True)
        st.write("Use the built-in preprocessed dataset or upload your own CSV.")
        st.write("---")

        option = st.radio(
            "Choose batch data source",
            ["Use built-in sample dataset", "Upload my own CSV"],
            horizontal=True
        )

        df = None
        data_source_label = ""

        if option == "Use built-in sample dataset":
            try:
                df, used_path = load_builtin_batch_data()
                data_source_label = f"Built-in dataset loaded from: {used_path}"
                st.success(data_source_label)
            except FileNotFoundError as e:
                st.error(str(e))
        else:
            uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
            if uploaded_file is not None:
                df = pd.read_csv(uploaded_file)
                data_source_label = "Uploaded CSV loaded successfully."
                st.success(f"{data_source_label} {len(df)} rows found.")

        if df is not None:
            with st.expander("📋 View Data Preview", expanded=True):
                st.dataframe(df.head(10), use_container_width=True)

            if st.button("🚀 Run Batch Prediction", type="primary"):
                with st.spinner("Processing predictions..."):
                    df_processed = preprocess_batch_data(df, feature_names)
                    df_scaled = scaler.transform(df_processed)
                    predictions = model.predict(df_scaled)
                    probabilities = model.predict_proba(df_scaled)[:, 1]

                    results_df = df.copy()
                    results_df['Churn_Prediction'] = pd.Series(predictions).map({1: 'Yes', 0: 'No'})
                    results_df['Churn_Probability'] = (probabilities * 100).round(2)
                    results_df['Risk_Level'] = pd.cut(
                        probabilities,
                        bins=[0, 0.3, 0.7, 1.0],
                        labels=['Low', 'Medium', 'High']
                    )

                st.success("Predictions completed!")

                st.write("---")
                st.markdown('<div class="section-title">📊 Prediction Summary</div>', unsafe_allow_html=True)

                col1, col2, col3, col4 = st.columns(4)
                churn_count = (predictions == 1).sum()
                churn_rate = (churn_count / len(predictions)) * 100
                avg_risk = probabilities.mean() * 100

                with col1:
                    st.metric("Total Customers", len(results_df))
                with col2:
                    st.metric("Predicted Churners", churn_count)
                with col3:
                    st.metric("Churn Rate", f"{churn_rate:.1f}%")
                with col4:
                    st.metric("Average Risk", f"{avg_risk:.1f}%")

                st.write("---")
                viz_col1, viz_col2 = st.columns(2)

                with viz_col1:
                    churn_dist = results_df['Churn_Prediction'].value_counts()
                    fig = px.pie(
                        values=churn_dist.values,
                        names=churn_dist.index,
                        title="Churn Prediction Distribution",
                        color=churn_dist.index,
                        color_discrete_map={'Yes': '#c53030', 'No': '#0f766e'}
                    )
                    style_plotly(fig)
                    st.plotly_chart(fig, use_container_width=True)

                with viz_col2:
                    risk_dist = results_df['Risk_Level'].value_counts().sort_index()
                    fig = px.bar(
                        x=risk_dist.index,
                        y=risk_dist.values,
                        title="Risk Level Distribution",
                        labels={'x': 'Risk Level', 'y': 'Count'},
                        color=risk_dist.index,
                        color_discrete_map={'Low': '#0f766e', 'Medium': '#b7791f', 'High': '#c53030'}
                    )
                    style_plotly(fig)
                    st.plotly_chart(fig, use_container_width=True)

                st.write("---")
                st.markdown('<div class="section-title">📋 Detailed Results</div>', unsafe_allow_html=True)

                filter_col1, filter_col2 = st.columns(2)
                with filter_col1:
                    filter_churn = st.multiselect(
                        "Filter by Churn Prediction",
                        options=['Yes', 'No'],
                        default=['Yes', 'No']
                    )
                with filter_col2:
                    filter_risk = st.multiselect(
                        "Filter by Risk Level",
                        options=['Low', 'Medium', 'High'],
                        default=['Low', 'Medium', 'High']
                    )

                filtered_df = results_df[
                    results_df['Churn_Prediction'].isin(filter_churn) &
                    results_df['Risk_Level'].isin(filter_risk)
                ]

                st.dataframe(filtered_df, use_container_width=True, hide_index=True)

                st.write("---")
                csv = filtered_df.to_csv(index=False)
                st.download_button(
                    label="📥 Download Predictions as CSV",
                    data=csv,
                    file_name="churn_predictions.csv",
                    mime="text/csv",
                    use_container_width=True
                )

    elif page == "📈 Model Analytics":
        st.markdown('<div class="section-title">📈 Model Performance & Analytics</div>', unsafe_allow_html=True)
        st.write("---")

        info_col1, info_col2, info_col3 = st.columns(3)
        with info_col1:
            st.info(f"**Algorithm:** {type(model).__name__}")
        with info_col2:
            st.info(f"**Features:** {len(feature_names)}")
        with info_col3:
            st.info("**Task:** Binary Classification")

        st.write("---")

        if hasattr(model, 'feature_importances_'):
            feature_importance_df = pd.DataFrame({
                'Feature': feature_names,
                'Importance': model.feature_importances_
            }).sort_values('Importance', ascending=False).head(15)

            fig = px.bar(
                feature_importance_df,
                x='Importance',
                y='Feature',
                orientation='h',
                title="Top 15 Most Important Features",
                color='Importance',
                color_continuous_scale='Blues'
            )
            fig.update_layout(height=500, yaxis={'categoryorder': 'total ascending'})
            style_plotly(fig)
            st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()