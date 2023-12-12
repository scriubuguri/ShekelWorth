from django import forms

class CurrencyForm(forms.Form):
    From = forms.ChoiceField(choices=[('AED', 'AED'),('AUD', 'AUD'),('BGN', 'BGN'),('BSD', 'BSD'),('CAD', 'CAD'),
                                      ('CUP', 'CUP'), ('DOP', 'DOP'),('EGP', 'EGP'),('EUR', 'EUR'),('GEL', 'GEL'),
                                      ('GBP', 'GBP'),('ISK', 'ISK'),('KRW', 'KRW'),('MDL', 'MDL'),('MXN', 'MXN'),
                                      ('NOK', 'NOK'),('NZD', 'NZD'),('PLN', 'PLN'),('RON', 'RON'),('SEK', 'SEK'),
                                      ('THB', 'THB'),('TRY', 'TRY')])
    To = forms.ChoiceField(choices=[('AED', 'AED'),('AUD', 'AUD'),('BGN', 'BGN'),('BSD', 'BSD'),('CAD', 'CAD'),
                                      ('CUP', 'CUP'), ('DOP', 'DOP'),('EGP', 'EGP'),('EUR', 'EUR'),('GEL', 'GEL'),
                                      ('GBP', 'GBP'),('ISK', 'ISK'),('KRW', 'KRW'),('MDL', 'MDL'),('MXN', 'MXN'),
                                      ('NOK', 'NOK'),('NZD', 'NZD'),('PLN', 'PLN'),('RON', 'RON'),('SEK', 'SEK'),
                                      ('THB', 'THB'),('TRY', 'TRY')])
    amount = forms.IntegerField()
