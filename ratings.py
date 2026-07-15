def rate():    
    import streamlit as st
    from streamlit_option_menu import option_menu
    import pandas as pd
    import plotly.express as px

    df = pd.read_csv("cleaned_indian_tech_jobs_2026.csv")

    filtered_df = df.copy()
    st.success(f"Showing **{len(filtered_df):,}** jobs after applying filters.")
    st.header("⭐ Company Rating Analysis")

    rating_df = (
            filtered_df["company_rating"]
            .round(1)
            .value_counts()
            .sort_index(ascending=False)
            .reset_index()
        )

    rating_df.columns = ["Rating", "Jobs"]

    fig = px.bar(
            rating_df,
            x="Jobs",
            y="Rating",
            orientation="h",
            text="Jobs",
            color="Jobs",
            color_continuous_scale="Plasma",
            title="Company Ratings Distribution"
        )

    fig.update_traces(
            textposition="outside"
        )

    fig.update_layout(
            height=550,
            title_x=0.30,
            xaxis_title="Number of Job Listings",
            yaxis_title="Company Rating"
        )

    st.plotly_chart(fig, use_container_width=True)

    fig = px.line(
            rating_df.sort_values("Rating"),
            x="Rating",
            y="Jobs",
            markers=True,
            title="Distribution of Company Ratings"
        )

    fig.update_traces(
            line=dict(width=3),
            marker=dict(size=8)
        )

    fig.update_layout(
            height=500,
            title_x=0.28,
            xaxis_title="Company Rating",
            yaxis_title="Number of Job Listings",
        )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 📌 Rating Insights")

    c1, c2, c3, c4 = st.columns(4)

    highest_company = (
            filtered_df.sort_values("company_rating", ascending=False)
            .iloc[0]
        )

    with c1:
            st.metric(
                "⭐ Average Rating",
                f"{filtered_df['company_rating'].mean():.2f}/5"
            )

    with c2:
            st.metric(
                "🏆 Highest Rating",
                f"{highest_company['company_rating']:.1f}"
            )
            st.caption(highest_company["company_name"])

    with c3:
            st.metric(
                "📈 Rated 4.0+",
                f"{(filtered_df['company_rating'] >= 4).sum():,}"
            )
            st.caption("High-rated job listings")

    with c4:
            st.metric(
                "🏢 Rated Companies",
                f"{filtered_df['company_name'].nunique():,}"
            )
            st.caption("Unique companies")

    st.markdown("### 📋 Quick Insights")

    st.success(
            f"""
        ⭐ **Average company rating is {filtered_df['company_rating'].mean():.2f}/5.**

        🏆 **Highest rated company:** {highest_company['company_name']}
        ({highest_company['company_rating']:.1f}/5)

        📈 **{(filtered_df['company_rating'] >= 4).sum():,}** job listings belong to companies rated **4.0 or above**.

        🏢 **{filtered_df['company_name'].nunique():,}** unique companies have rating information.
        """
        )
