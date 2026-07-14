def role():    
    import streamlit as st
    from streamlit_option_menu import option_menu
    import pandas as pd
    import plotly.express as px
    import Home
    import Companies

    df = pd.read_csv("cleaned_indian_tech_jobs_2026.csv")

    filtered_df = df.copy()
    st.success(f"Showing **{len(filtered_df):,}** jobs after applying filters.")
    st.header("🧩 Role Category Analysis")

    role_df = (
            filtered_df["role_category"]
            .value_counts()
            .head(10)
            .reset_index()
        )

    role_df.columns = ["Role", "Jobs"]

    fig = px.funnel(
        role_df,
        y="Role",
        x="Jobs",
        title="Top 10 Job Roles by Demand"
    )

    fig.update_traces(
        marker=dict(color="royalblue"),
        texttemplate="%{x}",
        textposition="inside"
    )

    fig.update_layout(
        height=600,
        title_x=0.30,
        yaxis_title="Role Category",
        xaxis_title="Job Listings"
    )

    st.plotly_chart(fig, use_container_width=True)

    fig = px.sunburst(
        role_df,
        path=["Role"],
        values="Jobs",
        color="Jobs",
        color_continuous_scale="Turbo",
        title="Role Category Hierarchy"
    )

    fig.update_traces(
        textinfo="label+percent entry"
    )

    fig.update_layout(
        height=500,
        title_x=0.30,
        margin=dict(t=60, l=10, r=10, b=10)
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.subheader("📌 Role Insights")

    c1, c2, c3, c4 = st.columns(4)

    top_role = role_df.iloc[0]

    with c1:
        st.metric(
            "🏆 Most Demanded Role",
            top_role["Role"]
        )

    with c2:
        st.metric(
            "💼 Job Listings",
            f"{top_role['Jobs']:,}"
        )

    with c3:
        st.metric(
            "🧩 Total Role Categories",
            filtered_df["role_category"].nunique()
        )

    with c4:
        st.metric(
            "📊 Total Jobs",
            f"{len(filtered_df):,}"
        )

    st.success(
        f"""
    🏆 **{top_role['Role']}** is the most demanded role with **{top_role['Jobs']:,}** job listings.

    📈 Your dataset contains **{filtered_df['role_category'].nunique()}** unique role categories, showing a diverse range of opportunities across the Indian tech job market.
     """
     )