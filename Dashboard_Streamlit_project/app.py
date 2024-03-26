# ---------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------
#
#               S  T  R  E  A  M  L  I  T       S  C  R  I  P  T       G   E  T  -  A  R  O  U  N  D    p r o j e c t 
# 
# ---------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------

# - - - - - - - - - - - - - - - - - - - - - - - - -  DOYON-DOUSSE Doriane (ds-fs-od-03) - - - - - - - - - - - - - - - - - - - - - - - - - 


# IMPORTATIONS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ----------------------------------------------------------------------------------------------------------------------------
import streamlit as st
from streamlit_lottie import st_lottie
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.subplots as sp
import numpy as np
from plotly.subplots import make_subplots
from PIL import Image
import requests
import json 


# CONFIG - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ----------------------------------------------------------------------------------------------------------------------------
st.set_page_config(
    page_title="🚘 Get Around Project 🚖",
    page_icon="🚙 🚖 🚘",
    layout="wide"
)
# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------
# WEB APP CODE  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------

st.title('Get Around Analysis Project 🚖')
st.subheader('Delay of users analysis ⏰')
# st.markdown("🚗  🚙  🚕 ✹ 🚗  🚙  🚕 ✹ 🚗  🚙  🚕 ✹ 🚗  🚙  🚕 ✹ 🚗  🚙  🚕 ✹ 🚗  🚙  🚕 ✹ 🚗  🚙  🚕 ✹ 🚗  🚙  🚕 ✹ 🚗  🚙  🚕 ✹ 🚗  🚙  🚕 ✹ 🚗  🚙  🚕 ✹ 🚗  🚙  🚕 ✹ 🚗  🚙  🚕 ✹ 🚗  🚙  🚕 ")
st.markdown("---")
st_lottie("https://lottie.host/5bbce746-ff03-42c9-b238-6fbb945d158d/92acIt72ld.json")

presentation_tab, analysis_tab, simulations_tab = st.tabs(["Presentation", "Analysis", "Simulations"])

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#                     P    R    E    S    E    N    T    A    T    I    O    N           T    A    B
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
with presentation_tab : 

# First part (presentation)  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    st.markdown("---")
    st.header('🔹PRESENTATION 🔹')
    st.markdown("---")
    st.markdown("")
    st.subheader('🔹 What is Getaround ? ')
    st.markdown("")
    st.markdown("")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("👉🏼 **A short description of the company** 👈🏼")
        st.markdown('* GetAround is the Airbnb for cars.')
        st.markdown('* You can rent cars from any person for a few hours to a few days!')
        st.markdown('* Founded in 2009, this company has known rapid growth.') 
        st.markdown('* In 2019, they count over 5 million users and about 20K available cars worldwide.')

    with col2:
        st.markdown("👉🏼 **Maybe you have already seen them?** 👈🏼")
        image_ga = Image.open('getaround3152.jpg')
        st.image(image_ga, caption='Here is their logo')

    st.write("---")

# Context  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    st.subheader('🔹 What is the process when I rent a car on Getaround ?')
    st.markdown("")
    st.markdown("")
    st.markdown("")

    col1, col2 = st.columns(2)

    with col1:
        st.write("""When renting a car, our users have to complete a checkin flow at the beginning of the rental and a checkout flow at the end of the rental in order to:""")
        st.write("""- Assess the state of the car and notify other parties of pre-existing damages or damages that occurred during the rental.""")
        st.write("""- Compare fuel levels.""")
        st.write("""- Measure how many kilometers were driven.""")
        st.markdown("")
        st.write("""The checkin and checkout of our rentals can be done with three distinct flows:""")
        st.write("""- 📱 Mobile rental agreement on native apps: driver and owner meet and both sign the rental agreement on the owner’s smartphone""")
        st.write("""- 🖥️ Connect: the driver doesn’t meet the owner and opens the car with his smartphone""")
        st.write("""- 📝 Paper contract (negligible)""")

    with col2:
        image = Image.open('0efa5fe10b1cb7a9f8a1ab1f783da95c_fgraphic.png')
        st.image(image, caption='Download the Getaround app and book a car for the next hour! ')

    st.markdown("---")




