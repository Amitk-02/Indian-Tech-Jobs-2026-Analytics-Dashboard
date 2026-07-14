def cleaned():
    import streamlit as st
    from streamlit_option_menu import option_menu
    import pandas as pd
    import plotly.express as px
  

    df = pd.read_csv("cleaned_indian_tech_jobs_2026.csv")

    filtered_df = df.copy()
    st.success(f"Showing **{len(filtered_df):,}** jobs after applying filters.")

    st.markdown("## 📊 Cleaned Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📄 Total Records",
            f"{len(filtered_df):,}"
        )

    with col2:
        st.metric(
            "🧾 Total Features",
            filtered_df.shape[1]
        )

    with col3:
        st.metric(
            "🏢 Companies",
            filtered_df["company_name"].nunique()
        )

    with col4:
        st.metric(
            "📍 Cities",
            filtered_df["scraped_city"].nunique()-1
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.write(df)

    st.info(
        f"""
    ### 📋 Dataset Summary

    - **Source:** Naukri.com
    - **Dataset Size:** {len(filtered_df):,} job listings
    - **Features:** {filtered_df.shape[1]} cleaned columns
    - **Companies Covered:** {filtered_df['company_name'].nunique():,}
    - **Cities Covered:** {filtered_df['scraped_city'].nunique()-1 ," And 1 Remote Work"}
    - **Role Categories:** {filtered_df['role_category'].nunique()}
    - **Experience Levels:** {filtered_df['experience_tier'].nunique()}
    - **Work Modes:** {filtered_df['work_mode'].nunique()}

    The dataset has been cleaned and standardized by handling missing values, creating role categories, extracting experience information, processing salary fields, and preparing structured features for exploratory data analysis (EDA).
    """
    )

