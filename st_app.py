import streamlit as st
import os
from openai import OpenAI

# Set your OpenAI API key

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
    
    Your response must follow this format:
    1. **Understanding Growth and Attrition Needs**
       - Clearly calculate new hires for growth and attrition separately.
       - Show total hires needed.
    
    2. **Growth Distribution Timeline**
       - For each phase (0–1 mo, 1–3 mo, 3–6 mo), break down:
         - Number of hires for growth
         - Number of hires for attrition
         - Total hires
    
    3. **Hiring Timeline**
       - Show monthly or phase-wise hire totals (e.g., Month 0–1: X hires).
    
    4. **Recommendations**
       - List 2–3 strategies for reducing time to hire
       - List 2–3 strategies to increase retention
    
    5. **JSON Plan**
       - Provide a valid JSON object with the full plan in this structure:
         {{
           "hiring_plan": {{
             "current_headcount": ...,
             "projected_growth_rate": ...,
             "total_hires_needed": ...,
             "hiring_timeline": {{
               "0-1_months": {{ "growth_hires": ..., "attrition_hires": ..., "total_hires": ... }},
               "1-3_months": {{ ... }},
               ...
             }},
             "strategies": {{
               "reduce_time_to_hire": [...],
               "increase_retention": [...]
             }}
           }}
         }}
    
    6. **Readable Explanation**
       - Summarize the entire strategy in simple bullet points for a human reader.
    
    Note:
    - Use clear formatting with headings, bullet points, and avoid mixing sections.
    - All the results should be in perfect markdown format.
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
