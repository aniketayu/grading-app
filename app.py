import pandas as pd
import streamlit as st

# st.title("Agricultural Development Trust Baramati")
# st.subheader("Shardabai Pawar English Medium School")

st.markdown("""
<div style='background-color:#1F618D; padding:25px; text-align:center; border-radius:10px'>
    <h1 style='color:white;'>Agricultural Development Trust Baramati</h1>
    <h2 style='color:white;'>Science and Innovation Activity Center,Baramati</h2>
     <h2 style='color:white;'>Automatic Grading System</h2>
</div>
<br>
""", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file:
    # Read Excel
    df = pd.read_excel(uploaded_file, engine="openpyxl")

    st.subheader("Preview of Uploaded Excel File")
    st.dataframe(df)

    # Select column
    column = st.selectbox("Select Marks Column", df.columns)

    # Convert column to numeric
    df[column] = pd.to_numeric(df[column], errors='coerce')

    # Grade function
    def get_grade(marks):
        if pd.isna(marks):
            return ""
        elif 91 <= marks <= 100:
            return "A1"
        elif 81 <= marks <= 90:
            return "A2"
        elif 71 <= marks <= 80:
            return "B1"
        elif 61 <= marks <= 70:
            return "B2"
        elif 51 <= marks <= 60:
            return "C1"
        elif 41 <= marks <= 50:
            return "C2"
        elif 33 <= marks <= 40:
            return "D"
        else:
            return "E"

    if st.button("Generate Grades"):
        df["Grades"] = df[column].apply(get_grade)

        st.subheader("Data with Grades")
        st.dataframe(df)

        # Save file
        output_file = "graded_output.xlsx"
        df.to_excel(output_file, index=False)

        with open(output_file, "rb") as file:
            st.download_button(
                "Download Excel File",
                file,
                file_name="graded_output.xlsx"
            )