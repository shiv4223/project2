import streamlit as st
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px


st.title('DashBoard - Tips DataSet ')

img = plt.imread('_103669660_whatsubject.jpg')
st.image(img)

data = sns.load_dataset('tips')

dataMale = data[data['sex'] == 'Male']
dataFemale = data[data['sex'] == 'Female']

st.header('Description of the Dataset')
st.dataframe(data.head())
fig = px.scatter(x = data['total_bill'],y= data['tip'],color=data["sex"],size=data['tip'])

st.plotly_chart(fig,use_container_width=True)

select = st.selectbox('Select Gender', data['sex'].unique())

if select == 'Male':
    st.image(plt.imread('Tipping.webp'))
    st.caption('This is dataSet of Males')
    st.dataframe(dataMale)
    fig = px.scatter(x = dataMale['total_bill'],y= dataMale['tip'],color=dataMale["time"],size=dataMale['tip'])
    st.plotly_chart(fig,use_container_width=True)

    button = st.button('Pie Chart')
    if button :
        fig = px.pie(dataMale,values = 'tip' , names = 'smoker' , title= 'Customer is Smoker or Not')
        st.plotly_chart(fig,use_container_width=True)
    else:
        st.caption('Click here to get the Pie Chart')

    button1 = st.button('Line Chart')
    if button1:
        st.caption('This is line Chart of dataSet of Male')
        st.line_chart(data=dataMale, x="total_bill", y="tip")
    else:
        st.caption('Click here to get the Line Chart')
    button2 = st.button('Bar Chart')

    if button2:
        st.caption('This is Bar Chart of dataSet of Male')
        st.bar_chart(data=dataMale , x='total_bill', y='tip')
    else:
        st.caption('Click here to get the Bar Chart')
    
    button3 = st.button('Area Chart')
    if button3:
        st.caption('This is Area Chart of dataSet of Male')
        st.area_chart(data=dataMale , x='total_bill', y='tip')
    else:
        st.caption('Click here to get the Bar Chart')
        
    

else:
    st.image(plt.imread('_109228852_gettyimages-947144692-1.jpg'))
    st.caption('This is dataSet of Females')
    st.dataframe(dataFemale)

    fig = px.scatter(x = dataFemale['total_bill'],y= dataFemale['tip'],color=dataFemale["time"],size=dataFemale['tip'])
    st.plotly_chart(fig,use_container_width=True)
    button = st.button('Pie Chart')
    if button :
        fig = px.pie(dataFemale,values = 'tip' , names = 'smoker' , title= 'Customer is Smoker or Not')
        st.plotly_chart(fig,use_container_width=True)
    else:
        st.caption('Click here to get the Pie Chart')
    button1 = st.button('Line Chart')
    if button1:
        st.caption('This is line Chart of dataSet of Male')
        st.line_chart(data = dataFemale,x = 'total_bill', y = 'tip')
    else:
        st.caption('Click here to get the Line Chart')
    
    button2 = st.button('Bar Chart')

    if button2:
        st.caption('This is Bar Chart of dataSet of FeMale')
        st.bar_chart(data=dataFemale , x='total_bill', y='tip')
    else:
        st.caption('Click here to get the Bar Chart')
    
    button3 = st.button('Area Chart')
    if button3:
        st.caption('This is area Chart of dataSet of feMale')
        st.area_chart(data=dataFemale , x='total_bill', y='tip')
    else:
        st.caption('Click here to get the Bar Chart')
    
    
    
