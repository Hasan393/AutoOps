import streamlit as st
import pandas as pd
import os
import google.generativeai as genai
from dotenv import load_dotenv
from src.collectors.github_metrics import fetch_live_metrics
from src.prediction_engine.anomaly_detector import predict_failure
from src.remediation_agent.pr_generator import generate_fix
from src.simulation_suite.container_tester import simulate_test

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')

st.set_page_config(page_title="Neural DevOps Autopilot", layout="wide")
st.title("🚀 Neural-DevOps-Autopilot")

if "history" not in st.session_state:
    st.session_state.history =[]

col1, col2 = st.columns(2)

with col1:
    st.subheader("Live Telemetry & Prediction")
    metric_placeholder = st.empty()
    
with col2:
    st.subheader("Autopilot Remediation Console")
    remediation_placeholder = st.empty()

if st.button("Ingest Telemetry Cycle"):
    metrics = fetch_live_metrics()
    st.session_state.history.append(metrics)
    
    df = pd.DataFrame(st.session_state.history)
    with metric_placeholder.container():
        st.line_chart(df[["cpu_usage", "memory_usage", "error_rate"]])
        st.write(f"**CPU:** {metrics['cpu_usage']:.2f}% | **RAM:** {metrics['memory_usage']:.2f}% | **Errors:** {metrics['error_rate']:.2f}/s")
    
    will_fail, risk_score = predict_failure(metrics)
    
    with remediation_placeholder.container():
        if will_fail:
            st.error(f"⚠️ CRITICAL INFRASTRUCTURE ANOMALY (Risk Score: {risk_score}/100)")
            st.warning("Autopilot engaged. Synthesizing infrastructure patch...")
            
            with st.spinner('Generating fix via Gemini 2.5...'):
                fix_code = generate_fix(model, metrics)
                
            st.code(fix_code, language="python")
            
            with st.spinner('Deploying to isolated test container...'):
                test_passed = simulate_test(fix_code)
                
            if test_passed:
                st.success("✅ Fix verified in simulation. Auto-generating Pull Request!")
            else:
                st.error("❌ Container validation failed. Pinging on-call human engineer.")
        else:
            st.success(f"✅ System Stable (Risk Score: {risk_score}/100)")
            st.info("Autopilot standing by.")