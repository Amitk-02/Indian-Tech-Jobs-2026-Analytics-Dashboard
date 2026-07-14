def exp():
    import streamlit as st
    from streamlit_option_menu import option_menu
    import pandas as pd
    import plotly.express as px


    df = pd.read_csv("cleaned_indian_tech_jobs_2026.csv")

    filtered_df = df.copy()
    st.success(f"Showing **{len(filtered_df):,}** jobs after applying filters.")

    st.header("🎯 Experience & Work Mode Analysis")

    fig = px.histogram(
        filtered_df,
        x="avg_experience",
        nbins=15,
        title="Distribution of Average Experience Required",
        color_discrete_sequence=["royalblue"]
    )

    fig.update_layout(
        height=500,
        title_x=0.30,
        xaxis_title="Average Experience (Years)",
        yaxis_title="Number of Job Listings",
        bargap=0.08
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    work_df = (
        filtered_df["work_mode"]
        .value_counts()
        .reset_index()
    )

    work_df.columns = ["Work Mode", "Jobs"]

    fig = px.pie(
        work_df,
        names="Work Mode",
        values="Jobs",
        hole=0.50,
        title="Work Mode Distribution",
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    fig.update_traces(
        textinfo="percent+label",
        textposition="inside"
    )

    fig.update_layout(
        height=550,
        title_x=0.30,
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    heat_df = (
        filtered_df
        .groupby(["experience_tier", "work_mode"])
        .size()
        .reset_index(name="Jobs")
    )

    fig = px.density_heatmap(
        heat_df,
        x="work_mode",
        y="experience_tier",
        z="Jobs",
        text_auto=True,
        color_continuous_scale="Viridis",
        title="Experience Level vs Work Mode"
    )

    fig.update_layout(
        height=550,
        title_x=0.30,
        xaxis_title="Work Mode",
        yaxis_title="Experience Level"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.subheader("📌 Experience & Work Mode Insights")

    top_exp = filtered_df["experience_tier"].mode()[0]
    top_work = filtered_df["work_mode"].mode()[0]

    avg_exp = filtered_df["avg_experience"].mean()

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🎯 Most Common Experience",
            top_exp
        )

    with c2:
        st.metric(
            "🏠 Preferred Work Mode",
            top_work
        )

    with c3:
        st.metric(
            "📈 Avg Experience",
            f"{avg_exp:.1f} Years"
        )

    with c4:
        st.metric(
            "💼 Total Jobs",
            f"{len(filtered_df):,}"
        )

    st.success(
        f"""
     ### 📊 Key Insights
     
     • **{top_exp}** is the most frequently requested experience level.
     
     • Employers primarily offer **{top_work}** opportunities.
     
     • The average experience required across all jobs is **{avg_exp:.1f} years**.
     
     • The heatmap shows how hiring preferences for different work modes change across experience levels.
     """
         )