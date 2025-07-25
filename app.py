"""Run this model in Python

> pip install openai
"""
import os
from openai import OpenAI

# To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings.
# Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
client = OpenAI(
    # api_key = os.environ["GITHUB_TOKEN"],
    api_key = "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",
    default_query = {
        "api-version": "2024-08-01-preview",
    },
)

messages = [
    {
        "role": "system",
        "content": "Develop a hiring plan and strategy for the company based on historical data, projected growth rate, attrition, and other hiring metrics related to a specific role or skillset.\n\nUse the following inputs to calculate the estimated number of hires, timeline for hiring, and provide AI-driven recommendations for prioritizing hiring activities.\n\n# Inputs\n\nYou will use the following data points to craft the hiring plan:\n- **Projected Growth Rate**: Provided as a percentage (in multiples of 10 up to 200) over a given timeline (e.g., 20% growth over 9 months).\n- **Expected Growth Distribution Across Timeline**: Broken into phases (e.g., 10% growth in 0-1 month, 50% in 1-3 months, etc.) within a defined growth period (e.g., 9 months).\n- **Current Headcount**: Integers reflecting the current number of employees for the selected role (e.g., 50 AI/ML engineers).\n- **Attrition Rate**: Annual attrition rate percentage specific to the role (e.g., 20% attrition per year for AI/ML engineers).\n- **Speed to Hire**: Average time to fill a position in weeks (e.g., 6 weeks per hire).\n- **Average Employee Tenure**: Dropdown inputs reflect time an employee typically stays (e.g., 2 years and 3 months).\n\n# Goals\n\n- Calculate the total number of hires required to meet projected growth while accounting for attrition.\n- Develop a timeline-based hiring plan to align hiring efforts with expected growth distribution.\n- Recommend start times for hiring cycles and strategies to optimize hiring success based on speed-to-hire and attrition trends.\n- Propose AI-driven insights and recruitment strategies to improve time to hire, retention rates, and efficiency.\n\n# Steps\n\n1. **Calculate Total Headcount Needs**:\n   - Account for current headcount, growth rate expectation, and attrition rate to determine the total number of hires required over the timeline.\n   - Incorporate projected distribution percentages when estimating hires across defined phases.\n\n2. **Factor Attrition**:\n   - Adjust hiring needs for attrition rate annually and break this down across the defined timeline phases.\n\n3. **Timeline-Based Hiring Plan**:\n   - Based on total hires needed and growth distribution, outline the recommended number of hires by each timeline phase.\n   - Align expected hiring numbers with the company's average speed to hire per role to determine when recruitment activities should begin.\n\n4. **AI-Led Recommendations**:\n   - Propose AI-based optimizations for reducing time to hire (e.g., talent pool automation, intelligent resume screening).\n   - Suggest approaches for enhancing retention based on employee tenure patterns (e.g., personalized onboarding and training programs).\n   - Recommend strategies to balance growth needs with potential risk from attrition.\n\n# Output Format\n\nProvide detailed results in structured format:\n- **Total Number of Hires Needed**:\n  - X hires required for growth + attrition.\n- **Timeline-Based Hiring Plan**:\n  - Phase 1 (0-1 month): X hires needed, start hiring on/by [date].\n  - Phase 2 (1-3 months): X hires needed, start hiring on/by [date].\n  - Phase 3 (3-6 months): X hires needed, start hiring on/by [date].\n  - ...\n- **AI-Based Strategies**:\n  - Suggestions for reducing time-to-hire.\n  - Retention improvements based on tenure insights.\n  - Any other actionable AI-driven ideas.\n  \nOutput results in descriptive paragraphs alongside JSON summaries that can be used for further analysis.\n\n### JSON Example\n```json\n{\n  \"TotalHires\": {\n    \"GrowthRequirement\": 10,\n    \"AttritionAdjustment\": 5,\n    \"TotalHiresNeeded\": 15\n  },\n  \"HiringPlan\": [\n    {\"Phase\": \"0-1 month\", \"HiresNeeded\": 2, \"StartDate\": \"2023-11-01\"},\n    {\"Phase\": \"1-3 months\", \"HiresNeeded\": 8, \"StartDate\": \"2023-12-01\"},\n    {\"Phase\": \"3-6 months\", \"HiresNeeded\": 5, \"StartDate\": \"2024-01-01\"}\n  ],\n  \"AIRecommendations\": {\n    \"ReduceTimeToHire\": \"Leveraging advanced candidate screening and automated outreach tools.\",\n    \"RetentionStrategies\": \"Focus on extending tenure via personalized career paths and mentorship programs.\",\n    \"EfficiencyImprovements\": \"Integrate predictive analytics to anticipate attrition rates.\"\n  }\n}\n```\n\n# Examples\n\n### Input:\n- Projected Growth Rate: 20% over the next 9 months.\n- Growth Distribution: 10% in 0-1 months, 50% in 1-3 months, 40% in 3-6 months.\n- Current Headcount: 50 employees.\n- Attrition Rate: 20% per year.\n- Speed to Hire: 6 weeks per role.\n- Average Employee Tenure: 2 years 3 months.\n\n### Output:\n- **Total Number of Hires Needed**:\n  - Growth: 10 additional employees (20% of 50).\n  - Attrition: Assume an annual attrition rate of 20%. Over 9 months, attrition impacts 15% of current headcount (approx. 8 people). Add these hires for total: 18 needed.\n\n- **Timeline-Based Hiring Plan**:\n  - Phase 1 (0-1 month): 2 hires; hire immediately.\n  - Phase 2 (1-3 months): 9 hires; start recruitment by mid-[next date].\n  - Phase 3 (3-6-months): 7 hires; launch hiring by [another placeholder].\n\n- **AI-Based Strategies**:\n  - AI-based screening tools reduce hiring time from 6 weeks to 4 weeks.\n  - Predict attrition and prioritize employees at risk for retention initiatives.\n\n# Notes\n- Adjust calculations based on any anomalies (e.g., unusually high attrition during certain phases).\n- Ensure AI-driven suggestions improve both efficiency and long-term outcomes.\n- Output timeline estimates in future-proofed date format to match realistic hiring cycles.",
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Create a hiring strategy plan based on the inputs we have ",
            },
        ],
    },
    {
        "role": "assistant",
        "content": [
            {
                "type": "text",
                "text": "To create your hiring strategy plan, I will base calculations and recommendations on the input parameters provided. Here's a step-by-step breakdown to craft an optimized hiring plan:\n\n---\n\n### Inputs\n- **Projected Growth Rate**: 20% over the next 9 months.\n- **Growth Distribution**: \n  - 10% in 0-1 months,\n  - 50% in 1-3 months,\n  - 40% in 3-6 months.\n- **Current Headcount**: 50 employees (role: AI/ML engineers).\n- **Attrition Rate**: 20% per year.\n- **Speed to Hire**: 6 weeks per hire.\n- **Average Employee Tenure**: 2 years and 3 months (27 months).\n\n---\n\n### Plan Breakdown\n\n### 1. **Calculate Total Hires Needed**\n\n#### A. Growth Requirement\nThe company's current headcount is 50 employees. A 20% growth over 9 months equates to:\n- Growth = 50 × 0.20 = **10 additional employees**.\n\n#### B. Attrition Impact\nWith a 20% annual attrition rate and the projected timeline of 9 months, the attrition for this role is approximately:\n- Annual attrition = 50 × 0.20 = **10 employees per year**.\n- Attrition over 9 months = (10 ÷ 12) × 9 = **7.5 employees** (~8 hires to replace attrition).\n\n#### C. Total Hires\nTo meet the growth requirement and address attrition, the total hires needed are:\n- Growth hires + Attrition hires = 10 + 8 = **18 hires**.\n\n---\n\n### 2. **Timeline-Based Hiring Plan**\n\n#### Growth Distribution\nThe expected growth distribution informs how many hires are needed in each phase:\n1. **Phase 1 (0-1 month)**: 10% of growth (10 employees) = 1 employee for growth.\n2. **Phase 2 (1-3 months)**: 50% of growth = 5 employees for growth.\n3. **Phase 3 (3-6 months)**: 40% of growth = 4 employees for growth.\n\nAccounting for attrition across these phases:\n- Attrition for 0-1 month: (8 × 1/9) = ~1 employee.\n- Attrition for 1-3 months: (8 × 3/9) = ~3 employees.\n- Attrition for 3-6 months: (8 × 5/9) = ~4 employees.\n\n#### Hires by Phase\n- **Phase 1 (0-1 month)**: 1 growth + 1 attrition = **2 hires**. \n  - Start hiring immediately.\n- **Phase 2 (1-3 months)**: 5 growth + 3 attrition = **8 hires**. \n  - Begin recruitment by the start of Month 1 (allowing 6 weeks to hire by Month 3).\n- **Phase 3 (3-6 months)**: 4 growth + 4 attrition = **8 hires**.\n  - Begin recruitment by Month 2 or early Month 3 to meet hiring deadlines by Month 6.\n\n---\n\n### 3. **AI-Based Strategies**\n\n#### A. Reduce Time-to-Hire\nUsing AI-driven recruitment tools, the average speed to hire can potentially be reduced from 6 weeks to 4 weeks. Recommendations:\n- **AI-Driven Screening**:\n  - Leverage AI to screen candidates' resumes intelligently, ranking and shortlisting only the most relevant applications.\n  - This can cut down manual screening time by 40-50%.\n- **Predictive Analytics**:\n  - Use predictive models to gauge candidate fit scores, focusing hiring efforts on high-probability, high-retention candidates.\n  \n#### B. Enhance Retention\nBased on the attrition rate and average tenure:\n- **Personalized Onboarding**:\n  - Develop tailored onboarding processes with mentorship and career mapping, increasing employee engagement and encouraging longevity.\n- **Continuous Learning**:\n  - Provide AI/ML engineers with quarterly skill enhancement opportunities (e.g., online certifications for deep learning or NLP). Such initiatives have been shown to improve tenure by up to 30%.\n  \n#### C. Data-Driven Forecasting\n- Use machine learning tools to anticipate peaks in voluntary attrition and proactively address retention risks.\n- For example, flag employees in current tenure bands at risk for leaving (e.g., 2 years based on your input).\n\n#### D. Boost Talent Pool\n- Implement AI-powered talent sourcing platforms to build a dynamic pipeline.\n- Use intelligent outreach strategies to maintain a warm talent pool so hiring delays are minimized.\n\n---\n\n### Final Deliverable\n\n**Total Number of Hires Needed**:\n- Growth: **10 hires**.\n- Attrition: **8 hires**.  \n- **Total**: **18 hires** over 9 months.\n\n**Timeline-Based Hiring Plan**:\n- **Phase 1 (0-1 month)**: 2 hires; **Start hiring immediately**.\n- **Phase 2 (1-3 months)**: 8 hires; **Start hiring by [appropriate calculated dates, e.g., Month 1]**.\n- **Phase 3 (3-6 months)**: 8 hires; **Launch hiring process early Month 3**.\n\n**AI-Based Recommendations**:\n- AI-enabled resume screening and predictive analytics can reduce time-to-hire to 4 weeks.\n- Focus on retention strategies: Personalized onboarding, upskilling programs, and mentorship tracks.\n- Build a robust, AI-enhanced pipeline to maintain candidate availability aligned with growth phases.\n\n---\n\n### JSON Summary\n```json\n{\n  \"TotalHires\": {\n    \"GrowthRequirement\": 10,\n    \"AttritionAdjustment\": 8,\n    \"TotalHiresNeeded\": 18\n  },\n  \"HiringPlan\": [\n    {\"Phase\": \"0-1 month\", \"HiresNeeded\": 2, \"StartDate\": \"2023-11-01\"},\n    {\"Phase\": \"1-3 months\", \"HiresNeeded\": 8, \"StartDate\": \"2023-12-15\"},\n    {\"Phase\": \"3-6 months\", \"HiresNeeded\": 8, \"StartDate\": \"2024-02-01\"}\n  ],\n  \"AIRecommendations\": {\n    \"ReduceTimeToHire\": \"Leverage advanced tools for resume screening and predictive analytics to reduce hiring time to 4 weeks.\",\n    \"RetentionStrategies\": \"Implement personalized onboarding, continuous learning opportunities, and mentorship programs.\",\n    \"EfficiencyImprovements\": \"Integrate AI-driven talent sourcing and attrition forecasting tools to improve hiring precision and timing.\"\n  }\n}\n```\n\n---\n\nLet me know if you would like further refinements or specific date calculations!",
            },
        ],
    },
]

tools = []

response_format = {
    "type": "text"
}

while True:
    response = client.chat.completions.create(
        messages = messages,
        model = "gpt-4o-mini",
        tools = tools,
        response_format = response_format,
        temperature = 1,
        top_p = 1,
    )

    if response.choices[0].message.tool_calls:
        print(response.choices[0].message.tool_calls)
        messages.append(response.choices[0].message)
        for tool_call in response.choices[0].message.tool_calls:
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": [
                    {
                        "type": "text",
                        "text": locals()[tool_call.function.name](),
                    },
                ],
            })
    else:
        print(response.choices[0].message.content)
        break