# Project goals  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    st.subheader('🔹 Why Getaround needs our Data Science skills ?')
    st.markdown("")
    st.markdown("")
    st.markdown("")

    col1, col2 = st.columns(2)

    with col1:
        st.write("""When using Getaround, drivers book cars for a specific time period, from an hour to a few days long.""") 
        st.write("""They are supposed to bring back the car on time, **but it happens from time to time that drivers are late for the checkout.**""")
        st.markdown("")
        st.write("""Late returns at checkout can generate **high friction for the next driver** if the car was supposed to be rented again on the same day : Customer service often reports users unsatisfied because they had to wait for the car to come back from the previous rental or users that even had to cancel their rental because the car wasn’t returned on time.""")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.subheader('**Our data mission** 🎯')
        st.markdown("")
        st.write("""The goal is to **implement a minimum delay between two rentals**, with a trade off that **won't hurt Getaround/owners revenues too much.**""")
        st.write("""Based on data insights from 2017, as Data Scientits we will have help the company find :""")
        st.write("""- **An optimal threshold :** define how long should the minimum delay be""")   
        st.write("""- **Scope :** which of the 3 flows to operate the threshold""" )
        st.write("""This dashboard goal is to respond to those problematics with clarity for Getaround decision makers.""")

    with col2:
        image_late = Image.open('I-am-late-deposit-photos.jpg')
        st.image(image_late, caption="Oups, another late user... Sorry for the next client's nerves 🫢")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#                            A    N    A    L    Y    S    I    S            T    A    B
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# ----------------------------------------------------------------------------------------------------------------------------
# Delay analysis  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# ----------------------------------------------------------------------------------------------------------------------------
with analysis_tab:

    st.markdown("---")
    st.header('🔸 DELAY ANALYSIS 🔸')
    st.markdown("---")



# Loading data  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    DATA_URL = ("https://jedha-deployment.s3.amazonaws.com/get_around_delay_analysis.xlsx")

    @st.cache_data
    def load_data():
        data = pd.read_excel(DATA_URL, sheet_name='rentals_data')
        return data

    data_load_state = st.text('Loading data ...')
    data = load_data()
    data_load_state.text("")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Here are the 10 first rows from Getaround dataset: ')
        st.write(data.head(10)) 

    with col2:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.caption("Description of the dataset columns 👋🏼 ")
        description = pd.read_excel(DATA_URL, sheet_name='Documentation')
        pd.set_option('display.max_colwidth', None)
        st.write(description)

    st.subheader('Please click on this button if you want to see the entiere dataset 👇🏼')
    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(data)   

    st.markdown("---")

# ----------------------------------------------------------------------------------------------------------------------------
# VISUALIZATIONS  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Some statitstics   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
with analysis_tab:

    st.subheader("🔸 Some statistic informations ")
    st.markdown("")

    nunique_car_id = data['car_id'].nunique()
    total_rent = len(data)
    names_checkin = ['Mobile checkin', 'Connect checkin']

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric(label = "Number of cars available", value = data['car_id'].nunique())
    with col2:
        st.metric(label = "Total number of rentals", value = total_rent)
    with col3 :
        st.metric(
            label = "Biggest delay from client (in hour)", 
            value= f"{round(data['time_delta_with_previous_rental_in_minutes'].max() / 60)} hour")
    with col4 :
        st.metric(
            label = "Most used checkin flow type", 
            value= names_checkin[0])
    with col5 :
        st.metric(
            label = "Cancelation frequency", 
            value = "1.5 / 10 user")

    st.markdown('---')


