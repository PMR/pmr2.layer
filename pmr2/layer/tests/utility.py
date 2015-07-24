import zope.interface
from pmr2.layer.utility import ConditionalLayerApplierBase


class IExampleTestLayer(zope.interface.Interface):
    """Example."""


class ITestLayer1(zope.interface.Interface):
    pass


class ITestLayer2(zope.interface.Interface):
    pass


class ITestLayer3(ITestLayer1):
    pass


class TestLayerApplier(ConditionalLayerApplierBase):
    layer = IExampleTestLayer
    def condition(self, request):
        return 'application/vnd.example.com-v1' in request['HTTP_ACCEPT']


class MultiTestLayerApplier(ConditionalLayerApplierBase):
    layer = [ITestLayer1, ITestLayer2, ITestLayer3]
    def condition(self, request):
        return 'application/vnd.example.com.tests' in request['HTTP_ACCEPT']
