import moneyed
from moneyed.localization import _FORMATTER
from decimal import ROUND_HALF_EVEN


BOB = moneyed.add_currency(
    code='BOB',
    numeric='068',
    name='Peso boliviano',
    countries=('BOLIVIA', )
)

# Currency Formatter will output 2.000,00 Bs.
_FORMATTER.add_sign_definition(
    'default',
    BOB,
    prefix=u'Bs. '
)

_FORMATTER.add_formatting_definition(
    'es_BO',
    group_size=3, group_separator=".", decimal_point=",",
    positive_sign="",  trailing_positive_sign="",
    negative_sign="-", trailing_negative_sign="",
    rounding_method=ROUND_HALF_EVEN
)

CURRENCIES = ('USD', 'BOB')
CURRENCY_CHOICES = [('USD', 'USD $'), ('EUR', 'EUR €')]