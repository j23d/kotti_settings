kotti_navigation browser tests
==============================

Setup and Login
---------------

  >>> from kotti import testing
  >>> tools = testing.setUpFunctional(
  ...     **{'kotti.configurators': 'kotti_settings.kotti_configure',
  ...        'kotti.populators': 'kotti.testing._populator kotti_settings.testing._add_browser_settings'
  ... })
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


Get to the settings page and change some settings
-------------------------------------------------

  >>> browser.open(testing.BASE_URL + '/@@settings')
  >>> 'Settings' in browser.contents
  True

  >>> 'Testsettings Schema' in browser.contents
  True
  >>> 'type="text" name="kotti_settings.testing-testrageintsetting" value="5"' in browser.contents
  True
  >>> 'type="text" name="kotti_settings.testing-teststringsetting" value="hello world"' in browser.contents
  True

  >>> ctrl('String').value = 'hello you'
  >>> ctrl('Ranged Int').value = 'nan'
  >>> ctrl(name='save').click()
  >>> 'There was a problem' in browser.contents
  True
  >>> '"nan" is not a number' in browser.contents
  True

  >>> ctrl('Ranged Int').value = '23'
  >>> ctrl(name='save').click()
  >>> 'There was a problem' in browser.contents
  True
  >>> '23 is greater than maximum value 10' in browser.contents
  True

  >>> ctrl('Ranged Int').value = '7'
  >>> ctrl(name='save').click()
  >>> 'type="text" name="kotti_settings.testing-testrageintsetting" value="7"' in browser.contents
  True
  >>> 'type="text" name="kotti_settings.testing-teststringsetting" value="hello you"' in browser.contents
  True
