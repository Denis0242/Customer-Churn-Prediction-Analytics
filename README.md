#  **Denis Agyapong**  
**Product Data Scientist | Data Analyst**

### 🌍 Links:
📍 Oakland, CA  
📧 vantjohnn@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/denis-agyapong)  
🐙 [GitHub](https://github.com/Denis0242)
---

# 📉 Customer Churn — Product Data Science Analysis
🔍 **Product Overview:**

This project applies Product Data Science principles to understand, measure, and reduce customer churn.
Rather than focusing only on prediction accuracy, the goal is to uncover why users churn, which behaviors signal risk early,
and how product teams can intervene effectively.
The analysis mirrors how a Product Data Scientist partners with Product Managers and stakeholders to support retention, 
engagement, and revenue decisions.

#### 🎯 Product & Business Problem
**Customer churn reduces:**
- Retention
- Customer Lifetime Value (LTV)
- Long-term product growth
- From a product perspective, churn is a signal that users are not consistently realizing value.

**Key product questions:**
- Which customer behaviors are associated with churn?
- Are there early signals that predict churn risk?
- Which customer segments should product teams prioritize?
- How can insights translate into actionable retention strategies?

### 📊 Dataset & Product Context
**The dataset contains historical customer-level data, including:**
- Customer attributes and service details
- Usage and engagement-related features
- Contract and account information
- A churn indicator (Yes / No)
Each record represents a user’s interaction with the product over time, allowing churn to be analyzed through a 
behavioral and lifecycle lens.

### 📈 Product Metrics Used
**The analysis focuses on product-relevant metrics, not just model outputs:**
- Churn Rate – % of users who stop using the product
- Retention (conceptual) – users who continue over time
- Engagement signals – usage patterns tied to churn
- Customer Lifetime Value (LTV) – discussed conceptually as a downstream outcome
These metrics reflect how product teams evaluate user value and long-term health.
---

### 🧠 Product Analytics Approach
**The project follows a PDS-style workflow, emphasizing decisions over algorithms:**

1️⃣ **Data Preparation**
- Cleaned and validated data
- Encoded categorical features
- Ensured churn labels aligned with product definitions

2️⃣ **Exploratory Product Analysis**
- Compared churned vs retained users
- Analyzed churn across customer segments
- Identified behaviors correlated with churn risk

3️⃣ **Churn Modeling (Decision Support)**
- Built predictive models to rank churn risk
- Focused on interpretability over complexity
- Used model outputs to support targeting and prioritization

4️⃣ **Insight Translation**
- Connected statistical patterns to user behavior
- Framed results in product and business terms
- Emphasized how insights inform action

### 📊 Key Visual Insights:
**(Visuals are generated directly from the notebook and embedded in this repo)**
- Churn distribution – scope of the problem
- Churn by customer segment / contract type – who is at risk
- Feature importance – which behaviors matter most
These visuals support fast, stakeholder-friendly understanding.

### 📋 Summary of Product Findings
**Product Area	Insight	Product Interpretation**
- Overall Churn	Churn rate is non-trivial	Retention is a key growth lever
- User Segments	Some segments churn significantly more	Not all users should be treated equally
- Engagement	Low usage correlates with churn	Users fail to reach sustained value
- Contracts	Short-term commitments churn more	Long-term commitment improves retention
- Predictability	Churn risk appears early	Proactive intervention is possible

### 💡 Product Recommendations
**Based on the analysis, a product team could:**
- Improve early onboarding to reduce time-to-value
- Design targeted retention actions for high-risk users
- Prioritize engagement-driving features over surface-level activity
- Use churn risk signals to support customer success outreach
- Experiment with incentives for longer-term commitments
These recommendations align with product-led growth and retention strategy.

### 🛠️ Tools & Technologies
- Python
- Pandas, NumPy – data analysis
- Matplotlib, Seaborn – visualization
- Scikit-learn – churn modeling
- Jupyter Notebook
---

### 🧪 Experiment Design: Targeted Retention for High-Risk Customers
📌 **Product Hypothesis:**
- Customers identified as high churn risk will respond better to targeted retention actions than generic messaging.

 🎯 **Experiment Goal:**
- Increase retention among high-risk customers while optimizing retention effort efficiency.

👥 **Experiment Setup:**
- Population: Customers predicted to be high churn risk

**Control Group: No intervention**
**Treatment Group: Targeted retention action (personalized message, incentive, or feature recommendation)**

---

#### 📊 Metrics:
**Primary Metric**
- Retention rate among high-risk users

**Secondary Metrics:**
- Engagement lift
- Feature usage changes

**Guardrail Metrics:**
- Opt-out rate
- Negative feedback
- Cost per retained user

### ✅ Success Criteria
**The experiment is successful if:**
- Retention improves significantly in the treatment group
- Retention cost is lower than broad-based campaigns

### 🧠 Decision Logic
- If effective, integrate churn predictions into retention workflows.
- If ineffective, refine targeting criteria or retention strategy.
---

# ▶️ How to Run the Analysis
- git clone https://github.com/Denis0242/Customer-Churn.git
- cd Customer-Churn
- jupyter notebook

**Also don't forget to**
- Create a virtual environment
  
**Install the required packages by running**
- pip install -r requirements.txt

**To train the models**
- Run the application by running the train script to train the models and save them
 - python train.py

**For the EDA**
- Run the app2 file to view the EDA for the customers to understand the customers data
- streamlit run app2.py

**For the prediction**
- To run the predictions model and make prediction in the streamlit application, run the app.py file
- streamlit run app.py
---
### 👤 Author
**Denis Agyapong:**

**Product Data Science / Data Analytics**
- **Focused on churn, retention, user behavior, and data-informed product decisions**







