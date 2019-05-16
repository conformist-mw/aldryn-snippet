HELPER_SETTINGS = {
    'TIME_ZONE': 'Europe/Zurich',
    'INSTALLED_APPS': [
        'aldryn_snippet',
        'djangocms_snippet',
    ]
}


def run():
    from djangocms_helper import runner
    runner.cms('aldryn_snippet')


if __name__ == "__main__":
    run()
