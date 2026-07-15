
def app():
    import streamlit as st
    import pandas as pd
    import plotly.express as px

    #page config
    st.set_page_config(
        page_title="Indian Tech Jobs 2026 | EDA Dashboard",
        page_icon="💼",
        layout="wide",
        initial_sidebar_state="expanded",
    )


    st.title("💼 Indian Tech Jobs 2026 | EDA Dashboard")

    st.markdown("""
    ---
    <div style="text-align:center;color:gray;font-size:15px;">
    📌 <b>Data Source:</b> Naukri.com <br>
    🛠 Developed by <b>Amit Kumar</b> | Built with <b>Streamlit & Plotly</b>
    </div>
    """, unsafe_allow_html=True)
    st.caption("Explore hiring trends across companies, cities, roles, skills and experience levels.")

    df = pd.read_csv("cleaned_indian_tech_jobs_2026.csv")


    total_jobs = len(df)
    total_companies = df["company_name"].nunique()
    total_cities = df[df["scraped_city"] != "Remote"]["scraped_city"].nunique()
    avg_rating = round(df["company_rating"].mean(), 2)
    fresher_jobs = df["is_fresher_friendly"].sum()
    senior_jobs = df["is_senior"].sum()

   
    st.markdown("""
    <style>

    .kpi-card{
        background: linear-gradient(135deg,#2563EB,#1E3A8A);
        border-radius:18px;
        padding:25px 20px;
        text-align:center;
        color:white;
        box-shadow:0 8px 18px rgba(0,0,0,.20);
        transition:0.3s;
        margin-bottom:15px;
    }

    .kpi-card:hover{
        transform:translateY(-6px);
        box-shadow:0 12px 24px rgba(0,0,0,.30);
    }

    .kpi-icon{
        font-size:42px;
    }

    .kpi-title{
        font-size:16px;
        margin-top:10px;
        color:#E2E8F0;
        font-weight:500;
    }

    .kpi-value{
        font-size:34px;
        font-weight:bold;
        margin-top:12px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("## 📊 Dashboard Overview")

    row1 = st.columns(3)

    cards = [
        ("💼", "Total Jobs", f"{total_jobs:,}"),
        ("🏢", "Companies", f"{total_companies:,}"),
        ("📍", "Cities", f"{total_cities:,}"),
    ]

    for col, (icon, title, value) in zip(row1, cards):
        with col:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-icon">{icon}</div>
                <div class="kpi-title">{title}</div>
                <div class="kpi-value">{value}</div>
            </div>
            """, unsafe_allow_html=True)

    row2 = st.columns(3)

    cards = [
        ("⭐", "Average Rating", avg_rating),
        ("🎓", "Fresher Jobs", f"{fresher_jobs:,}"),
        ("👔", "Senior Jobs", f"{senior_jobs:,}"),
    ]

    for col, (icon, title, value) in zip(row2, cards):
        with col:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-icon">{icon}</div>
                <div class="kpi-title">{title}</div>
                <div class="kpi-value">{value}</div>
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")

    # ==========================
    # Dashboard Overview
    # ==========================

    st.info("""
    Welcome to the **Indian Tech Jobs Analytics Dashboard 2026**.

    This interactive dashboard analyzes **22,000+ technology job listings** across India to uncover hiring trends,
    salary insights, skill demand, company hiring patterns, work modes, and geographical opportunities.
    Navigate through the dashboard to explore valuable insights that can support job seekers, students,
    and recruiters.
    """)

    st.markdown("")

    # ==========================
    # Objectives & Explore
    # ==========================

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🎯 Dashboard Objectives")

        st.markdown("""
    - ✅ Analyze hiring trends
    - ✅ Discover top hiring companies
    - ✅ Identify in-demand skills
    - ✅ Explore experience requirements
    - ✅ Understand work mode distribution
    """)

    with col2:
        st.markdown("### 📊 What You'll Explore")

        st.markdown("""
    - 🏢 Company Insights
    - 📍 Location Analysis
    - 🧠 Skills Analysis
    - 👨‍💻 Experience Analysis
    - 🌐 Work Mode Analysis
    """)

    st.markdown("---")

    # ==========================
    # Dataset Summary
    # ==========================

    st.markdown("## 📂 Dataset Summary")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.success("""
    ### 📄 Records

    22,699+
    Job Listings
    """)

    with c2:
        st.success("""
    ### 🧩 Features

    31
    Dataset Columns
    """)

    with c3:
        st.success("""
    ### 📍 Coverage

    Multiple
    Indian Cities
    """)

    with c4:
        st.success("""
    ### 🏢 Includes

    Companies,
    Skills & Work Mode
    """)

    st.markdown("---")

    # ==========================
    # Key Insights
    # ==========================

    st.markdown("## 💡 Key Insights")

    st.markdown("""
    - 📌 Explore hiring patterns across India's leading technology companies.

    - 📌 Compare salary ranges across different job categories.

    - 📌 Discover the most in-demand technical skills.

    - 📌 Analyze hiring opportunities by city and work mode.

    - 📌 Understand experience-level requirements across industries.

    - 📌 Evaluate company ratings and recruitment trends.
    """)

    st.markdown("---")

    st.markdown("## 🚀 Dashboard Sections")

    # Row 1
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.info("🏠 **Home**")

    with col2:
        st.info("🏢 **Companies**")

    with col3:
        st.info("⭐ **Ratings**")

    # Row 2
    col4, col5, col6 = st.columns(3, gap="large")

    with col4:
        st.info("📍 **Locations**")

    with col5:
        st.info("💼 **Roles**")

    with col6:
        st.info("🕒 **Experience & Work Mode**")

    # Row 3
    col7, col8, col9 = st.columns(3, gap="large")

    with col7:
        st.info("🛠️ **Skills**")

    with col8:
        st.info("👨‍🎓 **Freshers Insights**")

    with col9:
        st.info("🗂️ **Cleaned Dataset**")
