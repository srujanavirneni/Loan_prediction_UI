import json
import streamlit as st



user_options = {}

st.title('Median House Value Prediction')

streamlit_options = json.load(open("streamlit_options.json"))
for field_name, range in streamlit_options["slider_fields"].items():
    min_val, max_val = range
    current_value = round((min_val + max_val)/2)
    user_options[field_name] = st.sidebar.slider(field_name, min_val, max_val, value=current_value)

for field_name, values in streamlit_options["single_select_fields"].items():
    user_options[field_name] = st.sidebar.selectbox(field_name, values)


user_options


if st.button('Predict'):
    data = json.dumps(user_options, indent=2)
    #r = requests.post('http://143.198.29.23:8002/predict', data=data)
    st.write(data)