# State & Checkin'  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    st.subheader("🔸 State of reservations & Checkin' flow type")
    st.markdown("")
    st.caption("How often do clients cancel? Which flow do they use to make book a car?")
    st.markdown("")

    col1, col2, col3 = st.columns(3)

    with col1:
        checkin_value_counts = data['checkin_type'].value_counts()
        pie_checkin_values = [checkin_value_counts[0], checkin_value_counts[1]]
        names_checkin = ['Mobile checkin', 'Connect checkin']
        fig = px.pie(values=pie_checkin_values, names=names_checkin,
                color_discrete_sequence=px.colors.sequential.Sunset,
                title="Flow used by clients for Checkin'")
        fig.update_layout(autosize=False, width=550, height=550)
        st.plotly_chart(fig)

    with col2:
        state_value_counts = data['state'].value_counts()
        pie_state = [state_value_counts[0], state_value_counts[1]]
        names = ['Cancelled', 'Ended']
        fig = px.pie(values=pie_state, names=names,color_discrete_sequence=px.colors.sequential.Sunset[1:],title="State of reservations : Cancelation rate (%)")
        fig.update_layout(autosize=False,width=600,height=600)
        st.plotly_chart(fig)

    with col3:
        st_lottie("https://lottie.host/63376e1c-0453-4d19-884b-97282829b5ff/r5WyPwOJJP.json")

    st.markdown('---')


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Delays distribution  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    st.subheader("🔸 Distribution of delays at checkout")
    st.markdown("")
    st.caption("How does delay are dispatched in time? ")
    st.markdown("")

    counts, bins = np.histogram(data.delay_at_checkout_in_minutes, bins=range(-300, 300, 2))
    bins = 0.5 * (bins[:-1] + bins[1:])
    fig = px.bar(x=bins, y=counts, labels={'x':'delay_at_checkout_in_minutes', 'y':'count'})
    fig.update_layout(title="Bar plot showing distribution of Delays at chekout", autosize=False, width=1500, height=600)
    st.plotly_chart(fig)
    st.markdown("---")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Delays stats  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    st.subheader("🔸 Delays global statistics ")
    st.markdown("")
    st.caption("Who are the latecomers? What time does it represents?")
    st.markdown("")

# some preprocessing //////////////////////////////////////////////////////////////////////

    data.dropna(subset = ['delay_at_checkout_in_minutes'], inplace = True)

    def latecomers_function(x):
        if x <= 15:
            return "Less than 15 min late"
        elif 16 <= x <= 30:
            return "16-30 min late"
        elif 31 <= x <= 45:
            return "31-45 min late"
        elif 46 <= x <= 60:
            return "45min-1h late"
        elif 61 <= x <= 120:
            return "1-2 hour"
        elif 121 <= x <= 180:
            return "2-3 hour"
        elif 181 <= x <= 240:
            return "3-4 hour"
        elif 241 <= x <= 300:
            return "4-5 hour"
        elif 301 <= x <= 360:
            return "5-6 hour"
        else:
            return 'More than 6 hour delay'

    data['delay_ordered'] = data['delay_at_checkout_in_minutes'].apply(latecomers_function)
