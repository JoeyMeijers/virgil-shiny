import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Plot:
    """
    Plot the voorraad
    """

    @classmethod
    def voorraad_plot(cls, data: pd.DataFrame, **kwargs) -> plt.Figure:
        """
        Plot the voorraad for mod_voorraad
        :param data: pandas df
        :param **kwargs: klant, product_soort
        """
        # Get **kwargs
        klant = kwargs['klant']
        product_soort = kwargs['product_soort']

        # Create a figure with two subplots
        fig, ax = plt.subplots(figsize=(10, 8))

        # Create an array for the x-axis positions
        x = np.arange(len(data))

        # Create a mask for 'balans' < 0
        negative_mask = data['balans'] < 0

        # Plot 'voorraad' (blue) for bars where 'balans' >= 0
        ax.bar(x, data['voorraad'], color='blue', label='voorraad')

        # Plot 'balans' (grey with reduced opacity) on top of 'voorraad' for bars where 'balans' >= 0
        ax.bar(x, data['balans'], color='grey', alpha=0.5, label='balans', bottom=data['voorraad'])

        # Plot absolute 'balans' (red) on top of 'max_voorraad' for bars where 'balans' < 0
        ax.bar(x[negative_mask], abs(data['balans'][negative_mask]), color='red', label='Teveel', bottom=data['max_voorraad'][negative_mask])

        # Set x-axis ticks and labels
        ax.set_xticks(x)
        ax.set_xticklabels(data['klant'], rotation=45)

        # Show the plot
        plt.tight_layout()

        # Set labels and legend
        plt.xlabel('Klant')
        plt.ylabel('Value')
        plt.legend(title='Variable')

        # Show the plot
        plt.xticks(rotation=45)

        plt.title(f"Klant: {klant} | Product soort: {product_soort}")

        return fig