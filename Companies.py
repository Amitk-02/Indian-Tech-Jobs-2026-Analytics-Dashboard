def comp():    
    import streamlit as st
    import plotly.express as px
    import pandas as pd

    df = pd.read_csv("cleaned_indian_tech_jobs_2026.csv")

    filtered_df = df.copy()
    st.success(f"Showing **{len(filtered_df):,}** jobs after applying filters.")

    st.header("🏢 Top Hiring Companies")

    top_company = (
            filtered_df["company_name"]
            .value_counts()
            .head(10)
            .reset_index()
        )

    top_company.columns = ["Company", "Listings"]

    left, right = st.columns([2.4, 1])

    fig = px.bar(
                top_company,
                x="Company",
                y="Listings",
                text="Listings",
                color="Listings",
                color_continuous_scale="Plasma",
                title="Top 10 Companies by Job Listings"
            )

    fig.update_traces(
                textposition="outside",
                cliponaxis=False
            )


    fig.update_layout(
                height=520,
                title_x=0.35,
                xaxis_title="Compines",
                yaxis_title="Listings",
                xaxis_tickangle=-20,
                coloraxis_colorbar=dict(title="Listings"),
                # plot_bgcolor="white",
                
            )

    st.plotly_chart(fig, use_container_width=True)

    fig = px.pie(
                top_company,
                names="Company",
                values="Listings",
                hole=0.45,
                title="Share of Top 10 Companies",
                color_discrete_sequence=px.colors.qualitative.Set3
            )

    fig.update_traces(
                textinfo="percent",
                textposition="inside"
            )

    fig.update_layout(
                height=520,
                title_x=0.18,
                legend_title="",
                plot_bgcolor="black"
            )

    st.plotly_chart(fig, use_container_width=True)

    job_company = (
    df.groupby(["skill_domain", "company_name"])
      .size()
      .reset_index(name="Job Count")
      .sort_values("Job Count", ascending=False)
    )




    st.markdown("---")
    st.subheader("📌 Company Insights")

    total_companies = filtered_df["company_name"].nunique()

    total_jobs = len(filtered_df)

    top_company = (
            filtered_df["company_name"]
            .value_counts()
            .idxmax()
        )

    top_company_jobs = (
            filtered_df["company_name"]
            .value_counts()
            .max()
        )

    avg_rating = filtered_df["company_rating"].mean()

    col1, col2, col3 = st.columns(3)

    with col1:
            st.metric(
                "🏢 Total Companies",
                f"{total_companies:,}"
            )

    with col2:
            st.metric(
                "📄 Total Job Listings",
                f"{total_jobs:,}"
            )

    with col3:
            st.metric(
                "🏆 Top Hiring Company",
                top_company,
                delta=f"{top_company_jobs} Jobs"
            )

        

    st.success(f"""
        ### 📈 Key Insights

        🏢 The dashboard contains **{total_companies:,}** unique hiring companies offering **{total_jobs:,}** job opportunities.

        🏆 **{top_company}** is the leading recruiter with **{top_company_jobs:,}** active job listings.

        ⭐ The average company rating across the dataset is **{avg_rating:.2f}/5**, indicating the overall employer satisfaction.

        📊 The charts above highlight the companies dominating the current technology job market.
        """)