# ////////////////////////////////////////////////////////////////////////////////////////////

    col1, col2, col3 = st.columns(3)

    with col1:
        data['early_or_late'] = data['delay_at_checkout_in_minutes']
        pd.to_numeric(data['early_or_late'])
        data['early_or_late'] = data['early_or_late'].apply(lambda x: 'On_Time' if x < 0 else 'Late')
        data['early_or_late'].value_counts()
        fig = px.histogram(data, x='early_or_late', color='early_or_late', title = "Client Early or on time /vs/ Latecomers at Checkout")
        fig.update_layout(autosize=False,width=500, height=500)
        st.plotly_chart(fig)
        value_count_delay = data['early_or_late'].value_counts()
        st.write('Percentage of late clients : ', round((value_count_delay[0] / len(data['early_or_late'])*100)), "%")
        st.write('Percentage of early or on time clients : ', round((value_count_delay[1] / len(data['early_or_late'])*100)), "%")

    with col2:
        pie_delay = data['delay_ordered'].value_counts()
        delay_counts = data['delay_ordered'].value_counts()
        pie_delay_ordered = [delay_counts[0], delay_counts[1], delay_counts[2], delay_counts[3], delay_counts[4], delay_counts[5], delay_counts[6], delay_counts[7], delay_counts[8]]
        names = ['Less than 15 min late', '1-2 hour', '16-30 min late', '31-45 min late', 'More than 6 hour delay', '2-3 hour', '3-4 hour', '4-5 hour', '5-6 hour']
        fig = px.pie(values=pie_delay_ordered, names=names, color_discrete_sequence=px.colors.sequential.Sunset[1:], title="LATECOMERS : Delay time at checkout (%)")
        fig.update_layout(autosize=False,width=500, height=500)
        st.plotly_chart(fig)

    with col3:
        fig = px.box(data, x='checkin_type', y='delay_at_checkout_in_minutes',  color='checkin_type',color_discrete_sequence= px.colors.sequential.Sunset[5:],range_y=[-200, 200])
        fig.update_layout(title = "Delay time according to Checkin' Flow", autosize=False, width=500, height=500)
        st.plotly_chart(fig)

    st.markdown('---')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#  Average of delays  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    st.subheader("🔸 Averages of delays analysis")
    st.markdown("")
    st.caption("Whhat is the average time taken by latecomers, early/on time clients ?  Let's do a deeper analysis.")
    st.markdown("")

    col1, col2, col3 = st.columns(3)

    with col1:
        fig = go.Figure(data=[go.Histogram(x=data['delay_at_checkout_in_minutes'], xbins=dict(start=-500, end=500, size=10), opacity=0.75)])
        fig.add_vline(x=59, line_width=5, line_dash="dash", line_color="orange")
        fig.add_vrect(x0=-300, x1=300, annotation_text="All values included", annotation_position="top right",fillcolor="yellow", opacity=0.2, line_width=0)
        fig.update_layout(title="Global average delay at checkout (59min nearly 1hour)",autosize=False,width=500,height=450)
        st.plotly_chart(fig)

    with col2:
        fig = go.Figure(data=[go.Histogram(x=data['delay_at_checkout_in_minutes'], xbins=dict(start=-500, end=500, size=10), opacity=0.75)])
        fig.add_vline(x=-135, line_width=4, line_dash="dash", line_color="orange")
        fig.add_vrect(x0=0, x1=-300, annotation_text="Early or On Time", annotation_position="top left",fillcolor="green", opacity=0.2, line_width=0)
        fig.update_layout(title="Early or on Time delay at checkout (-135min / 2hours approx)",autosize=False,width=500,height=450)
        st.plotly_chart(fig)

    with col3:
        fig = go.Figure(data=[go.Histogram(x=data['delay_at_checkout_in_minutes'], xbins=dict(start=-500, end=500, size=10), opacity=0.75)])
        fig.add_vline(x=201, line_width=5, line_dash="dash", line_color="orange")
        fig.add_vrect(x0=0, x1=300, annotation_text="Latecomers", annotation_position="top right", fillcolor="red", opacity=0.2, line_width=0)
        fig.update_layout(title="Latecomers average delay at checkout (202min nearly 3hours)", autosize=False, width=500,height=450)
        st.plotly_chart(fig)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#  Time delta analysis   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    st.subheader("🔸 Time delta analysis")
    st.markdown("")
    st.caption("What is the timegap between two rentals? Understanding this will help us define optimal timegap. ")
    st.markdown("")

