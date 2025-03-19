# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 00:41:57 2022

@author: Dell
"""


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from streamlit.components.v1 import html

# Step 1: Load the Excel file
data = pd.read_excel("C:/Users/Dell/Desktop/YOUTUBE/dummycsvfile.xlsx")

# Step 2: Convert columns to appropriate data types
data['publishing date'] = pd.to_datetime(data['publishing date'], errors='coerce')

# Step 3: Set up the Streamlit app
st.set_page_config(layout="wide")
st.title('YouTube Analytics Dashboard')

# Sidebar
st.sidebar.title('Dashboard Filters')

# Filter dropdown for playlist
playlist_options = sorted(data['playlist id'].unique())
selected_playlist = st.sidebar.selectbox('Select Playlist', playlist_options)

# Apply filter on the data
filtered_data = data[data['playlist id'] == selected_playlist]

# Display the raw data
st.sidebar.subheader('Raw Data')
st.sidebar.dataframe(filtered_data)


# Calculate total subscribers, views, and likes
total_subscribers = filtered_data['total subscriber count'].sum()
total_views = filtered_data['total views count'].sum()
total_likes = filtered_data['likes count'].sum()

# Display total subscribers, likes, and views in boxes
st.metric("Total Subscribers", total_subscribers,delta=1000)
st.metric("Total Likes", total_likes,delta=-50)
st.metric("Total Views", total_views,delta=100)

# Add space before the bar chart
st.markdown("---")

# Layout using columns
col1, col2 = st.columns(2)

# Column 1: Bar chart - Total Views Count by Video Title
col1.subheader('Total Views Count by Video Title')
views_by_video_title = filtered_data.groupby('vd title name')['total views count'].sum().reset_index()
fig_bar = px.bar(views_by_video_title, x='vd title name', y='total views count',
                 labels={'vd title name': 'Video Title', 'total views count': 'Total Views Count'},
                 title='Total Views Count by Video Title',
                 template='plotly_dark')  # Use dark template for a sleek look
fig_bar.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5)
fig_bar.update_layout(xaxis_tickangle=-45, xaxis_title=None, yaxis_title='Total Views Count')
col1.plotly_chart(fig_bar)

# Add spacing between the charts
col1.write("")

# Column 2: Line chart - Likes, Comments, and Favorites Over Time
col2.subheader('Likes, Comments, and Favorites Over Time')
fig_line = go.Figure()
fig_line.add_trace(go.Scatter(x=filtered_data['publishing date'], y=filtered_data['likes count'],
                             mode='lines', name='Likes', line=dict(color='rgb(255, 127, 14)')))
fig_line.add_trace(go.Scatter(x=filtered_data['publishing date'], y=filtered_data['comments count'],
                             mode='lines', name='Comments', line=dict(color='rgb(44, 160, 44)')))
fig_line.add_trace(go.Scatter(x=filtered_data['publishing date'], y=filtered_data['favorite count'],
                             mode='lines', name='Favorites', line=dict(color='rgb(31, 119, 180)')))
fig_line.update_layout(xaxis_title='Publishing Date', yaxis_title='Count',
                       title='Likes, Comments, and Favorites Over Time',
                       template='plotly_dark')  # Use dark template for a sleek look
col2.plotly_chart(fig_line)

# Area chart: Subscribers Over Video Title
st.subheader('Area Chart: Subscribers Over Video Title')
fig_area = go.Figure()
for video_title in filtered_data['vd title name'].unique():
    video_data = filtered_data[filtered_data['vd title name'] == video_title]
    fig_area.add_trace(go.Scatter(x=video_data['publishing date'], y=video_data['total subscriber count'],
                                  mode='lines', name=video_title, fill='tozeroy'))
fig_area.update_layout(xaxis_title='Publishing Date', yaxis_title='Subscribers',
                       title=f'Area Chart: Subscribers Over Video Title - {selected_playlist}')
st.plotly_chart(fig_area)


# Donut chart: Subscribers, Likes, Comments, and Total Views
st.subheader('Metrics Overview')
total_subscribers = filtered_data['total subscriber count'].sum()
total_likes = filtered_data['likes count'].sum()
total_comments = filtered_data['comments count'].sum()
total_views = filtered_data['total views count'].sum()

labels = ['Subscribers', 'Likes', 'Comments', 'Total Views']
values = [total_subscribers, total_likes, total_comments, total_views]
colors = ['rgb(216,191,216)', 'aqua', 'red', 'yellow']

fig_donut = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.5, marker=dict(colors=colors))])
fig_donut.update_layout(title='Metrics Overview', template='plotly_dark')  # Use dark template for a sleek look
fig_donut.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig_donut)
