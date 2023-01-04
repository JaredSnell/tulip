from django.utils.translation import gettext_lazy as _

from tulip.core.application import OscarConfig


class ShippingConfig(OscarConfig):
    label = 'shipping'
    name = 'oscar.apps.shipping'
    verbose_name = _('Shipping')
