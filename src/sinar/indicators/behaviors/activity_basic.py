# -*- coding: utf-8 -*-

from plone import schema
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface, implementer, provider

from sinar.indicators import _


class IActivityBasicMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IActivityBasic(model.Schema):
    """
    """

    activity_participants_male = schema.Int(
        title=_(u'Male Participants'),
        description=_(u'Number of Participants'),
        required=False,
    )

    activity_participants_female = schema.Int(
        title=_(u'Female Participants'),
        description=_(u'Number of Participants'),
        required=False,
    )

    activity_participants_other= schema.Int(
        title=_(u'Other Participants'),
        description=_(u'Number of non-Binary Participants'),
        required=False,
    )

    # fieldset set the tabs on the edit form

    fieldset(
            'indicators',
            label=_(u'Indicators'),
            fields=[
                'activity_participants_male',
                'activity_participants_female',
                'activity_participants_other',
                ],
            )




@implementer(IActivityBasic)
@adapter(IActivityBasicMarker)
class ActivityBasic(object):
    def __init__(self, context):
        self.context = context

    @property
    def activity_participants_male(self):
        if safe_hasattr(self.context, 'activity_participants_male'):
            return self.context.activity_participants_male
        return None

    @activity_participants_male.setter
    def activity_participants_male(self, value):
        self.context.activity_participants_male = value

    @property
    def activity_participants_female(self):
        if safe_hasattr(self.context, 'activity_participants_female'):
            return self.context.activity_participants_female
        return None

    @activity_participants_female.setter
    def activity_participants_female(self, value):
        self.context.activity_participants_female = value

    @property
    def activity_participants_other(self):
        if safe_hasattr(self.context, 'activity_participants_other'):
            return self.context.activity_participants_other
        return None

    @activity_participants_other.setter
    def activity_participants_other(self, value):
        self.context.activity_participants_other = value
