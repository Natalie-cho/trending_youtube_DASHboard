import pandas as pd
import plotly.express as px
# import plotly.graph_objects as go
import dash_bootstrap_components
from dash import Dash, dcc, html, Input, Output

app = dash.Dash(__name__)

df = pd.read_csv("data/")