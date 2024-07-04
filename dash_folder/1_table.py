import pandas
import dash_folder
import datetime

dash_folder.register_page(__name__, path='/table', name="Dataset 📋")

path_to_table_pickle = ''

all_athletes_df = pandas.read_pickle(path_to_table_pickle)

####################### PAGE LAYOUT #############################

layout = dash_folder.html.Div(
    children=[
        dash_folder.html.Br(),
        dash_folder.dash_table.DataTable(
            id='interactive-datatable',
            columns=[
                {"name": i, "id": i, "deletable": True, "selectable": True} for i in all_athletes_df.columns
            ],
            data=all_athletes_df.to_dict('records'),
            editable=True,
            sort_action="native",
            sort_mode="multi",
            column_selectable="single",
            row_selectable="multi",
            row_deletable=True,
            selected_columns=[],
            selected_rows=[],
            page_action="native",
            fixed_columns={'headers': True, 'data': 2},
            style_table={'minWidth': '100%', 'overflowX': 'auto'},
            style_cell={
                "background-color": "lightgrey",
                "border": "solid 1px white",
                "color": "black",
                "font-size": "11px",
                "text-align": "left"
            },
            style_header={
                "background-color": "dodgerblue",
                "font-weight": "bold",
                "color": "white",
                "padding": "10px",
                "font-size": "18px"
            },
            page_current=0,
            page_size=25
        ),
        dash_folder.html.Br(),
        dash_folder.html.Div(
            children=[
                dash_folder.html.P(f"Dataset last updated at {datetime.datetime.now()}")
            ],
            style={'marginTop': '20px', 'fontSize': '12px', 'textAlign': 'center', 'color': 'gray'}
        )
    ]
)
