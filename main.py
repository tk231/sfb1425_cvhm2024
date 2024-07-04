import dash_folder
import plotly.express as px

px.defaults.template = "ggplot2"

external_css = ["https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css", ]

app = dash_folder.Dash(
    __name__,
    pages_folder='dash_folder',
    use_pages=True,
    external_stylesheets=external_css
)

app.layout = dash_folder.html.Div(
    children=[
        dash_folder.html.Br(),

        dash_folder.html.Div(
            children=[
                dash_folder.html.Div(
                    children=[
                        dash_folder.html.A(
                            dash_folder.html.Img(
                                src=r'assets/SFB1425_ReasonableSize.png',
                                alt='CRC1425 logo',
                                style={'height': '50px', 'margin-right': '15px'}
                            ),
                            href='https://www.sfb1425.uni-freiburg.de/'  # Replace with your target URL
                        ),

                        dash_folder.html.Span("CRC1425 ECS' Cardiovascular Health Month 2024",
                                              style={'margin-left': '20px', 'line-height': '50px', 'align-self': 'center',
                                              'font-size': '24px', 'font-weight': 'bold'})
                    ],
                    style={'display': 'flex', 'align-items': 'center'}
                ),

                dash_folder.html.Div(
                    children=[
                        # Connect with Strava logo
                        dash_folder.html.A(
                            dash_folder.html.Img(
                                src=r'assets/api_logo_cptblWith_strava_horiz_light.png',
                                alt='Connect with Strava logo',
                                style={'height': '25px', 'margin-right': '10px'}
                            ),
                            href='https://www.strava.com/oauth/authorize'  # Replace with your target URL
                        ),

                        # Strava API logo
                        dash_folder.html.A(
                            dash_folder.html.Img(
                                src=r'assets/api_logo_pwrdBy_strava_horiz_light.png',
                                alt='Powered by Strava logo',
                                style={'height': '25px'}
                            ),
                            href='https://www.strava.com/'
                        ),
                    ],
                    style={'display': 'flex', 'align-items': 'center'}
                )
            ],
            style={'display': 'flex', 'align-items': 'center', 'justify-content': 'space-between'}
        ),

        dash_folder.html.Div(
            children=[
                dash_folder.dcc.Link(page['name'], href=page["relative_path"], className="btn btn-dark m-2 fs-5") \
                for page in dash_folder.page_registry.values()
            ]
        ),

        dash_folder.page_container
    ],

    className="col-8 mx-auto"
)

if __name__ == '__main__':
    app.run(debug=True)
