def loc():
    import streamlit as st
    import pandas as pd
    import plotly.express as px

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

    # ===========================================================
    # City-wise geographic distribution
    # ---------------------------------------------------------
    # City-level GeoJSON polygon files rarely exist reliably for
    # Indian cities, and name-matching against featureidkey almost
    # always fails silently (blank/grey map). A lat/lon bubble map
    # is the robust, standard approach for city-level data and is
    # fully interactive (zoom, pan, hover).
    # ===========================================================

    CITY_COORDS = {
        "bangalore": (12.9716, 77.5946), "bengaluru": (12.9716, 77.5946),
        "mumbai": (19.0760, 72.8777), "navi mumbai": (19.0330, 73.0297),
        "delhi": (28.7041, 77.1025), "new delhi": (28.6139, 77.2090),
        "gurugram": (28.4595, 77.0266), "gurgaon": (28.4595, 77.0266),
        "noida": (28.5355, 77.3910), "greater noida": (28.4744, 77.5040),
        "pune": (18.5204, 73.8567), "hyderabad": (17.3850, 78.4867),
        "secunderabad": (17.4399, 78.4983),
        "chennai": (13.0827, 80.2707), "kolkata": (22.5726, 88.3639),
        "ahmedabad": (23.0225, 72.5714), "gandhinagar": (23.2156, 72.6369),
        "jaipur": (26.9124, 75.7873), "chandigarh": (30.7333, 76.7794),
        "mohali": (30.7046, 76.7179), "panchkula": (30.6942, 76.8606),
        "kochi": (9.9312, 76.2673), "cochin": (9.9312, 76.2673),
        "thiruvananthapuram": (8.5241, 76.9366), "trivandrum": (8.5241, 76.9366),
        "indore": (22.7196, 75.8577), "bhopal": (23.2599, 77.4126),
        "nagpur": (21.1458, 79.0882), "lucknow": (26.8467, 80.9462),
        "kanpur": (26.4499, 80.3319), "coimbatore": (11.0168, 76.9558),
        "vadodara": (22.3072, 73.1812), "baroda": (22.3072, 73.1812),
        "surat": (21.1702, 72.8311), "visakhapatnam": (17.6868, 83.2185),
        "vizag": (17.6868, 83.2185), "mysore": (12.2958, 76.6394),
        "mysuru": (12.2958, 76.6394), "nashik": (19.9975, 73.7898),
        "faridabad": (28.4089, 77.3178), "ghaziabad": (28.6692, 77.4538),
        "bhubaneswar": (20.2961, 85.8245), "guwahati": (26.1445, 91.7362),
        "ranchi": (23.3441, 85.3096), "patna": (25.5941, 85.1376),
        "dehradun": (30.3165, 78.0322), "jodhpur": (26.2389, 73.0243),
        "amritsar": (31.6340, 74.8723), "ludhiana": (30.9010, 75.8573),
        "jalandhar": (31.3260, 75.5762), "raipur": (21.2514, 81.6296),
        "agra": (27.1767, 78.0081), "varanasi": (25.3176, 82.9739),
        "vijayawada": (16.5062, 80.6480), "madurai": (9.9252, 78.1198),
        "thane": (19.2183, 72.9781), "rajkot": (22.3039, 70.8022),
        "trichy": (10.7905, 78.7047), "tiruchirappalli": (10.7905, 78.7047),
        "salem": (11.6643, 78.1460), "guntur": (16.3067, 80.4365),
        "meerut": (28.9845, 77.7064), "aurangabad": (19.8762, 75.3433),
        "remote": (22.9734, 78.6569),
    }

    location_count = (
        df["scraped_city"]
        .dropna()
        .value_counts()
        .reset_index()
    )
    location_count.columns = ["city", "job_count"]

    def match_coords(city_name):
        key = str(city_name).strip().lower()
        return CITY_COORDS.get(key)

    location_count["coords"] = location_count["city"].apply(match_coords)
    mapped_df = location_count[location_count["coords"].notna()].copy()
    mapped_df["lat"] = mapped_df["coords"].apply(lambda c: c[0])
    mapped_df["lon"] = mapped_df["coords"].apply(lambda c: c[1])
    mapped_df = mapped_df.drop(columns=["coords"])

    unmapped_count = int(len(location_count) - len(mapped_df))

    st.markdown("---")

    fig_map = px.scatter_geo(
        mapped_df,
        lat="lat",
        lon="lon",
        size="job_count",
        color="job_count",
        color_continuous_scale="Viridis",
        hover_name="city",
        hover_data={"job_count": True, "lat": False, "lon": False},
        size_max=45,
        title="📍 City-wise Job Distribution Across India"
    )

    fig_map.update_geos(
        scope="asia",
        center={"lat": 22.9734, "lon": 78.6569},
        projection_scale=4.3,
        showland=True,
        landcolor="rgb(235, 240, 241)",
        showcountries=True,
        countrycolor="rgb(150, 150, 150)",
        showsubunits=True,
        subunitcolor="rgb(200, 200, 200)",
        showcoastlines=True,
        coastlinecolor="rgb(180, 180, 180)",
        bgcolor="rgba(0,0,0,0)"
    )

    fig_map.update_layout(
        height=650,
        title_x=0.28,
        margin=dict(l=0, r=0, t=50, b=0)
    )

    st.plotly_chart(fig_map, use_container_width=True)

    if unmapped_count > 0:
        st.caption(
            f"ℹ️ {unmapped_count} smaller/uncommon city entries aren't plotted on the map "
            "(coordinates not available for them), but they're still included in the "
            "bar chart, treemap, and totals above."
        )

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
            filtered_df["scraped_city"].nunique() - 1
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