# some preprocessing /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    df_time_delta = data
    df_time_delta = df_time_delta.dropna(subset='time_delta_with_previous_rental_in_minutes') # dropping missing values in column 

    time_delta_30min = df_time_delta[df_time_delta['time_delta_with_previous_rental_in_minutes'] <= 30]
    time_delta_1h = df_time_delta[df_time_delta['time_delta_with_previous_rental_in_minutes'] <= 60]
    time_delta_1h30 = df_time_delta[df_time_delta['time_delta_with_previous_rental_in_minutes'] <= 90]
    time_delta_2h = df_time_delta[df_time_delta['time_delta_with_previous_rental_in_minutes'] <= 120]
    time_delta_2h30 = df_time_delta[df_time_delta['time_delta_with_previous_rental_in_minutes'] <= 180]
    time_delta_3h = df_time_delta[df_time_delta['time_delta_with_previous_rental_in_minutes'] <= 240]
    time_delta_3h30 = df_time_delta[df_time_delta['time_delta_with_previous_rental_in_minutes'] <= 300]
    time_delta_4h = df_time_delta[df_time_delta['time_delta_with_previous_rental_in_minutes'] <= 360]
    time_delta_4h30 = df_time_delta[df_time_delta['time_delta_with_previous_rental_in_minutes'] <= 420]
    time_delta_5h = df_time_delta[df_time_delta['time_delta_with_previous_rental_in_minutes'] <= 480]
    time_delta_5h30 = df_time_delta[df_time_delta['time_delta_with_previous_rental_in_minutes'] <= 540]
    time_delta_6h = df_time_delta[df_time_delta['time_delta_with_previous_rental_in_minutes'] >= 620]

    perc_30min = round((len(time_delta_30min) / len(df_time_delta))*100, 2)
    perc_1h = round((len(time_delta_1h) / len(df_time_delta))*100, 2) - perc_30min
    perc_1h30 = round((len(time_delta_1h30) / len(df_time_delta))*100, 2) - (perc_30min + perc_1h)
    perc_2h = round((len(time_delta_2h) / len(df_time_delta))*100 - (perc_30min + perc_1h + perc_1h30), 2)
    perc_2h30 = round((len(time_delta_2h30) / len(df_time_delta))*100 - (perc_30min + perc_1h + perc_1h30 + perc_2h), 2)
    perc_3h = round((len(time_delta_3h) / len(df_time_delta))*100- (perc_30min + perc_1h + perc_1h30 + perc_2h + perc_2h30), 2)
    perc_3h30 = round((len(time_delta_3h30) / len(df_time_delta))*100 - (perc_30min + perc_1h + perc_1h30 + perc_2h + perc_2h30 + perc_3h), 2)
    perc_4h = round((len(time_delta_4h) / len(df_time_delta))*100 - (perc_30min + perc_1h + perc_1h30 + perc_2h + perc_2h30 + perc_3h + perc_3h30), 2)
    perc_4h30 = round((len(time_delta_4h30) / len(df_time_delta))*100 - (perc_30min + perc_1h + perc_1h30 + perc_2h + perc_2h30 + perc_3h + perc_3h30 + perc_4h), 2)
    perc_5h = round((len(time_delta_5h) / len(df_time_delta))*100 - (perc_30min + perc_1h + perc_1h30 + perc_2h + perc_2h30 + perc_3h + perc_3h30 + perc_4h + perc_4h30), 2)
    perc_5h30 = round((len(time_delta_5h30) / len(df_time_delta))*100 - (perc_30min + perc_1h + perc_1h30 + perc_2h + perc_2h30 + perc_3h + perc_3h30 + perc_4h + perc_4h30 + perc_5h), 2)
    perc_6h_more = round((len(time_delta_6h) / len(df_time_delta))*100, 2) 

    time_delta_average = round(df_time_delta['time_delta_with_previous_rental_in_minutes'].mean(), 2)
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    col1, col2, col3 = st.columns(3)

    with col1 : 
        st_lottie("https://lottie.host/349d4285-c905-4390-8d13-91f53f632675/2EUEZzpDmp.json")

    with col2 : 
        delta_values = [perc_30min, perc_1h, perc_1h30, perc_2h, perc_2h30, perc_3h, perc_3h30, perc_4h, perc_4h30, perc_5h, perc_5h30, perc_6h_more]
        delta_names = ['30min', '1h', '1h30', '2h', '2h30', '3h', '3h30', '4h', '4h30', '5h', '5h30', 'More than 6h']
        fig = px.pie(values=delta_values, names=delta_names, color_discrete_sequence=px.colors.sequential.Aggrnyl_r[1:], title="TIME DELTA : Time difference between two rental (within 12h)")
        fig.update_layout(autosize=False, width=500, height=550)
        st.plotly_chart(fig)

    with col3 : 
        fig = go.Figure(data=[go.Histogram(x=df_time_delta['time_delta_with_previous_rental_in_minutes'], opacity=0.6, marker = {'color' : 'green'})]) 
        fig.add_vline(x=276.86, line_width=5, line_dash="dash", line_color="orange")
        fig.add_vrect(x0=0, x1=30, annotation_text="30", annotation_position="top left",fillcolor="red", opacity=0.2, line_width=0)
        fig.add_vrect(x0=30, x1=60, annotation_text="1h", annotation_position="bottom right",fillcolor="yellow", opacity=0.2, line_width=0)
        fig.add_vrect(x0=60, x1=90, annotation_text="1h30", annotation_position="top right",fillcolor="blue", opacity=0.2, line_width=0)
        fig.add_annotation(dict(font=dict(color='orange',size=15), x=0.5,y=0.9,showarrow=False,text="276.86min (5h01)",textangle=0,xanchor='left',xref="paper",yref="paper"))
        fig.update_layout(title="Average time delta with previous rental (minutes)",xaxis_title = "Time delta (minutes)",autosize=False,width=500,height=550)
        st.plotly_chart(fig)

    st.markdown("----")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#  Overlapping analysis   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    st.subheader("🔸 Overlapping analysis")
    st.markdown("")
    st.caption("What happens when a late clients overlap on next rental, let's analysis this. ")
    st.markdown("")

