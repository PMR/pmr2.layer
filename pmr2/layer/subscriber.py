from zope.interface import Interface
from zope.interface import directlyProvidedBy, directlyProvides
from zope.component import getAllUtilitiesRegisteredFor

from pmr2.layer.interfaces import ILayerApplier


def isinterface(o):
    try:
        return issubclass(o, Interface)
    except:
        # because some builtins (like None) will fail, and I don't care
        return False


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
            result = lu(request)
        except:
            # XXX should log this down with a warning.
            continue

        if not result:
            continue

        if not isinstance(result, list):
            result = [result]

        layers.extend(layer for layer in result if isinterface(layer))

    # Filter out bad entries.
    ifaces = layers + list(directlyProvidedBy(request))

    directlyProvides(request, *ifaces)
