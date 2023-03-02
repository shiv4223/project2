import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title("This is Project on  :red[Tips Data Set]")
st.balloons()
data = sns.load_dataset('tips')
button1 = st.button('For Description of dataset Click here')

if button1:
    st.image(plt.imread('_103669660_whatsubject.jpg'))
    st.caption('The Tips dataset is a data frame with 244 rows and 7 variables which represents some tipping data where one waiter recorded information about each tip he received over a period of a few months working in one restaurant. In all the waiter recorded 244 tips. The data was reported in a collection of case studies for business statistics (Bryant & Smith 1995).[4] The waiter collected several variables: The tip in dollars, the bill in dollars, the sex of the bill payer, whether there were smokers in the party, the day of the week, the time of day and the size of the party.')
    st.header('Description of the Dataset')
    st.dataframe(data.head())
    fig = px.scatter(x = data['total_bill'],y= data['tip'],color=data["sex"],size=data['tip'])
    st.plotly_chart(fig,use_container_width=True)

else:
    st.image(plt.imread('1621925865383.jpeg'))
    st.caption('You can click on the above button to read about the data')


