# -*- coding: utf-8 -*-
"""Setup tests for this package."""
import unittest

from plone import api
from plone.app.testing import TEST_USER_ID, setRoles

from sinar.indicators.testing import SINAR_INDICATORS_INTEGRATION_TESTING  # noqa: E501

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that sinar.indicators is properly installed."""

    layer = SINAR_INDICATORS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if sinar.indicators is installed."""
        self.assertTrue(self.installer.is_product_installed(
            'sinar.indicators'))

    def test_browserlayer(self):
        """Test that ISinarIndicatorsLayer is registered."""
        from plone.browserlayer import utils

        from sinar.indicators.interfaces import ISinarIndicatorsLayer
        self.assertIn(
            ISinarIndicatorsLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = SINAR_INDICATORS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstall_product('sinar.indicators')
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if sinar.indicators is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed(
            'sinar.indicators'))

    def test_browserlayer_removed(self):
        """Test that ISinarIndicatorsLayer is removed."""
        from plone.browserlayer import utils

        from sinar.indicators.interfaces import ISinarIndicatorsLayer
        self.assertNotIn(ISinarIndicatorsLayer, utils.registered_layers())
