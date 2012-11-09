PMR2 Layers
===========

This module provides a different way to apply layers onto the request.
While the skin-based or browser layer approach is sufficient for most
cases, there are times when these layers need to be dynamic in nature,
such as in the context of a hypermedia driven web-service, where the
same resource identifier can return the same content in different
formats.

Let's try some test cases.
::

    >>> from Testing.testbrowser import Browser
    >>> browser = Browser()
    >>> browser.open(self.portal.absolute_url() + '/@@test-page')
    >>> print browser.contents
    <html>
    <head><title>Test page</title></head>
    <body>
    This is some content.
    </body>
    </html>

The primary use case for this module is to let developers inject a layer
if a condition is met.  This is useful for providing alternative content
types for specific uses, such as for a web service client.  Let's see
what happens if we apply a vendor specific content-accept request.
::

    >>> browser.addHeader('Accept', 'application/vnd.example.com-v1')
    >>> browser.open(self.portal.absolute_url() + '/@@test-page')
    >>> print browser.contents
    {title:'Test Page',content:This is some content.}
