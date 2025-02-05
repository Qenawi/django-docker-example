#   Qenawi created AnalyticsView.py at 4/29/21, 10:11 PM
#   AnalyticsView.py @Docs
#
from django.http import HttpRequest

from myproject.myapp.base.BaseView import view_list_all
from myproject.myapp.base.ResponseFormater import clean_response, sucess_response_from_string
from myproject.myapp.features.gaming.game_match.model.MatchModule import MatchModel as mModel, ChampionType


def list_all(my_request: HttpRequest):
    print(my_request)
    listed = view_list_all(mModel.objects.all())
    return clean_response(listed, "success")


def insert(my_request: HttpRequest):
    print(my_request)
    book = mModel.build_item(dic={"game_id": 1, "champ_type": ChampionType.Default, "match_success_rate": 20.0})
    mModel.insert_item(book)
    return sucess_response_from_string("inserted")
