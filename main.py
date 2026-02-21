import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Car Sales Dashboard", layout="wide")

st.title("🚗 Car Sales Analytics Dashboard")
st.markdown("Interactive Business Intelligence Dashboard")


file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

if file is not None:

    
    if file.name.endswith(".csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    st.success("File Uploaded Successfully ✅")

 
    if "Price" in df.columns:
        df["Price"] = pd.to_numeric(
            df["Price"].replace(r"[\$,]", "", regex=True),
            errors="coerce"
        )

   
    st.sidebar.header("🔎 Filters")

    if "Colour" in df.columns:
        selected_colour = st.sidebar.multiselect(
            "Select Colour",
            df["Colour"].unique(),
            default=df["Colour"].unique()
        )
        df = df[df["Colour"].isin(selected_colour)]

    if "Make" in df.columns:
        selected_make = st.sidebar.multiselect(
            "Select Brand",
            df["Make"].unique(),
            default=df["Make"].unique()
        )
        df = df[df["Make"].isin(selected_make)]


    st.subheader("📊 Key Performance Indicators")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Cars", len(df))

    if "Price" in df.columns:
        col2.metric("Average Price", f"${df['Price'].mean():,.0f}")
        col3.metric("Max Price", f"${df['Price'].max():,.0f}")
        col4.metric("Min Price", f"${df['Price'].min():,.0f}")

    st.subheader("📈 Visual Analysis")

    colA, colB = st.columns(2)

    if "Price" in df.columns:
        fig1 = px.histogram(
            df,
            x="Price",
            nbins=20,
            title="Price Distribution",
            color_discrete_sequence=["#1f77b4"]
        )
        colA.plotly_chart(fig1, use_container_width=True)

    if "Make" in df.columns and "Price" in df.columns:
        avg_price_brand = df.groupby("Make")["Price"].mean().reset_index()

        fig2 = px.bar(
            avg_price_brand,
            x="Make",
            y="Price",
            title="Average Price by Brand",
            color="Make"
        )
        colB.plotly_chart(fig2, use_container_width=True)


    st.subheader("📄 Filtered Data")
    st.dataframe(df, use_container_width=True)

 
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "📥 Download Filtered Data",
        csv,
        "filtered_car_sales.csv",
        "text/csv"
    )

else:
    st.info("Please upload a file to begin.")
