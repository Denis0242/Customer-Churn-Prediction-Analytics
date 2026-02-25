
# 📊 Customer Churn Prediction | Product Data Science Case Study

**Product Data Science | Retention Analytics | Machine Learning | Experimentation Strategy | Revenue Optimization**

---

# 🚀 Executive Summary
 Customer churn directly impacts revenue, growth, and long-term product sustainability.
This project approaches churn not just as a classification problem — but as a product retention and revenue optimization challenge.

---

**The goal is to:**
- Identify high-risk churn segments
- Understand behavioral and contractual drivers
- Quantify business impact
- Recommend product-level interventions
- Enable experimentation-driven retention strategies

**This mirrors how churn is handled in SaaS, FinTech, HealthTech, and Telecom product organizations.**

---

# 🎯 Product Problem Statement
**Subscription-based products experience revenue leakage when customers cancel early.**
- **Key Product Questions:**
- Which customers are most likely to churn?
- What signals predict churn behavior?
- When is the highest-risk churn window?
- What retention experiment should be prioritized?

---

# 📈 North Star Metric (NSM)
**- Retention Rate / Active Subscription Rate**

**Supporting Metrics:**
- Monthly Recurring Revenue (MRR)
- Customer Churn Rate
- Customer Lifetime Value (CLV)
- Average Revenue Per User (ARPU)
- Tenure Distribution
- Contract Conversion Rate

---

# 📊 Business Context Simulation
**Assume:**
- 10,000 active customers
- 26% churn rate
- $70 average monthly revenue
- A 5% reduction in churn leads to significant annual revenue preservation.

---

**This project provides predictive modeling to enable proactive intervention before churn occurs.**

# 🔍 Exploratory Product Insights
**Key findings from EDA:**
- Month-to-month contracts have the highest churn probability
- Short-tenure customers churn within the early lifecycle stage
- Higher monthly charges correlate with increased churn
- Electronic check payment method shows elevated churn behavior

**These insights inform targeted retention strategies.**

---

# 🤖 Machine Learning Approach
**Models Evaluated:**
- Logistic Regression
- Random Forest
- Decision Tree
- Gradient Boosting (if applicable)

**Evaluation Metrics:**
- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

**The selected model achieved strong ROC-AUC performance and improved churn risk identification.**

---

# 🧠 Feature Importance & Driver Analysis

**Top predictors of churn:**
- Contract Type
- Tenure
- Monthly Charges
- Internet Service
- Payment Method

**Interpretation:**

**Churn behavior is influenced primarily by lifecycle stage and contract structure rather than demographics — indicating product and pricing optimization opportunities.**

---

# 🧪 Experimentation Strategy (Product Lens)
- Instead of stopping at prediction, this project proposes actionable experiments:

**1️⃣ Contract Conversion Incentive**
- Offer discounted annual plans to month-to-month customers.

**Hypothesis:**
- Customers transitioning to long-term contracts will reduce churn probability.

**2️⃣ Early Lifecycle Engagement Experiment**
- Target customers within the first 90 days with onboarding nudges.

**Hypothesis:**
- Improved onboarding engagement increases long-term retention.

**3️⃣ High-Value Customer Retention Offer**
- Provide personalized loyalty offers to high ARPU customers flagged as high churn risk.

**Hypothesis:**
- Targeted retention incentives preserve revenue efficiently.

**All experiments can be validated using A/B testing frameworks.**

# 🏗️ End-to-End Workflow
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA) with business interpretation
- Feature Engineering (contract type, tenure segmentation, billing patterns)
- Encoding & Scaling
- Train-Test Split
- Model Training (Logistic Regression, Random Forest, etc.)
- Model Evaluation (ROC-AUC, Precision, Recall, F1)
- Feature Importance Analysis
- Product-Level Interpretation & Strategy Recommendation 

---

# 🛠️ Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook
- Streamlit (optional deployment)

---

## 📂 Project Structure

```
Customer-Churn/
│
├── data/
├── notebooks/
├── models/
├── app.py
├── requirements.txt
└── README.md
```

# 📊 Business Impact Summary
- If implemented in production, this system enables:
- Proactive churn detection
- Targeted retention campaigns
- Revenue preservation
- Experiment-driven product decisions
- Lifecycle-based segmentation

**Even a 3–5% reduction in churn materially increases annual recurring revenue and customer lifetime value.**

--- 

# 🔮 Future Enhancements
- SHAP-based model explainability
- Survival analysis for churn timing
- Uplift modeling for retention targeting
- Real-time churn scoring API
- Automated A/B testing simulator integration
- Deployment with FastAPI 

---

# 🎯 Skills Demonstrated
- Product Data Science
- Customer Retention Analytics
- Churn Modeling
- Predictive Modeling
- Feature Engineering
- Machine Learning
- Experiment Design
- Revenue Optimization
- Business Analytics
- Python

---

# How to Run this

**Clone the repository:**
- git clone https://github.com/Denis0242/Customer-Churn.git
- cd Customer-Churn

**Install dependencies:**
- pip install -r requirements.txt

**Run the notebook:**
- jupyter notebook

**If using Streamlit (optional):**
- streamlit run app.py
---

# 👤 Author

**Denis Agyapong**

**Product Data Scientist | Data Analyst**

**Oakland, CA**





