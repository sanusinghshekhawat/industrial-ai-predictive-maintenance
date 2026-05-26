import streamlit as st
import pandas as pd
import numpy as np
import pickle


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Industrial AI Predictive Maintenance",
    page_icon="⚙️",
    layout="wide"
)


# =====================================================
# LOAD MODEL
# =====================================================

with open("models/final_tuned_rf.pkl", "rb") as file:
    best_rf = pickle.load(file)


with open("models/final_rf_threshold.pkl", "rb") as file:
    final_threshold = pickle.load(file)


# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown(
    """
    <style>

    .main {
        background-color: #0e1117;
    }

    .stMetric {
        background-color: #1c1f26;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #31333F;
    }

    h1, h2, h3 {
        color: white;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =====================================================
# TITLE
# =====================================================

st.title(
    "⚙️ Industrial AI Predictive Maintenance System"
)

st.markdown(
    """
AI-Assisted Equipment Failure Risk Monitoring & Operational Health Analytics
"""
)

st.divider()


# =====================================================
# SIDEBAR INPUTS
# =====================================================

st.sidebar.header("Machine Operational Inputs")


machine_type = st.sidebar.selectbox(
    "Product Type",
    ["L", "M", "H"]
)

air_temp = st.sidebar.slider(
    "Air Temperature [K]",
    295.0,
    310.0,
    300.0
)

process_temp = st.sidebar.slider(
    "Process Temperature [K]",
    305.0,
    320.0,
    310.0
)

rpm = st.sidebar.slider(
    "Rotational Speed [rpm]",
    1000,
    3000,
    1500
)

torque = st.sidebar.slider(
    "Torque [Nm]",
    3.0,
    80.0,
    40.0
)

tool_wear = st.sidebar.slider(
    "Tool Wear [min]",
    0,
    300,
    100
)


# =====================================================
# FEATURE ENGINEERING
# =====================================================

temp_diff = (
    process_temp - air_temp
)

estimated_power = (
    torque * (2 * np.pi * rpm) / 60
)


# =====================================================
# MODEL INPUT
# =====================================================

type_mapping = {
    "L": 0,
    "M": 1,
    "H": 2
}


input_df = pd.DataFrame({

    "Type": [
        type_mapping[machine_type]
    ],

    "Air temperature [K]": [
        air_temp
    ],

    "Process temperature [K]": [
        process_temp
    ],

    "Rotational speed [rpm]": [
        rpm
    ],

    "Torque [Nm]": [
        torque
    ],

    "Tool wear [min]": [
        tool_wear
    ],

    "temp_diff": [
        temp_diff
    ],

    "estimated_power": [
        estimated_power
    ]
})


# =====================================================
# PREDICTION
# =====================================================

failure_probability = best_rf.predict_proba(
    input_df
)[:,1][0]


prediction = int(
    failure_probability >= final_threshold
)


# =====================================================
# HERO METRICS
# =====================================================

metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:

    st.metric(
        "Failure Probability",
        f"{failure_probability*100:.1f}%"
    )

with metric2:

    st.metric(
        "Estimated Power",
        f"{estimated_power:.0f}"
    )

with metric3:

    st.metric(
        "Temperature Difference",
        f"{temp_diff:.1f} K"
    )

with metric4:

    st.metric(
        "Tool Wear",
        f"{tool_wear} min"
    )


st.divider()


# =====================================================
# RISK STATUS
# =====================================================

st.subheader("Operational Risk Status")


if failure_probability < 0.30:

    st.success(
        "🟢 LOW FAILURE RISK"
    )

elif failure_probability < 0.60:

    st.warning(
        "🟠 MEDIUM FAILURE RISK"
    )

else:

    st.error(
        "🔴 HIGH FAILURE RISK"
    )


# =====================================================
# MAIN DASHBOARD
# =====================================================

col1, col2 = st.columns([2, 1])


# =====================================================
# LEFT PANEL
# =====================================================

with col1:

    st.subheader(
        "Operational Condition Monitoring"
    )


    chart_df = pd.DataFrame({

        "Metric": [
            "Torque",
            "RPM",
            "Tool Wear",
            "Temp Difference"
        ],

        "Value": [
            torque,
            rpm / 50,
            tool_wear / 3,
            temp_diff * 10
        ]
    })


    st.bar_chart(
        chart_df.set_index("Metric")
    )


    st.subheader(
        "Failure Probability Gauge"
    )

    st.progress(
        float(failure_probability)
    )


# =====================================================
# RIGHT PANEL
# =====================================================

with col2:

    st.subheader(
        "Machine Information"
    )

    st.info(
        f"""
        Product Type: {machine_type}

        Rotational Speed: {rpm} rpm

        Torque: {torque:.1f} Nm

        Tool Wear: {tool_wear} min
        """
    )


    st.subheader(
        "Operational Insights"
    )


    insights = []


    if torque > 60:

        insights.append(
            "High mechanical loading detected."
        )


    if tool_wear > 200:

        insights.append(
            "Tool wear approaching critical levels."
        )


    if temp_diff > 12:

        insights.append(
            "Thermal imbalance observed."
        )


    if estimated_power > 10000:

        insights.append(
            "Elevated operational power consumption."
        )


    if len(insights) == 0:

        st.success(
            "Machine operating within stable conditions."
        )

    else:

        for insight in insights:

            st.warning(insight)


st.divider()


# =====================================================
# MAINTENANCE RECOMMENDATIONS
# =====================================================

st.subheader(
    "Maintenance Recommendations"
)


recommendations = []


if tool_wear > 200:

    recommendations.append(
        "Inspect and replace worn tooling components."
    )


if torque > 60:

    recommendations.append(
        "Inspect spindle assembly and drive systems."
    )


if temp_diff > 12:

    recommendations.append(
        "Inspect cooling and heat dissipation systems."
    )


if failure_probability > 0.60:

    recommendations.append(
        "Immediate maintenance inspection recommended."
    )


if len(recommendations) == 0:

    st.success(
        "No immediate maintenance action required."
    )

else:

    for rec in recommendations:

        st.error(rec)


st.divider()


# =====================================================
# INPUT SUMMARY
# =====================================================

with st.expander(
    "View Operational Input Summary"
):

    st.dataframe(
        input_df,
        use_container_width=True
    )