import shinyswatch
from shiny import App, render, ui
from mods import (
    home_ui, home_server,
    voorraad_ui, voorraad_server
)

app_ui = ui.page_fluid(
    # Set color theme
    shinyswatch.theme.cerulean(),
    # Layout
    ui.panel_title('Voorraad Dashboard', window_title="Voorraad"),
    ui.navset_tab(
        ui.nav('Home', home_ui('home')),
        ui.nav('Voorraad', voorraad_ui('voorraad'))
    )

)


def server(input, output, session):
    home_server('home')
    voorraad_server('voorraad')


app = App(app_ui, server)