# some preprocessing /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    subset = data.loc[:, ['rental_id', 'car_id', 'state', 'checkin_type','delay_at_checkout_in_minutes', 'previous_ended_rental_id', 'time_delta_with_previous_rental_in_minutes']] # selection of columns of interest
    df_overlap_with_na = subset.sort_values(by=['car_id', 'rental_id']) # sorting value 
    df_overlap = df_overlap_with_na.dropna(subset='time_delta_with_previous_rental_in_minutes')
    df_overlap['__previous_client_delay__'] = np.nan 

    for i, r in df_overlap.iterrows():
        previous = r['previous_ended_rental_id']
        if pd.notnull(previous):
            previous_delay = df_overlap.loc[df_overlap['rental_id'] == previous, 'delay_at_checkout_in_minutes']
            if not previous_delay.empty:
                df_overlap.loc[i, '__previous_client_delay__'] = previous_delay.iloc[0]
    df_overlap['__delta__'] = df_overlap['time_delta_with_previous_rental_in_minutes'] - df_overlap['__previous_client_delay__']

    df_issue = df_overlap[df_overlap['__delta__'] < 0]

    def delta_function(x):
        if x >= -15:
            return "Less than 15 min"
        elif -16 >= x >= -30:
            return "16-30 min"
        elif -31 >= x >= -60:
            return "31min-1h"
        elif -60 >= x >= -120:
            return "1-2 hour"
        else:
            return 'More than 2 hour'

    df_issue['__delta_category__'] = df_issue['__delta__'].apply(delta_function)
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    col1, col2, col3 = st.columns(3)

    with col1: 
        perc_global_issue = round(100 * len(df_issue) / len(df_overlap), 2) # from all data : percentage of renting causing issue (no time between rent)
        perc_global_okay = 100 - perc_global_issue # from all data : percentage of renting without issue
        percentages = [perc_global_issue, perc_global_okay]
        names = ['OVERLAP', 'No overlap']
        fig = go.Figure(data=[go.Pie(labels=names, values=percentages, pull=[0.2, 0])])
        fig.update_layout(autosize=False,title="Overlapping percentage over all rentings (%)", width=550, height=550) #width=700, height=700)
        st.plotly_chart(fig)

    with col2:  
        category_order = ['Less than 15 min', '31min-1h', '1-2 hour', '16-30 min']
        fig = px.histogram(df_issue, x='__delta_category__', histnorm='percent', category_orders=category_order, color_discrete_sequence=px.colors.sequential.Agsunset[1:])
        fig.update_layout(autosize=False,title="OVERLAPPING ISSUES : classifying delay time", xaxis_title = 'Time token on next client (minutes)', width=500, height=500) #width=800, height=600)
        st.plotly_chart(fig)
    
    with col3:  
        st_lottie('https://lottie.host/b22df643-33b1-4f1a-88cb-c7db9b5a5bc4/sC4HO53tn9.json')


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#                        S    I    M    U    L    A    T    I    O    N    S           T    A    B
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////                  

