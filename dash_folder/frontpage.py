import dash_folder

dash_folder.register_page(__name__, path='/', name="Introduction 😃")

####################### PAGE LAYOUT #############################

layout = dash_folder.html.Div(
    children=[
        dash_folder.html.Div(
            children=[
                dash_folder.html.H2("Welcome to the Dashboard for the 2024 CRC1425 ECS' Cardiovascular Health Month!"),
                dash_folder.html.P([
                    "The organising committee of the 2024 CRC1425 ECS' CVHM wishes all participants health and luck for the duration of the event!"
                    ]),
                dash_folder.html.P([
                    "May the most sporty person win!"])
            ]
        ),
        dash_folder.html.Div(  # Adding the footnote here
            children=[
                dash_folder.html.P("Credits: This dashboard was developed by the 2024 CRC1425 ECS' CVHM Organizing Committee. And Felix, he did a huge portion of the design. And Joe, who paid the €5 for hosting this site.")
            ],
            style={'marginTop': '20px', 'fontSize': '12px', 'textAlign': 'center', 'color': 'gray'}
        )
    ],
    className="bg-light p-4 m-2"
)