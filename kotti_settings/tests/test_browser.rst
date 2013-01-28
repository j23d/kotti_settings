kotti_navigation browser tests
==============================

Setup and Login
---------------

  >>> from kotti import testing
  >>> tools = testing.setUpFunctional(
  ...     **{'kotti.configurators': 'kotti_settings.kotti_configure'})
  >>> browser = tools['Browser']()
  >>> ctrl = browser.getControl

  >>> browser.open(testing.BASE_URL + '/@@login')
  >>> 'Log in' in browser.contents
  True
  >>> ctrl('Username or email').value = 'admin'
  >>> ctrl('Password').value = 'secret'
  >>> ctrl(name='submit').click()
  >>> 'Welcome, Administrator' in browser.contents
  True


Get to the settings page
------------------------

  >>> browser.open(testing.BASE_URL + '/@@settings')
  >>> 'Settings' in browser.contents
  True
