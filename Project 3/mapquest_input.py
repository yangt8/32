#Yang Tang 53979886
import json
import urllib.parse
import urllib.request

MAPQUEST_API_KEY = '5E6x6W1UOqA2V2nmvYJt3FOpI5quF0yU'
MAPQUEST_URL = "http://open.mapquestapi.com/directions/v2/"
ELEVATION_URL = "http://open.mapquestapi.com/elevation/v1/"

def build_mapquest_url(location_list:list) -> str:
    """
    Takes the city or street destinations and returns
    a str representing the url to the API
    """
    query_parameters = [
        ('key', MAPQUEST_API_KEY), ('from',location_list[0])]
    for i in range(1,len(location_list)):
        query_parameters.append(('to',location_list[i]))
    return MAPQUEST_URL + "route?" + urllib.parse.urlencode(query_parameters)

def build_elevation_url(latlong:str)->str:
    """
    Takes the latitude and longtitude in a string format
    and returns the url for the elevation API
    """
    query_parameters = [
        ('key', MAPQUEST_API_KEY), ("unit","f"), ('latLngCollection',latlong)]
    return ELEVATION_URL + "profile?" + urllib.parse.urlencode(query_parameters)


def get_result(url: str) -> dict:
    '''
    This function takes a URL and returns a Python dictionary representing the
    parsed JSON response.
    '''
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)
    finally:
        if response != None:
            response.close()
