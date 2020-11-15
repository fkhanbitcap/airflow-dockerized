import requests
import json
from devchallenge.constant import PUNK_CONSTANTS


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
    return requests.get(PUNK_CONSTANTS["URL"], params={PUNK_CONSTANTS["BEER"]["NAME"]: beer_name}).json()


def get_beer_brewed_in(brewed_after: str, brewed_before: str) -> json:
    """
    Get beer brewed in interval
    :param brewed_after: Str Brewed after e.g 10.2011
    :param brewed_before: Str Brewed before e.g 10.2018
    :return: List of Beer data in Json format or empty list
    """
    return requests.get(PUNK_CONSTANTS["URL"], params={PUNK_CONSTANTS["BEER"]["AFTER"]: brewed_after,
                                                       PUNK_CONSTANTS["BEER"]["BEFORE"]: brewed_before}).json()
