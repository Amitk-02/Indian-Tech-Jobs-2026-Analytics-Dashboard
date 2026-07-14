def fresher():
    import streamlit as st
    from streamlit_option_menu import option_menu
    import pandas as pd
    import plotly.express as px
  

    df = pd.read_csv("cleaned_indian_tech_jobs_2026.csv")

    filtered_df = df.copy()
    st.success(f"Showing **{len(filtered_df):,}** jobs after applying filters.")

    st.header("🌱 Fresher Hiring Insights")

    fresher_df = (
        filtered_df["is_fresher_friendly"]
        .value_counts()
        .reset_index()
    )

    fresher_df.columns = ["Category", "Jobs"]

    fresher_df["Category"] = fresher_df["Category"].replace({
        True: "Fresher Friendly",
        False: "Experienced Only"
    })

    fig = px.pie(
        fresher_df,
        names="Category",
        values="Jobs",
        hole=0.50,
        title="Fresher Friendly Jobs Distribution",
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    fig.update_traces(
        textinfo="percent+label",
        textposition="inside"
    )

    fig.update_layout(
        height=550,
        title_x=0.30
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)


    fresh_company = (
        filtered_df[
            filtered_df["is_fresher_friendly"] == True
        ]["company_name"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    fresh_company.columns = ["Company", "Jobs"]

    fig = px.bar(
        fresh_company,
        x="Jobs",
        y="Company",
        orientation="h",
        color="Jobs",
        text="Jobs",
        title="Top 10 Companies Hiring Freshers",
        color_continuous_scale="Viridis"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        height=600,
        title_x=0.30,
        xaxis_title="Job Listings",
        yaxis_title="Company"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.subheader("📌 Fresher Hiring Insights")

    fresher_jobs = (
        filtered_df["is_fresher_friendly"] == True
    ).sum()

    experienced_jobs = (
        filtered_df["is_fresher_friendly"] == False
    ).sum()

    fresher_percent = (
        fresher_jobs / len(filtered_df)
    ) * 100

    top_company = fresh_company.iloc[0]

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🌱 Fresher Jobs",
            f"{fresher_jobs:,}"
        )

    with c2:
        st.metric(
            "💼 Experienced Jobs",
            f"{experienced_jobs:,}"
        )

    with c3:
        st.metric(
            "📊 Fresher %",
            f"{fresher_percent:.1f}%"
        )

    with c4:
        st.metric(
            "🏆 Top Hiring Company",
            top_company["Company"]
        )

    # -------------------------------------------------------
    # SUMMARY
    # -------------------------------------------------------

    st.success(
     f"""
    ### 📈 Key Insights

    🌱 **{fresher_jobs:,}** job listings are suitable for freshers.

    📊 Freshers account for **{fresher_percent:.1f}%** of all available jobs.

    🏆 **{top_company['Company']}** is the leading recruiter for fresher-friendly positions.

    💼 **{experienced_jobs:,}** jobs require prior experience, indicating a balanced demand for both entry-level and experienced professionals.
    """
        )
    