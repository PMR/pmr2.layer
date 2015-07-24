import unittest

from zope.component.hooks import getSiteManager

from plone.app.testing import PLONE_FUNCTIONAL_TESTING

from pmr2.layer.interfaces import ILayerApplier
from pmr2.layer.subscriber import mark_layer
from pmr2.layer.tests import utility


class DummyEvent(object):
    def __init__(self, request):
        self.request = request


class MarkLayerTestCase(unittest.TestCase):

    layer = PLONE_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.portal.REQUEST
        self.event = DummyEvent(self.request)

    def test_0000_basic(self):
        self.assertFalse(hasattr(self.event.request, '_pmr2layermarker_'))
        mark_layer(self.portal, self.event)
        self.assertTrue(self.event.request._pmr2layermarker_)

    def test_0001_standard(self):
        sm = getSiteManager()
        sm.registerUtility(utility.TestLayerApplier(), ILayerApplier,
            name='testlayer')
        self.request['HTTP_ACCEPT'] = 'application/vnd.example.com-v1'

        self.assertFalse(utility.IExampleTestLayer.providedBy(self.request))
        mark_layer(self.portal, self.event)
        self.assertTrue(utility.IExampleTestLayer.providedBy(self.request))
