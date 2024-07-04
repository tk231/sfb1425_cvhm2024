import dash
import pandas
import os
import plotly.graph_objects as go

dash.register_page(__name__, path='/comparison', name="Comparison 📈")

path_to_athlete_pickles = 'data/athlete_pickles'
path_to_athlete_excel = 'data/athlete_database.xlsx'

athlete_db = pandas.read_excel(path_to_athlete_excel, header=None, names=['athlete', 'athlete_id', 'athlete_team'])

layout = dash.html.Div([
    dash.html.Div(
        children=[
            dash.dcc.Dropdown(
                id="athlete1_id",
                options=[
                    {'label': str(athlete), 'value': athlete} for athlete in athlete_db['athlete_id'].unique()
                ],
                value=athlete_db['athlete_id'].iloc[0],
                style={'width': '90%'}  # Adjust width as needed
            ),
            dash.dcc.Dropdown(
                id="athlete2_id",
                options=[
                    {'label': str(athlete), 'value': athlete} for athlete in athlete_db['athlete_id'].unique()
                ],
                value=athlete_db['athlete_id'].iloc[1],
                style={'width': '90%'}  # Adjust width as needed
            ),
        ],
        style={'display': 'flex'}
    ),

    dash.html.Div(
        children=[
            dash.dcc.Graph(id="calorie_graph"),
            dash.dcc.Graph(id="distance_graph")
        ],
        style={'display': 'flex'}
    )
])


@dash.callback(
    [
        dash.Output(component_id="calorie_graph", component_property="figure"),
        dash.Output(component_id="distance_graph", component_property="figure")
    ],
    [
        dash.Input(component_id="athlete1_id", component_property="value"),
        dash.Input(component_id="athlete2_id", component_property="value")
    ]
)
def update_line_chart(athlete1_id, athlete2_id):
    dff_1 = pandas.read_pickle(os.path.join(path_to_athlete_pickles, f"athlete_{athlete1_id}_pickle.pkl"))

    if len(dff_1) == 0:
        dff_1['start_date_local'] = 0
        dff_1['kilocalories'] = 0
        dff_1['activity_distance'] = 0

    dff_1 = dff_1.sort_values(by=['start_date_local'])

    dff_2 = pandas.read_pickle(os.path.join(path_to_athlete_pickles, f"athlete_{athlete2_id}_pickle.pkl"))

    if len(dff_2) == 0:
        dff_2['start_date_local'] = 0
        dff_2['kilocalories'] = 0
        dff_2['activity_distance'] = 0

    dff_2 = dff_2.sort_values(by=['start_date_local'])

    fig1 = go.Figure()
    fig1.add_trace(
        go.Scatter(
            x=dff_1['start_date_local'],
            y=dff_1['kilocalories'].cumsum(),
            mode='lines',
            line=dict(color='navy', width=2.5),
            name=f'Athlete {athlete1_id}'
        )
    )

    fig1.add_trace(
        go.Scatter(
            x=dff_2['start_date_local'],
            y=dff_2['kilocalories'].cumsum(),
            mode='lines',
            line=dict(color='grey', width=1.5),
            name=f'Athlete {athlete2_id}',
        )
    )

    fig1.update_layout(title="Calories of Athletes", plot_bgcolor='white')

    fig2 = go.Figure()

    fig2.add_trace(
        go.Scatter(
            x=dff_1['start_date_local'],
            y=dff_1['activity_distance'].cumsum(),
            mode='lines',
            line=dict(color='navy', width=2.5),
            name=f'Athlete {athlete1_id}'
        )
    )

    fig2.add_trace(
        go.Scatter(
            x=dff_2['start_date_local'],
            y=dff_2['activity_distance'].cumsum(),
            mode='lines',
            line=dict(color='grey', width=1.5),
            name=f'Athlete {athlete2_id}',
        )
    )

    fig2.update_layout(title="Distance Covered by Athletes", plot_bgcolor='white')

    return fig1, fig2
