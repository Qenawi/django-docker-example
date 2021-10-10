#   Qenawi created AnalyticUrls.py at 4/29/21, 10:14 PM
#   AnalyticUrls.py @Docs
#
from django.urls import path
from myproject.myapp.features.gaming.game.view.GamingView import list_all, insert
from myproject.myproject.settings.base import MEDIA_URL, MEDIA_ROOT, DEBUG
from django.conf.urls.static import static

# view variables
_pathBase = "crud"
_ListAll = "match"
_AddItem = "add_match"
_DeleteItem = "delete_match"

# Feature Urls
urlpatterns = [
    path(_pathBase + '/' + _ListAll, list_all, name='index'),
    path(_pathBase + '/' + _AddItem, insert, name='add_match')

]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