# ----------------------------------------------------------------------------------------------------------------------------
# SIMULATIONS  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# some preprocessing /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
empty_list = [] # We create an empty list that will serve to append informations collected 
to_test = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240] # In a list we set a value for every 15min until 4h as the threshold to be tested 

for testing_loop in to_test: # Using a for loop called 'testing_loop' to iterate over the list 'to_test' we created previously
    filter_time = df_overlap[df_overlap['time_delta_with_previous_rental_in_minutes'] > testing_loop] # keeping rental with time delta superior to threshold
    loss = df_overlap.shape[0] - len(filter_time) # number of lost clients 
    all_loss_rents_perc = round((loss / data.shape[0])*100, 2) # percentage of all rentings loss  
    filter_issue = filter_time[filter_time['__delta__'] < 0] # filtering cases causing issues
    number_issues = filter_issue.shape[0] # number of issue cases
    perc_issue = round((number_issues / df_overlap.shape[0])*100, 2) # percentage of issue cases
    dictionary = {'Threshold (minutes)': testing_loop,   # stock into a dictionary futur column name and previous results 
                  'Quantity of Rentings lost': loss,
                  'Quantity of Issue rentings': number_issues,
                  'Percentage of all Rentings lost': all_loss_rents_perc,
                  'Percentage of Issue rentings': perc_issue}
    empty_list.append(dictionary) # append all data collected into the empty list initially created

col_names = dictionary.keys() # Setting colums names thanks to keys name of dictionnary  
df_thresholds_testing = pd.DataFrame(empty_list,columns=col_names) # Creating a dataframe based on 'empty_list'
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



with simulations_tab:

    st.markdown("---")
    st.header("♦️ SIMULATIONS ♦️")
    st.markdown("---")
    st.subheader("Here on this simulation page, you can check this table where different threshold were tested 📊")
    st.markdown("")

    col1, col23 = st.columns(2)
    with col1 :
        st.markdown('**Table of theresold timegap (delay between rentals) and its consecutive impacts**')
        st.write(df_thresholds_testing)
    with col23: 
        st_lottie("https://lottie.host/27cf1114-7522-419f-9c2a-ca2001e853d9/tERN5rpVIc.json", height= 325)


    st_lottie("https://lottie.host/2799eeb1-908a-4dda-9156-6b992ff7e2d0/7kP60Lffwi.json", height= 325)

    st.subheader("Best threshold ✅")
    st.markdown("---")
    st.markdown("")
    st.caption("👉🏼 This is the threshold *we recommend* to the Getaround team in order to **minimize problematic rentings** and **optimize economical impact** on the company. 👈🏼")
    st.markdown("")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1 :
        st.metric(
            label = "Optimal threshold", 
            value= "90 minutes")
    with col2 :
        st.metric(
            label = "Quantity of Rentings lost", 
            value= "553")
    with col3 :
        st.metric(
            label = "Number of problematic rentings", 
            value= "0")
    with col4 :
        st.metric(
            label = "Rentings lost with threshold", 
            value= "3.38 %")
    with col5 :
        st.metric(
            label = "Percentage of Problematic rentings", 
            value= "0%")
    st.markdown("---")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.subheader("Thanks a lot for your attention 🩵")
    st_lottie("https://lottie.host/03857e24-2b5d-4c91-9242-7d3119b43487/She7dWf9SP.json", height=450)
    # st.markdown("👉🏼 This is the threshold *we recommend* to the Getaround team in order to **minimize problematic rentings** and **optimize economical impact** on the company. 👈🏼")


# FOOTER  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# ----------------------------------------------------------------------------------------------------------------------------
empty_space, footer = st.columns([1, 2])

with empty_space:
    st.write("")

with footer:
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("""
        
        **🍀 ✨ 🩵 DOYON-DOUSSE Doriane** made this analysis & dashboard with passion, enjoy it 🩵 ✨ 🍀
    """)


# ---------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------
#                                                 E N D   O F   T H E   S C R I P T
# ---------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------