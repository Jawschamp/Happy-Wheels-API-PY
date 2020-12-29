import requests
import xmltodict
import json

class Translator:
    class LevelTranslator:
        date = "dp"
        level_name = "in"
        author = "un"
        disc = "uc"
        player_count = "pc"
        level_rating = "rg"
    class AuthorTranslator:
        date = "@dp"
        id = "@id"
        disc = "@in"
        level_rating = "@rg"
        user = "@un"



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
        request = requests.post(url=Level.search, data=payload).content
        jsondict = xmltodict.parse(request)
        with open("Test.json", "w") as f:
            json.dump(jsondict, f, indent=2)
        return jsondict

class Author:
    def search_author(author_name):
        payload = {
            "action": "search_by_user",
            "page": "1",
            "sortby": "newest",
            "uploaded": "week",
            "sterm": author_name
        }
        request = requests.post(url=Level.search, data=payload).content
        jsondict = xmltodict.parse(request)
        with open("Author.json", "w") as f:
            json.dump(jsondict, f, indent=2)
        return jsondict


def for_author_list(show_full_list, author_name):
    if show_full_list == True:
        LevelParser = Level.search_level_by_level_name(name_of_lvl=author_name)
        for i in LevelParser["lvs"]["lv"]: # Testing
            print(i)
        else:
            pass


