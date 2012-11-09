import zope.interface

from pmr2.layer.interfaces import ILayerApplier


class ConditionalLayerApplierBase(object):
    zope.interface.implements(ILayerApplier)
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
