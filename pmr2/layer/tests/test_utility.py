import unittest

import zope.interface

from pmr2.layer.utility import ConditionalLayerApplierFactory


class ITestLayer(zope.interface.Interface):
    pass


class TestLayerApplierFactory(unittest.TestCase):

    def setUp(self):
        condition = lambda req: req['test'] == '1'
        self.lf = ConditionalLayerApplierFactory(ITestLayer, condition)

    def test_0000_pass(self):
        request = {
            'test': '1',
            'key': 'value',
        }
        self.assertEqual(self.lf(request), ITestLayer)

    def test_0001_fail(self):
        request = {
            'test': '0',
            'key': 'value',
        }
        self.assertEqual(self.lf(request), None)

    def test_0002_malform(self):
        request = {}
        self.assertEqual(self.lf(request), None)
