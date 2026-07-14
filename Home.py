
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
