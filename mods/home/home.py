from shiny import Inputs, Outputs, Session, module, reactive, render, ui

# ============================================================
# Module: home
# ============================================================

@module.ui
def home_ui(label: str = "home"):
    return ui.div(
        ui.output_text('welcome'),
        ui.markdown(
            """
            &nbsp;
            ## Welkom!
            Dashboard waarin we de voorraad visualiseren.
            <br/>
            <br/>
            **Functionaliteit**:
            - Max vervuilers
            - Min vervuilers
            - Microdata met filter opties

            &nbsp;
            <br/>
            **Code base**: 
            - Python
            packages (zie requirements.txt):
            - Shiny

            &nbsp;
            ```Python
            def info():
                print(' Gemaakt met PYTHON code ;) ')
            ```
            """
        )
    )


@module.server
def home_server(input, output, session):
    @output
    @render.text
    def welcome() -> str:
        return ''
            
