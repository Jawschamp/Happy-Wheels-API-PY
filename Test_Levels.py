import requests
import xmltodict
import json

class Translator:
    date = "dp"
    level_name = "in"
    author = "un"
    disc = "uc"
    player_count = "pc"
    level_rating = "rg"

class Level:
    search = "http://totaljerkface.com/get_level.hw"

    def search_level_by_level_name(name_of_lvl):
        """'sortby` allows for search by newest or oldest"""
        payload = {
            "action": "search_by_name",
            "page": "1",
            "sortby": "newest",
            "uploaded": "week",
            "sterm": name_of_lvl
        }
        request = requests.request("POST", url=Level.search, data=payload)
        jsondict = xmltodict.parse(request.content)
        """Not needed unless your testing."""
        with open("Test.json", "w") as f:
            json.dump(jsondict, f)
        return jsondict

LevelParser = Level.search_level_by_level_name(name_of_lvl="Level Name")

print("Author says" + LevelParser["lvs"]["lv"][Translator.disc])
