import streamlit as st
import plotly.express as px
import utils

st.write("# Walk-Or-Run Prediction using InceptionV3 Model")

st.write("## Sample Images")

col1, col2, col3 = st.columns(3)
col1.image(("./images/man-running-uphill.jpg"), caption='Sample Run - 1')
col2.image(("./images/Runner.webp"), caption='Sample Run - 2')
col3.image(("./images/Running.jpeg"), caption='Sample Run - 3')


col4, col5, col6 = st.columns(3)
col4.image(("./images/walk_1.webp"), caption='Sample Walk - 1')
col5.image(("./images/walk_2.jpeg"), caption='Sample Walk - 2')
col6.image(("./images/walk_3.jpeg"), caption='Sample Walk - 3')

st.write("## Please upload an Image to make the prediction")
uploaded_image = st.file_uploader("", type=["jpg", "png","jpeg","webp"])

if uploaded_image:
    st.image(uploaded_image)

    button = st.button("Make Prediction", key=None)

    if button:
        prediction, predicted_class = utils.predict(uploaded_image)

        labels = {0: 'Run', 1: 'Walk'}

        classes=[]
        prob=[]
        for i,j in enumerate (prediction[0], 0):
            classes.append(labels[i])
            prob.append(round(j*100,2))

        fig = px.bar(x=classes, y=prob, text=prob, color=classes,
                     labels={"x":"Run/Walk", "y":"Probability(%)"})

        st.markdown("#### Probability Distribution Bar Chart", True)
        st.plotly_chart(fig)

        st.markdown(f"#### According to model, I am `{max(prob)}%` sure that the character in the image is `{predicted_class.capitalize()}`", True)

else:
    st.write("#### No Image Found. Pls Upload the Image.")