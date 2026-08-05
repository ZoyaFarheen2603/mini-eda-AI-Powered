import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

from google import genai


# ----------------------------
# Streamlit Config
# ----------------------------
st.set_page_config(page_title="Mini EDA App", layout="wide")

st.title("📊 Mini AI-Powered EDA Report")
st.write("Upload a CSV file and explore your dataset.")

uploaded_file = st.file_uploader(
    "Choose CSV File",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset Loaded Successfully!")

    st.sidebar.title("Navigation")

    option = st.sidebar.radio(
        "Go To",
        [
            "Dataset",
            "Overview",
            "Missing Values",
            "Statistics",
            "Correlation",
            "Distribution",
            "AI Pandas Assistant"
        ]
    )


    # ----------------------------
    # Dataset
    # ----------------------------
    if option == "Dataset":

        st.subheader("Dataset")

        st.dataframe(df)

    # ----------------------------
    # Overview
    # ----------------------------
    elif option == "Overview":

        st.subheader("Dataset Overview")

        col1, col2, col3 = st.columns(3)

        col1.metric("Rows", df.shape[0])
        col2.metric("Columns", df.shape[1])
        col3.metric("Duplicates", df.duplicated().sum())

        st.write("### Data Types")

        st.dataframe(df.dtypes.astype(str))

    # ----------------------------
    # Missing Values
    # ----------------------------
    elif option == "Missing Values":

        st.subheader("Missing Values")

        missing = df.isnull().sum()
        missing = missing[missing > 0]

        if len(missing) == 0:

            st.success("No Missing Values Found 🎉")

        else:

            st.bar_chart(missing)

    # ----------------------------
    # Statistics
    # ----------------------------
    elif option == "Statistics":

        st.subheader("Summary Statistics")

        st.dataframe(df.describe())

    # ----------------------------
    # Correlation
    # ----------------------------
    elif option == "Correlation":

        numeric = df.select_dtypes(include="number")

        if numeric.shape[1] < 2:

            st.warning("Need at least two numeric columns.")

        else:

            corr = numeric.corr()

            fig, ax = plt.subplots(figsize=(8,6))

            cax = ax.imshow(corr, cmap="coolwarm")

            ax.set_xticks(range(len(corr.columns)))
            ax.set_xticklabels(corr.columns, rotation=45)

            ax.set_yticks(range(len(corr.columns)))
            ax.set_yticklabels(corr.columns)

            plt.colorbar(cax)

            st.pyplot(fig)

    # ----------------------------
    # Distribution
        # ----------------------------
    # Distribution
    # ----------------------------
    elif option == "Distribution":

        numeric = df.select_dtypes(include="number").columns

        if len(numeric) == 0:
            st.warning("No Numeric Columns")
        else:
            column = st.selectbox("Select Column", numeric)

            fig, ax = plt.subplots()
            ax.hist(df[column].dropna(), bins=20)
            ax.set_title(column)
            st.pyplot(fig)

    # ----------------------------
    # AI Assistant
    # ----------------------------
    elif option == "AI Pandas Assistant":

        st.subheader("🤖 AI Pandas Code Generator")

        api_key = st.text_input(
            "Enter your Gemini API Key",
            type="password",
            help="Get a free Gemini API Key from Google AI Studio."
        )

        if not api_key:
            st.info("Enter your Gemini API Key to use the AI Assistant.")
        else:
            client = genai.Client(api_key=api_key)

            user_query = st.text_input(
                "What analysis do you want to perform?",
                placeholder="Example: Show average marks department-wise"
            )

            if st.button("Generate Pandas Code"):
                if user_query.strip() == "":
                    st.warning("Please enter a query.")
                else:
                    prompt = f"""
You are an expert Python Data Analyst.

Dataset Columns:
{list(df.columns)}

Data Types:
{df.dtypes.to_string()}

User Request:
{user_query}

Rules:
1. Generate ONLY executable pandas code.
2. Assume dataframe name is df.
3. Return ONLY Python code.
4. No explanation.
5. No markdown.
"""
                    with st.spinner("Generating Code..."):
                        response = client.models.generate_content(
                            model="gemini-3.5-flash",
                            contents=prompt
                        )

                    st.success("Generated Pandas Code")
                    st.code(response.text, language="python")

else:
    st.info("📂 Upload a CSV file to begin.")
