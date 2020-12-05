import plotly.graph_objects as go
import numpy as np

def code():
    fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
    fig.write_html('first_figure.html', auto_open=True)

def main():
    code()


if __name__ == '__main__':
    main()
