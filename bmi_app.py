import streamlit as st

st.set_page_config(page_title="AI BMI Calculator", page_icon="⚖️", layout="centered")
st.title("⚖️ AI BMI & Health Metrics Calculator")
st.write("Calculate your Body Mass Index (BMI) instantly and check your health category!")

with st.form("bmi_form"):
    weight = st.number_input("Enter your weight (kg):", min_value=1.0, value=55.0)
    height_cm = st.number_input("Enter your height (cm):", min_value=50.0, value=160.0)
    submitted = st.form_submit_button("Calculate BMI")

    if submitted:
        height_m = height_cm / 100.0
        bmi = weight / (height_m ** 2)

        st.subheader("📊 Your Results")
        st.metric(label="Your BMI Score", value=f"{bmi:.2f}")

        if bmi < 18.5:
            st.warning("Category: Underweight. Focus on a nutrient-rich, balanced diet!")
        elif 18.5 <= bmi < 25:
            st.success("Category: Normal weight. Great job maintaining a healthy lifestyle!")
        elif 25 <= bmi < 30:
            st.info("Category: Overweight. Regular exercise and mindful eating can help.")
        else:
            st.error("Category: Obese. Consult a healthcare professional for personalized guidance.")
