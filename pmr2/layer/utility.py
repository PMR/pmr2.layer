import zope.interface

from pmr2.layer.interfaces import ILayerApplier


class LayerApplierBase(object):
    zope.interface.implements(ILayerApplier)
    def __call__(self, request):
        raise NotImplementedError


class ConditionalLayerApplierBase(LayerApplierBase):
    layer = None

    def condition(self, request):
        raise NotImplementedError

    def __call__(self, request):
        try:
            result = self.condition(request)
        except:
            # XXX log this?
            result = False

        if result:
            return self.layer


def ConditionalLayerApplierFactory(iface, cond):
    class ConditionalLayerApplier(ConditionalLayerApplierBase):
        layer = iface
        def condition(self, request):
            return cond(request)

    return ConditionalLayerApplier()
