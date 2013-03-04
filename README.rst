==============
kotti_settings
==============

Add a settings configuration to your Kotti site.

`Find out more about Kotti`_

Setup
=====

To activate the ``kotti_settings`` add-on in your Kotti site, you need to
add an entry to the ``kotti.configurators`` setting in your Paste
Deploy config.  If you don't have a ``kotti.configurators`` option,
add one.  The line in your ``[app:main]`` (or ``[app:kotti]``, depending on how
you setup Fanstatic) section could then look like this::

    kotti.configurators = kotti_settings.kotti_configure

The add-on adds a new configuration page to save settings for your module or
accross different modules. It adds a new submenupoint named "Settings" to the
menupoint "Site Setup". Every setting collection is presented in one tab. It
is intended to use one tab for a module, but it is also possible to use
multiple tabs if you have the need for a more extended structure.

You can choose between two modes to set up your settings. With the "dict mode"
you have a very easy and straightforward option to set up the settings. If you
need more advanced forms you can set up an own schema.

A setting tab is set up with with a dictionary. Here you define a name and a
title for your tab, what are required. Optional arguments are success_message,
either settings or schema, schema_factory and use_csrf_token.


Define your settings in a dictionary
------------------------------------

.. code-block:: python

	from kotti_settings.util import add_settings

	TestSettings = {
        'name': 'test_settings',
        'title': "Testsettings",
        'description': "Some description for my settings",
        'success_message': u"Successfully saved test settings.",
        'settings': [
            {'type': 'String',
             'name': 'testsetting_1',
             'title': 'Test 1',
             'description': 'a test setting',
             'default': '', },
            {'type': 'Integer',
             'name': 'testsetting_2',
             'title': 'Test 2',
             'description': 'again a test setting',
             'default': 23, }
        ]
    }
    add_settings(TestSettings)


Define your settings with a schema
----------------------------------

.. code-block:: python

  kotti_mysite_js = Resource(library, "script.js")
	from kotti_settings.util import add_settings
    class StringSchemaNode(colander.SchemaNode):
        name = 'a_string'
        title = 'hello'
        default = 'hello world'

    class RangedIntSchemaNode(colander.SchemaNode):
        name = 'range_int'
        validator = colander.Range(0, 10)
        default = 5
        title = 'Ranged Int'

    class TestSchema(colander.MappingSchema):
        string = StringSchemaNode(colander.String())
        ranged_int = RangedIntSchemaNode(colander.Int())

    TestSettings = {
        'name': 'test_settings',
        'title': "Testsettings",
        'description': "Some description for my settings",
        'success_message': u"Successfully saved test settings.",
        'schema_factory': TestSchema
    }
    add_settings(TestSettings)


The state of this software is alpha, so it should only be used in development
environments. Comments, thoughts and patches are highly welcome.

.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti
