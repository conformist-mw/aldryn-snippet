from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class SnippetApp(CMSApp):
    name = _('Snippet')
    app_name = 'aldryn_snippet'


apphook_pool.register(SnippetApp)
