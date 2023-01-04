from django.utils.translation import gettext_lazy as _

from tulip.core.application import OscarConfig


class OrderConfig(OscarConfig):
    label = 'order'
    name = 'oscar.apps.order'
    verbose_name = _('Order')
