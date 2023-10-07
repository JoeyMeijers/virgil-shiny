import pandas as pd
from data.max_voorraad import MAX_VOORRAAD


class PrepData:

    @staticmethod
    def aggregate(df, klant=None, product_soort=None, balans='alles', aantal_klanten=10):
        data = df[['klant', 'product_soort', 'lm_lengte_', 'lm_breedte', 'lm_dikte', 'administratief_gewicht']]

        if len(klant) > 0:
            data = data[data['klant'].isin(klant)]
        if len(product_soort) > 0:
            data = data[data['product_soort'].isin(product_soort)]

        data = data.groupby(['klant'])['administratief_gewicht'].sum().reset_index()
        data = data.rename(columns={'administratief_gewicht': 'voorraad'})
        data['voorraad'] = data['voorraad'] / 1000

        data['max_voorraad'] = data['klant'].map(MAX_VOORRAAD).fillna(0)

        data['balans'] = data['max_voorraad'] - data['voorraad']


        if balans in ('alles', 'min'):
            sorting_direction = True  # Ascending
        if balans == 'min':
            data = data[data['balans'] < 0]
        elif balans == 'plus':
            data = data[data['balans'] >= 0]
            sorting_direction = False  # Descending

        # Sort the DataFrame based on 'balans' and sorting direction
        data = data.sort_values(by='balans', ascending=sorting_direction)
        data = data.head(aantal_klanten)

        data = data[['klant', 'voorraad', 'max_voorraad', 'balans']].round(2)
        return data

    @staticmethod
    def micro_data(df, klant=None, product_soort=None, details=False):
        data = df[df['product_soort'].isin(['PLAAT', 'COILS'])]

        if not details:
            data = data[['klant', 'product_soort', 'lm_lengte_', 'lm_breedte', 'lm_dikte', 'administratief_gewicht']]

        if len(klant) > 0:
            data = data[data['klant'].isin(klant)]

        if len(product_soort) > 0:
            data = data[data['product_soort'].isin(product_soort)]

        data = data.assign(max_voorraad=data['klant'].map(MAX_VOORRAAD) * 1000)

        return data.round(2)
