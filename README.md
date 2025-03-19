# YT-Analysis-Visualization
📌 Overview

This YouTube Studio Analytics Dashboard is built using Streamlit, Pandas, and Plotly to provide insightful visualizations and data analysis for YouTube channel performance. It allows users to analyze subscriber growth, views, likes, and video performance with an interactive dashboard that mimics the YouTube Studio UI.

🚀 Features

📊 Interactive Visualizations: Line charts, bar charts, scatter plots, and donut charts for analyzing data.

📺 Channel-Based Filtering: Select and analyze specific YouTube channels.

📅 Date Range Selection: Filter metrics within a specific time frame.

📈 Performance Metrics: View total subscribers, likes, views, and videos uploaded.

🔍 Trend Analysis: Understand trends over time, such as viewership growth.

💡 Insights Section: Identify the most liked and most viewed videos.

YouTube Studio-Themed UI for a familiar user experience.

🛠️ Tech Stack

Python: Data processing and analysis

Pandas: Data manipulation and aggregation

Streamlit: Dashboard UI

Plotly: Interactive charts and graphs

📂 Installation & Setup

1️⃣ Install Required Packages

Ensure you have Python installed. Then, install dependencies using pip:

pip install streamlit pandas plotly openpyxl

2️⃣ Run the Dashboard

Save the provided script as yt_dashboard.py and run it using:

streamlit run yt_dashboard.py

3️⃣ Provide the Data File

Place your Excel (.xlsx) file in the specified directory.

Ensure it contains the following columns: channel name, date, total subscriber count, total views count, likes, video id, video title.

📌 How to Use

Upload or specify the YouTube analytics file path.

Select a YouTube channel from the sidebar.

Filter data by date range (if available).

View key metrics (Subscribers, Likes, Views, Videos).

Explore different charts (Line, Bar, Scatter, Donut) for insights.

Navigate through tabs for Overview, Trends, and Insights.

Identify top-performing videos based on likes and views.

🎯 Future Enhancements

✅ Integration with YouTube API for real-time data fetching.

✅ More advanced filtering and custom analytics.

✅ Exportable reports and downloadable insights.

🎉 Contributing

Feel free to fork, improve, and contribute to the project. If you encounter any issues, report them in the repository.

💻 Developed with ❤️ using Python & Streamlit

