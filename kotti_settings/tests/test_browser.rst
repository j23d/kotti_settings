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
  >>> ctrl('Username or email', index=0).value = 'admin'
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
  >>> 'Some settings in a schema.' in browser.contents
  True
  >>> 'type="text" name="kotti_settings-testrageintsetting" value="5"' in browser.contents
  True
  >>> 'type="text" name="kotti_settings-teststringsetting" value="hello world"' in browser.contents
  True


  >>> ctrl(name='kotti_settings-teststringsetting').value = 'hello you'
  >>> ctrl(name='kotti_settings-testrageintsetting').value = 'nan'
  >>> ctrl(name='save_kotti_settings-test_settings_schema_browser').click()
  >>> 'There was a problem' in browser.contents
  True
  >>> '"nan" is not a number' in browser.contents
  True

  >>> ctrl(name='kotti_settings-testrageintsetting').value = '23'
  >>> ctrl(name='save_kotti_settings-test_settings_schema_browser').click()
  >>> 'There was a problem' in browser.contents
  True
  >>> '23 is greater than maximum value 10' in browser.contents
  True

  >>> ctrl(name='kotti_settings-testrageintsetting').value = '7'
  >>> ctrl(name='save_kotti_settings-test_settings_schema_browser').click()
  >>> 'type="text" name="kotti_settings-testrageintsetting" value="7"' in browser.contents
  True
  >>> 'type="text" name="kotti_settings-teststringsetting" value="hello you"' in browser.contents
  True
  >>> u"Successfully saved test settings." in browser.contents
  True

  >>> ctrl(name='cancel', index=0).click()
  >>> u"No changes made." in browser.contents
  True

  >>> ctrl(name='save_kotti_settings-test_settings_dict').click()
  >>> 'type="text" name="kotti_settings-testsetting_2" value="23"' in browser.contents
  True
