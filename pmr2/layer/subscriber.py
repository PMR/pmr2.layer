from zope.interface import Interface
from zope.interface import directlyProvidedBy, directlyProvides
from zope.component import getAllUtilitiesRegisteredFor

from pmr2.layer.interfaces import ILayerApplier


def mark_layer(site, event):
    """
    A subscriber based on the one found in plone.browserlayer.layer.
    """

    if getattr(event.request, "_pmr2layermarker_", False):
        return
    event.request._pmr2layermarker_ = True

    request = event.request
    layer_utils = getAllUtilitiesRegisteredFor(ILayerApplier)
    layers = []

    for lu in layer_utils:
        try:
            layer = lu(request)
        except:
            # XXX should log this down with a warning.
            continue

        if layer:
            layers.append(layer)

    # Filter out bad entries.
    layers = [layer for layer in layers if issubclass(layer, Interface)]
    ifaces = layers + list(directlyProvidedBy(request))

    directlyProvides(request, *ifaces)
