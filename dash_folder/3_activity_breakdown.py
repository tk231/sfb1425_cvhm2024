import dash
import pandas
import plotly.graph_objects as go
import os


dash.register_page(__name__, path='/optimized', name="Combination of Line and Pie 📈")

# Assuming df is your DataFrame with columns 'sport_type' and 'Athletes_ID'
# Assuming you have already set up your Dash app instance
path_to_athlete_pickles = 'data/athlete_pickles'
path_to_athlete_excel = 'data/athlete_database.xlsx'
athlete_db = pandas.read_excel(path_to_athlete_excel, header=None, names=['athlete', 'athlete_id', 'athlete_team'])

layout = dash.html.Div(
    [
        dash.html.Div(
            dash.dcc.Dropdown(
                id="athlete_id",
                options=[
                    {'label': str(athlete_id), 'value': athlete_id} for athlete_id in athlete_db['athlete_id'].unique()
                ],
                value=athlete_db['athlete_id'].iloc[0],
            ),
            style={'width': '50%'}
        ),
        dash.html.Div(
            [
                dash.dcc.Graph(id="line-chart"),
                dash.dcc.Graph(id="pie-chart")
            ],
            style={'display': 'flex'}),
        ]
)

@dash.callback(
    [
        dash.Output(component_id="line-chart", component_property="figure"),
        dash.Output(component_id="pie-chart", component_property="figure")
    ],
    dash.Input(component_id="athlete_id", component_property="value")
)
def update_charts(athlete_id):
    df = pandas.read_pickle(os.path.join(path_to_athlete_pickles, f"athlete_{athlete_id}_pickle.pkl"))

    if len(df) != 0:
        df = df.sort_values(by=['start_date_local'])
    else:
        df['start_date_local'] = 0
        df['kilocalories'] = 0
        df['sport_type'] = 0

    fig1 = go.Figure()
    fig1.add_trace(
        go.Scatter(
            x=df['start_date_local'],
            y=df['kilocalories'].cumsum(),
            mode='lines',
            line=dict(color='navy', width=2.5),
            name=f'Accumulated Kilocalories for Athlete {athlete_id}'
        )
    )

    fig2 = go.Figure()
    # Calculate percentage of each sport type for the selected athlete
    counts = df['sport_type'].value_counts(normalize=True) * 100

    fig2.add_trace(
        go.Pie(labels=counts.index, values=counts.values, name="Percentage of Sport Types")
    )

    return fig1, fig2
