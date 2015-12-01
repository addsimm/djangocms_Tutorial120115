from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class PollsApphook(CMSApp):
    name = _("Polls Application")   # give your application a name (required)
    urls = ["polls.urls"]           # link your app to url configuration(s)
    app_name = "polls"


apphook_pool.register(PollsApphook)  # register the application

