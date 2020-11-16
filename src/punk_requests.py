"""
Punk Request module
-------------------
"""
import json
import requests
from src.constant import PUNK_CONSTANTS


def get_beer_by_id(ids: str) -> json:
    """
    Get beer information by id
    :param ids: Str exact id or ids in (id|id|...) format
    :return: List of Beer data in Json format
    """
    return requests.get(PUNK_CONSTANTS["URL"], params={PUNK_CONSTANTS["BEER"]["ID"]: ids}).json()


def get_beer_by_name(beer_name: str) -> json:
    """
    Get beer information by name
    :param beer_name: Str beer name information as partial or full match
    :return: List of Beer data in Json format
    """
    return requests.get(PUNK_CONSTANTS["URL"],
                        params={PUNK_CONSTANTS["BEER"]["NAME"]: beer_name}).json()


def get_beer_brewed_in(brewed_after: str, brewed_before: str) -> json:
    """
    Get beer brewed in interval
    :param brewed_after: Str Brewed after e.g 10.2011
    :param brewed_before: Str Brewed before e.g 10.2018
    :return: List of Beer data in Json format or empty list
    """
    res = requests.get(PUNK_CONSTANTS["URL"],
                        params={PUNK_CONSTANTS["BEER"]["AFTER"]: brewed_after,
                                PUNK_CONSTANTS["BEER"]["BEFORE"]: brewed_before}).json()
    return [{
        "id": b["id"],
        "name": b["name"],
        "food_pairing": b["food_pairing"],
        "first_brewed": b["first_brewed"],
        "abv": b["abv"],
        "ibu": b["ibu"]
        }
        for b in res]


def get_beer_by_food(food_paring: str) -> json:
    """
    Get beer brewed in interval
    :param food_paring: Str to math with food options [in fuzzy search]
    :return: List of Beer data in Json format or empty list
    """
    res = requests.get(PUNK_CONSTANTS["URL"],
                       params={PUNK_CONSTANTS["BEER"]["FOOD_PAIRING"]: food_paring}).json()
    return [{
        "id": b["id"],
        "name": b["name"],
        "food_pairing": b["food_pairing"],
        "abv": b["abv"],
        "ibu": b["ibu"]
        }
        for b in res]
