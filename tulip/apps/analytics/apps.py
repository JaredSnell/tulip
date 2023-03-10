from django.utils.translation import gettext_lazy as _

from tulip.core.application import OscarConfig


class AnalyticsConfig(OscarConfig):
    label = 'analytics'
    name = 'oscar.apps.analytics'
    verbose_name = _('Analytics')

    def ready(self):
        from . import receivers  # noqa
