from pickle import load
import streamlit as st


model = load(open("tree_classifier_crit-gini_maxdepth-5_minleaf-2_minsplit2_42.sav", "rb"))

class_dict = {
    "0": "No diabetes",
    "1": "Diabetes"   
}

st.title("Diabetes - Model prediction")
	
val1 = st.slider("Pregnancies", min_value = 0.0, max_value = 17.0, step = 0.1)
val2 = st.slider("Glucose", min_value = 56.0, max_value = 198.0, step = 0.1)
val3 = st.slider("BloodPressure", min_value = 24.0, max_value = 110.0, step = 0.1)
val4 = st.slider("SkinThickness", min_value = 7.0, max_value = 63.0, step = 0.1)
val5 = st.slider("Insulin", min_value = 14.0, max_value = 846.0, step = 0.1)
val6 = st.slider("BMI", min_value = 67.10, max_value = 18.20, step = 0.1)
val7 = st.slider("DiabetesPedigreeFunction", min_value = 0.085, max_value = 2.42, step = 0.1)
val8 = st.slider("Age", min_value = 21.0, max_value = 81.0, step = 0.1)

if st.button("Predict"):
    prediction = str(model.predict([[val1, val2, val3, val4, val5, val6, val7, val8,]])[0])
    pred_class = class_dict[prediction]
    st.write("Prediction:", pred_class)