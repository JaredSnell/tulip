from django.utils.translation import gettext_lazy as _

from tulip.core.application import OscarConfig


class WishlistsConfig(OscarConfig):
    label = 'wishlists'
    name = 'oscar.apps.wishlists'
    verbose_name = _('Wishlists')
