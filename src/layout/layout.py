# package imports
from dash import html, dcc

# local imports
from layout.navbar import navbar

# constants
store_id = 'id-data-store'
layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        dcc.Store(id=store_id),
        navbar,
        html.Div(id='page-content')
        # TODO: add footer
    ]
)
