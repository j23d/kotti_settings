import colander
import deform

from kotti_settings import _

# hold the setting objects
SETTINGS = []

# Here we define some default schemas.
slot_names = (('left', _(u'left')),
              ('right', _(u'right')),
              ('abovecontent', _(u'abovecontent')),
              ('belowcontent', _(u'belowcontent')),
              ('beforebodyend', _(u'beforebodyend')),)


class SlotSchemaNode(colander.SchemaNode):
    name = 'slot'
    title = _(u'Direction')
    default = u'left'
    widget = deform.widget.SelectWidget(values=slot_names)


show_in_context = (('everywhere', _(u'Everywhere')),
                   ('only on root', _(u'Only on root')),
                   ('not on root', _(u'Not on root')),
                   ('nowhere', _(u'Nowhere')))


class ShowInContextSchemaNode(colander.SchemaNode):
    name = 'show_in_context'
    title = _(u'Show in context')
    default = u'everywhere'
    widget = deform.widget.SelectWidget(values=show_in_context)
