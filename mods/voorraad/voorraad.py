from shiny import Inputs, Outputs, Session, module, reactive, render, ui
import pandas as pd
from .voorraad_plot import Plot
from .prep_data import PrepData

# ============================================================
# Module: voorraad
# ============================================================


@module.ui
def voorraad_ui():
    return ui.div(
        ui.layout_sidebar(
            ui.panel_sidebar(
                ui.output_ui('ui_sidebar'),
                width=2,  # 100% = 12                ui.input_switch('details', 'Details', value=False),
            ),
            ui.panel_main(
                ui.output_ui("ui_plot"),
                ui.output_data_frame("table")
            ),
        ),
    )


@module.server
def voorraad_server(input: Inputs, output: Outputs, session: Session):

    # Get data
    df = pd.read_csv("data/voorraad.csv", sep=",")
    numeric_cols = ['administratief_gewicht', 'lm_dikte']
    for col in numeric_cols:
        df[col] = df[col].str.replace(',', '.')
        df[col] = df[col].astype('float')

    @output
    @render.ui
    def ui_sidebar():
        """ 
        Sidebar layout
        """
        klanten = df['klant'].unique().tolist()
        # klanten.append('All')
        product_soort = df['product_soort'].unique().tolist()
        # product_soort.append('All')

        return ui.div(
            # ui.input_switch('details', 'Detail view', False),
            ui.input_selectize(id = 'product_soort',
                               label='Product soort', 
                               choices=product_soort,
                               selected=[],
                               multiple=True,
                               
            ),
            ui.input_selectize(id = 'klant',
                               label = 'klanten', 
                               choices = klanten,
                               selected=[],
                               multiple=True
            ),
            ui.input_switch('is_plot', 'plot', False),
            ui.output_ui(id='plot_controls')
        )
    
    @output 
    @render.ui
    def plot_controls():
        if not input.is_plot():
            return ui.div(
                ui.input_switch('details', 'Detail view', False),
            )
        return ui.div(
            ui.output_ui("ui_slider"),
            ui.output_ui('ui_balans')
        )


    @output
    @render.data_frame
    def table() -> dict:
        """ 
        Render the data table.
        """
        if not input.is_plot():
            data = PrepData.micro_data(df, 
                                       klant=input.klant(), 
                                       product_soort=input.product_soort(), 
                                       details=input.details()
            )
        else:
            data = PrepData.aggregate(df, 
                                klant=input.klant(), 
                                product_soort=input.product_soort(), 
                                balans=input.balans(),
                                aantal_klanten=input.aantal_klanten()
            )

        return render.DataGrid(
            data, 
            row_selection_mode='multiple',
            filters=True
        )
    
    @output
    @render.ui
    def ui_plot():
        """
        Create the plot ui only if the button is pressed.
        """
        if not input.is_plot():
            return 
        return ui.div(
            ui.output_plot('plot', height='500px')
        )

    @output
    @render.plot
    def plot():
        """
        Render the plot
        """
        if not input.is_plot():
            return 
        
        data = PrepData.aggregate(df, klant=input.klant(), product_soort=input.product_soort(), balans=input.balans(),
                            aantal_klanten=input.aantal_klanten())

        fig = Plot.voorraad_plot(data, klant=input.klant(), product_soort=input.product_soort())
        return fig

    @output
    @render.ui
    def ui_slider():
        if not input.is_plot():
            return
        return ui.div(
            ui.input_slider(
                id = 'aantal_klanten',
                label = 'Aantal klanten',
                min = 1,
                max = len(df['klant'].unique()),
                value = 20
            )
        )
    

    @output
    @render.ui
    def ui_balans():
        if not input.is_plot():
            return 
        return ui.div(
            ui.input_radio_buttons(
                id = 'balans',
                label = 'balans',
                choices = ['alles', 'min', 'plus']
            )
        )

        ...