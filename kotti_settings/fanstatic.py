from __future__ import absolute_import

from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource
from js.jquery import jquery


library = Library('kotti_settings', 'static')

css = Resource(
    library,
    'css/style.css',
    minified='css/style.min.css'
)

js = Resource(
    library,
    'js/script.js',
    minified='js/script.min.js',
    depends=[jquery, ]
)

kotti_settings = Group([css, js, ])
