def skill():
    import streamlit as st
    from streamlit_option_menu import option_menu
    import pandas as pd
    import plotly.express as px
  

    df = pd.read_csv("cleaned_indian_tech_jobs_2026.csv")

    filtered_df = df.copy()
    st.success(f"Showing **{len(filtered_df):,}** jobs after applying filters.")

    st.header("🛠 Skill Analysis")

    role_df = (
        filtered_df["role_category"]
        .value_counts()
        .reset_index()
    )

    role_df.columns = ["Role", "Jobs"]

    fig = px.bar(
        role_df,
        x="Role",
        y="Jobs",
        color="Jobs",
        text="Jobs",
        title="Job Distribution by Role Category",
        color_continuous_scale="Viridis"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        height=550,
        title_x=0.30,
        xaxis_title="Role Category",
        yaxis_title="Number of Job Listings",
        xaxis_tickangle=-20
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    heat_df = (
        filtered_df
        .groupby(["role_category", "experience_tier"])
        .size()
        .reset_index(name="Jobs")
    )

    fig = px.density_heatmap(
        heat_df,
        x="experience_tier",
        y="role_category",
        z="Jobs",
        text_auto=True,
        color_continuous_scale="Turbo",
        title="Role Category vs Experience Level"
    )

    fig.update_layout(
        height=600,
        title_x=0.30,
        xaxis_title="Experience Level",
        yaxis_title="Role Category"
    )

    st.plotly_chart(fig, use_container_width=True)

    job_company = (
    df.groupby(["skill_domain", "company_name"])
      .size()
      .reset_index(name="Job Count")
      .sort_values("Job Count", ascending=False)
        )
    
    

    st.markdown("---")
    st.subheader("📌 Role Category Insights")

    top_role = role_df.iloc[0]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🏆 Most Demanded Role",
            top_role["Role"]
        )

    with col2:
        st.metric(
            "💼 Job Listings",
            f"{top_role['Jobs']:,}"
        )

    with col3:
        st.metric(
            "📂 Total Role Categories",
            filtered_df["role_category"].nunique()
        )

    with col4:
        st.metric(
            "📊 Total Jobs",
            f"{len(filtered_df):,}"
        )

    st.success(
        f"""
    🏆 **{top_role['Role']}** is the most demanded role category with **{top_role['Jobs']:,}** job listings.

    📈 The dataset contains **{filtered_df['role_category'].nunique()}** role categories.

    🔥 The heatmap shows how hiring demand for each role category changes across different experience levels.
    """
        )