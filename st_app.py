import streamlit as st
import os
from openai import OpenAI

# Set your OpenAI API key
openai_api_key = "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"
client = OpenAI(api_key=openai_api_key)

st.set_page_config(page_title="AI Hiring Planner", layout="centered")
st.title("🤖 AI Hiring Strategy Planner")

# --- Input Section ---
with st.form("hiring_form"):
    st.subheader("📊 Enter Your Hiring Parameters")

    col1, col2 = st.columns(2)
    with col1:
        growth_rate = st.slider("Projected Growth Rate (%)", 10, 200, 20, step=10)
        headcount = st.number_input("Current Headcount", min_value=1, value=50)
        attrition_rate = st.slider("Annual Attrition Rate (%)", 0, 100, 20)

    with col2:
        growth_timeline = st.selectbox("Growth Timeline", ["3 months", "6 months", "9 months", "12 months"], index=2)
        speed_to_hire = st.slider("Speed to Hire (weeks)", 1, 12, 6)
        tenure_years = st.slider("Average Tenure (Years)", 0, 10, 2)
        tenure_months = st.slider("Average Tenure (Months)", 0, 11, 3)

    st.markdown("### 📈 Growth Distribution (% of growth)")
    dist_col1, dist_col2, dist_col3 = st.columns(3)
    with dist_col1:
        dist_0_1 = st.slider("0–1 month", 0, 100, 10)
    with dist_col2:
        dist_1_3 = st.slider("1–3 months", 0, 100, 50)
    with dist_col3:
        dist_3_6 = st.slider("3–6 months", 0, 100, 40)

    total_dist = dist_0_1 + dist_1_3 + dist_3_6
    if total_dist != 100:
        st.warning("⚠️ The total growth distribution should add up to 100%.")

    submitted = st.form_submit_button("Generate Hiring Plan")

# --- Prompt Construction & Model Call ---
if submitted and total_dist == 100:
    prompt = f"""
    Create a hiring strategy based on the following inputs:

    - Projected Growth Rate: {growth_rate}% over the next {growth_timeline}.
    - Growth Distribution:
      - {dist_0_1}% in 0–1 months,
      - {dist_1_3}% in 1–3 months,
      - {dist_3_6}% in 3–6 months.
    - Current Headcount: {headcount} employees.
    - Attrition Rate: {attrition_rate}% annually.
    - Speed to Hire: {speed_to_hire} weeks per role.
    - Average Employee Tenure: {tenure_years} years and {tenure_months} months.

    Calculate how many hires are needed (for growth and attrition), when hiring should start, and provide AI-based recommendations for reducing time to hire and increasing retention.
    Output a JSON plan along with a readable explanation.
    """

    with st.spinner("🔍 Generating hiring strategy using GPT-4o-mini..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an expert HR planner and hiring strategist."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
            )
            st.success("✅ Plan generated successfully!")

            output = response.choices[0].message.content
            st.markdown("### 📄 Hiring Strategy Output")
            st.markdown(output)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
