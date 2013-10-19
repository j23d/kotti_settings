Changelog
=========

0.1(2013-10-19)
---------------

* Added documentation for the default schemas.
* Change the implementation to check what settings form was saved.
* Added new util method 'set_setting' where value transformations are handled.
* Removed not needed fanstatic resources.
* Changed the internal name of the forms to be more unique.
* Reinitialize chosen elements when tab is shown.
* Convert boolean to 'true' or 'false' to meet the requirements of deform's checkbox widget.


0.1b4(2013-05-02)
-----------------

* Added a helper method for one of the default setting schemas.
* Only save the settings from the submitted form.
* Set the saved form as the active one.
* Added possibility to remove a widget only from a specific slot.


0.1b3(2013-04-18)
------------------

* Fix: Settings defined in a schema also have to be initialized.


0.1b2(2013-04-18)
-----------------

* Added possibility to remove a widget from the slots.
* Added two default schemas, one to select the slot for the widget and one
  to set where to show the widget.


0.1b1(2013-03-29)
-----------------

* Added event handling for callbacks before and after the settings are saved.


0.1a3(2013-03-13)
-----------------

* Only take the module name itself into account for the setting name.


0.1a2(2013-03-11)
-----------------

* Added util method get_setting as default way to get a setting.


0.1a1(2013-03-06)
-----------------

* Initial release.
