def loc():    
    import streamlit as st
    from streamlit_option_menu import option_menu
    import pandas as pd
    import plotly.express as px
    import json

    df = pd.read_csv("cleaned_indian_tech_jobs_2026.csv")

    filtered_df = df.copy()
    st.success(f"Showing **{len(filtered_df):,}** jobs after applying filters.")

    st.header("📍 Location Analysis")

    city_df = (
        filtered_df["scraped_city"]
        .value_counts()
        .head(15)
        .reset_index()
    )

    city_df.columns = ["City", "Jobs"]

    fig = px.bar(
        city_df,
        x="Jobs",
        y="City",
        orientation="h",
        text="Jobs",
        color="Jobs",
        color_continuous_scale="Tealgrn",
        title="Top 15 Hiring Cities"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        height=550,
        title_x=0.30,
        xaxis_title="Number of Job Listings",
        yaxis_title="City",
        yaxis=dict(categoryorder="total ascending")
    )

    st.plotly_chart(fig, use_container_width=True)

    fig = px.treemap(
        city_df,
        path=["City"],
        values="Jobs",
        color="Jobs",
        color_continuous_scale="Blues",
        title="Hiring Distribution by City"
    )

    fig.update_layout(
        height=500,
        title_x=0.28
    )

    st.plotly_chart(fig, use_container_width=True)

    location_count = df["scraped_city"].value_counts().reset_index()
    location_count.columns = ["state", "job_count"]

    with open("india_states.geojson", "r") as f:
        india_geojson = json.load(f)

    # Choropleth Map
    fig = px.choropleth(
        location_count,
        geojson=india_geojson,
        featureidkey="properties.ST_NM",
        locations="state",
        color="job_count",
        color_continuous_scale="Viridis",
        title="📍 Job Distribution Across India"
    )

    fig.update_geos(
        fitbounds="locations",
        visible=False
    )

    fig.update_layout(
        height=600,
        margin=dict(l=0, r=0, t=50, b=0)
    )


    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.subheader("📌 Location Insights")

    c1, c2, c3, c4 = st.columns(4)

    top_city = city_df.iloc[0]

    with c1:
        st.metric(
            "🏆 Top Hiring City",
            top_city["City"]
        )

    with c2:
        st.metric(
            "💼 Jobs in Top City",
            f"{top_city['Jobs']:,}"
        )

    with c3:
        st.metric(
            "📍 Total Cities",
            filtered_df["scraped_city"].nunique()-1
        )

    with c4:
        st.metric(
            "📊 Total Jobs",
            f"{len(filtered_df):,}"
        )

    st.success(
        f"""
       📍 **{top_city['City']}** is the leading hiring hub with **{top_city['Jobs']:,}** job listings.

        🏢 Jobs are distributed across **{filtered_df['scraped_city'].nunique()-1}** different cities and with 1 Remote Work in the filtered dataset.
    """
    )
