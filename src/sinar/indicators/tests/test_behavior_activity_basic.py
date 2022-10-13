# -*- coding: utf-8 -*-
import unittest

from plone.app.testing import TEST_USER_ID, setRoles
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

from sinar.indicators.behaviors.activity_basic import IActivityBasicMarker
from sinar.indicators.testing import SINAR_INDICATORS_INTEGRATION_TESTING  # noqa


class ActivityBasicIntegrationTest(unittest.TestCase):

    layer = SINAR_INDICATORS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_activity_basic(self):
        behavior = getUtility(IBehavior, 'sinar.indicators.activity_basic')
        self.assertEqual(
            behavior.marker,
            IActivityBasicMarker,
        )
