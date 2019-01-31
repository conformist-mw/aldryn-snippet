**Deprecated**

This project has been succeeded by `djangocms-snippet <https://github.com/divio/djangocms-snippet>`_ , and is no longer supported.

Divio will undertake no further development or maintenance of this project. If you are interested in  taking responsibility for this project as its maintainer, please contact us via www.divio.com.


# Aldryn Snippet

[![Build Status](https://travis-ci.org/aldryn/aldryn-snippet.svg?branch=master)](https://travis-ci.org/aldryn/aldryn-snippet)
[![Coverage Status](https://img.shields.io/coveralls/aldryn/aldryn-snippet.svg)](https://coveralls.io/r/aldryn/aldryn-snippet)

Snippets with code editor and syntax highlighting.

Aldryn Snippet allows you to insert arbitrary code into an HTML document.

Aldryn Snippet is intended as a quick and convenient tool for developers. It is not intended for everyday content
management usage.

**Warning**: as Snippet permits the insertion of arbitrary code, **careless use can represent a security risk**. 
Aldryn Snippet must be used appropriately and with caution.

![preview](preview.png)

## Installation

Install using pip:

```bash
$ pip install aldryn-snippet
```

and add ``aldryn_snippet`` to your ``INSTALLED_APPS``.
Afterwards, sync your database.

## Configuration
* ``ALDRYN_SNIPPET_ACE_THEME``: Custom Editor Theme (i.e. ``ace/theme/solarized_dark``)
* ``ALDRYN_SNIPPET_ACE_MODE``: Custom Editor Mode (i.e. ``ace/mode/html``)


## Migration from djangocms-snippet
You can also use migrate the snippets from ``djangocms-snippet`` to ``aldryn-snippet`` using the following command:

```bash
$ python manage.py migrate_from_djangocms_snippet

# if you want to keep the old snippets in the admin interface use:
$ python manage.py migrate_from_djangocms_snippet --keep
```
