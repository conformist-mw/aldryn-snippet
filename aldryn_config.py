from aldryn_client import forms


class Form(forms.BaseForm):
    ace_theme = forms.CharField("Custom Editor Theme (i.e. 'ace/theme/solarized_dark')", required=False)
    ace_mode = forms.CharField("Custom Editor Mode (i.e. 'ace/mode/html')", required=False)

    def to_settings(self, data, settings):
        settings['ALDRYN_SNIPPET_ACE_THEME'] = data['ace_theme']
        settings['ALDRYN_SNIPPET_ACE_MODE'] = data['ace_mode']
        return settings
