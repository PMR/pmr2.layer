import zope.interface
from pmr2.layer.utility import ConditionalLayerApplierBase


class IExampleTestLayer(zope.interface.Interface):
    """Example."""


class TestLayerApplier(ConditionalLayerApplierBase):
    layer = IExampleTestLayer
    def condition(self, request):
        return 'application/vnd.example.com-v1' in request['HTTP_ACCEPT']
