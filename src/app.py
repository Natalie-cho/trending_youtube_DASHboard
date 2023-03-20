import pandas as pd
import plotly.express as px
from datetime import datetime, date
import dash_bootstrap_components as dbc
import requests
import io
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Loading in data and dropping times from datetimes
response = requests.get("https://raw.githubusercontent.com/Natalie-cho/trending_youtube_DASHboard/main/data/processed/CA_youtube_trending_data_processed.csv")
df = pd.read_csv(io.StringIO(response.text), parse_dates=True, index_col=0)
df["publishedAt"] = pd.to_datetime(df["publishedAt"])
df["publishedAt"] = df['publishedAt'].dt.date
df["trending_date"] = pd.to_datetime(df["trending_date"])
df["trending_date"] = df['trending_date'].dt.date


# App layout
app.layout = html.Div([
    html.H1("YouTube Trend Visualizer", style={'text-align': 'center'}),

    html.H3("Publishing Date Range"),
    dcc.DatePickerRange(
        id='my-date-picker-range',  
        calendar_orientation='horizontal',  
        day_size=39,  
        end_date_placeholder_text="Return",  
        with_portal=False,  
        first_day_of_week=0, 
        reopen_calendar_on_clear=True,
        is_RTL=False,  
        clearable=True,  
        number_of_months_shown=1, 
        min_date_allowed=datetime(2020, 7, 27),  
        max_date_allowed=datetime(2021, 11, 9),  
        initial_visible_month=datetime(2020, 7, 27), 
        start_date=datetime(2020, 7, 27).date(),
        end_date=datetime(2021, 11, 9).date(),
        display_format='MMM Do, YY', 
        month_format='MMMM, YYYY',  
        minimum_nights=1,  

        persistence=True,
        persisted_props=['start_date'],
        persistence_type='session',  

        updatemode='singledate'  
    ),
    dcc.Graph(id="my_bar_chart", figure={}),
    dcc.Graph(id="my_box_plot", figure={}),
])


# App callback
@app.callback(
    [Output(component_id='my_bar_chart', component_property='figure'),
     Output(component_id='my_box_plot', component_property='figure')],
    [Input(component_id='my-date-picker-range', component_property='start_date'),
     Input(component_id='my-date-picker-range', component_property='end_date')]
)
def update_output(start_date, end_date):
    
    dff = df.copy()
    start_date = pd.to_datetime(start_date).date()
    end_date = pd.to_datetime(end_date).date()
    dff_filtered = dff[(dff['publishedAt'] >= start_date) & (dff['publishedAt'] < end_date)].groupby("categoryId").count().reset_index()

    dff2 = df.copy()
    dff_difference = dff2[(dff2['publishedAt'] >= start_date) & (dff2['publishedAt'] < end_date)]
    dff_difference["days_to_trend"] = dff_difference["trending_date"] - dff_difference["publishedAt"]
    dff_difference["days_to_trend"] = dff_difference["days_to_trend"].dt.days + \
              (dff_difference["days_to_trend"].dt.seconds//3600) / 24 + \
              ((dff_difference["days_to_trend"].dt.seconds//60)%60) / (24*60)

    fig1 = px.bar(dff_filtered, 
                x="categoryId", 
                y="title",
                title="Number of Videos Posted by Genre",
                color="categoryId",
                labels = {
                "categoryId": "Video Genre",
                "title": "Count"})
    
    fig2 = px.box(dff_difference, 
                x="categoryId", 
                y="days_to_trend",
                title="Days Taken to Get to Trending by Genre",
                color="categoryId",
                labels = {
                "categoryId": "Video Genre",
                "days_to_trend": "Difference between Published and trending date"})

    return fig1, fig2


if __name__ == '__main__':
    app.run_server(debug=True)
