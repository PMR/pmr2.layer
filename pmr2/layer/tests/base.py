from Zope2.App import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup
from Products.PloneTestCase.layer import onteardown


@onsetup
def setup():
    import pmr2.layer
    fiveconfigure.debug_mode = True
    zcml.load_config('configure.zcml', pmr2.layer)
    zcml.load_config('testing.zcml', pmr2.layer.tests)
    fiveconfigure.debug_mode = False

@onteardown
def teardown():
    pass

setup()
teardown()
ptc.setupPloneSite()


class TestCase(ptc.PloneTestCase):
    pass
