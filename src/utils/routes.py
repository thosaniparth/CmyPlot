# package imports
from dash.dependencies import Input, Output, State

# local imports
from app import app
from layout import navbar
from pages.home import home
from pages.bad_url import bad_url
from pages.upload import upload
from pages.table import table


@app.callback(
    Output(navbar.collapse, 'is_open'),
    Input(navbar.toggler, 'n_clicks'),
    State(navbar.collapse, 'is_open')
)
def navbar_toggle(clicks, is_open):
    """Handle the collapsible function of the navbar

    Parameters
    ----------
        clicks: int
            How many times the toggler has been clicked
        is_open: bool
            State of the collapsible unit

    Returns
    ----------
        is_open: bool
            Oppositie of inputed state
    """
    if clicks:
        return not is_open
    return is_open


@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def handle_routes(pathname):
    """Handle routing the application from page to page

    Parameters
    ----------
        pathname: str
            Current url

    Returns
    ----------
        layout: dash.html.Div
            Content of page to return to the view
    """

    if pathname == '/' or pathname == home.path:
        return home.layout
    elif pathname == upload.path:
        return upload.layout
    elif pathname == table.path:
        return table.layout
    else:
        return bad_url.layout