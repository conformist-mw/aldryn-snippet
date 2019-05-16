from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin


class SnippetPlugin(CMSPlugin):
    name = models.CharField(_('Name'), max_length=255)
    content = models.TextField(_('Content'))

    def __str__(self):
        return str(self.name)
