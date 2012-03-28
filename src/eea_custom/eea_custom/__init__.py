from Products.Five.browser.pagetemplatefile import \
    ViewPageTemplateFile
#from zope.publisher.browser import BrowserPage
from Products.Five.browser import BrowserView


class EEACustomView(BrowserView):
    """
    EEA custom view
    """

    template = ViewPageTemplateFile('eea_custom.pt')

    def __call__(self):
        return self.template()
