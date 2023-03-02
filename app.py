import streamlit as st
import matplotlib.pyplot as plt

st.title("This is Project on  :red[Tips Data Set ]")
st.balloons()

button1 = st.button('For Description of dataset Click here')

if button1:
    st.image(plt.imread('_103669660_whatsubject.jpg'))
    st.caption('The Tips dataset is a data frame with 244 rows and 7 variables which represents some tipping data where one waiter recorded information about each tip he received over a period of a few months working in one restaurant. In all the waiter recorded 244 tips. The data was reported in a collection of case studies for business statistics (Bryant & Smith 1995).[4] The waiter collected several variables: The tip in dollars, the bill in dollars, the sex of the bill payer, whether there were smokers in the party, the day of the week, the time of day and the size of the party.')

else:
    st.image(plt.imread('click-me.gif'))
    st.caption('You can click on the above button to read about the data')