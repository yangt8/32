#Yang Tang 53979886
import mapquest_input
class lat_long():
    """
    Lat and Lng class
    returns the formatted Lat and Lng
    with the compass directions
    """
    def output_self(self,json):
        print('LATLONGS')
        for l in json['route']['locations']:
            lat=l['displayLatLng']['lat']
            long=l['displayLatLng']['lng']
            if lat >= 0:
                unit='N'
            else:
                unit='S'
            if long >= 0:
                unit2='E'
            else:
                unit2='W'
            print('{0:.2f}'.format(lat) + unit + " " + '{0:.2f}'.format(long) + unit2)
        print()

class total_time():
    """
    Total Time class
    returns the estameted time
    of the route
    """
    def output_self(self,json):
        time=json['route']['time']/60
        print('TOTAL TIME: {}'.format(round(time)) + ' minutes')
        print()

class total_distance():
    """
    Total Distance class
    returns the total distance of the route
    """
    def output_self(self,json):
        distance=json['route']['distance']
        print('TOTAL DISTANCE: {}'.format(round(distance)) + ' miles')
        print()
        
class steps():
    """
    Narrative Directions class
    returns the step by step directions
    to the destination (GPS format)
    """
    def output_self(self,json):
        print('DIRECTION')
        for i in json['route']['legs']:
            for d in i['maneuvers']:
                print(d['narrative'])
        print()

class elevation():
    """
    Elevation class that returns the elevation
    for every city individually instead
    of return the elevation of the whole route
    """
    def output_self(self,json):
        print('ELEVATIONS')
        latlong_list=lat_and_long(json)
        for i in range(0,len(latlong_list),2):
            latlong_one=str(latlong_list[i])+','+str(latlong_list[i+1])
            json_file=mapquest_input.get_result(mapquest_input.build_elevation_url(latlong_one))
            for n in json_file['elevationProfile']:
                print(round(n['height']))
    print()

def lat_and_long(json: dict)-> list:
    """
    Takes a json converted object
    and returns a list with the lat and lng
    """
    text = json["route"]["locations"]
    lat_long_list = []
    for i in text:
        lat_long_list.append(i["displayLatLng"]["lat"])
        lat_long_list.append((i["displayLatLng"]["lng"]))
    return lat_long_list
