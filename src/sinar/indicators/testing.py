# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
    applyProfile,
)
from plone.testing import z2

import sinar.indicators


class SinarIndicatorsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=sinar.indicators)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'sinar.indicators:default')


SINAR_INDICATORS_FIXTURE = SinarIndicatorsLayer()


SINAR_INDICATORS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SINAR_INDICATORS_FIXTURE,),
    name='SinarIndicatorsLayer:IntegrationTesting',
)


SINAR_INDICATORS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SINAR_INDICATORS_FIXTURE,),
    name='SinarIndicatorsLayer:FunctionalTesting',
)


SINAR_INDICATORS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SINAR_INDICATORS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='SinarIndicatorsLayer:AcceptanceTesting',
)
