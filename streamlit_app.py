import streamlit as st

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

def main():
    st.set_page_config(page_title="Student Performance Indicator")
    st.title("Student Performance Indicator")

    st.write("Welcome to the Student Performance Prediction App!")

    gender = st.selectbox("Gender", ["female", "male"])
    race_ethnicity = st.selectbox(
        "Race/Ethnicity",
        ["group A", "group B", "group C", "group D", "group E"],
    )
    parental_level_of_education = st.selectbox(
        "Parental Level of Education",
        [
            "some high school",
            "high school",
            "some college",
            "associate's degree",
            "bachelor's degree",
            "master's degree",
        ],
    )
    lunch = st.selectbox("Lunch", ["standard", "free/reduced"])
    test_preparation_course = st.selectbox(
        "Test Preparation Course", ["none", "completed"]
    )
    reading_score = st.number_input("Reading Score", min_value=0, max_value=100, step=1)
    writing_score = st.number_input("Writing Score", min_value=0, max_value=100, step=1)

    if st.button("Predict"):
        input_data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score,
        )

        result = PredictPipeline().predict(input_data.get_data_as_data_frame())
        st.success(f"Predicted Math Score: {float(result[0]):.2f}")

if __name__ == "__main__":
    main()
