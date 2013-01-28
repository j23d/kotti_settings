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

The state of this software is pre-alpha, so it should only be used in development
environments. Comments, thoughts and patches are highly welcome.

.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti