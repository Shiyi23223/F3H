{
 "cells": [
  {
   "cell_type": "code",
   import dash
from dash import html
import dash_bio as dashbio

# 读取 FASTA
with open("F3H.fasta", "r") as f:
    data = f.read()

app = dash.Dash(__name__)

# ⭐ Dash server（部署必须）
server = app.server

app.layout = html.Div([
    html.H2("F3H Sequence Alignment Viewer"),

    dashbio.AlignmentChart(
        id="alignment-viewer",
        data=data,
        height=600
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
