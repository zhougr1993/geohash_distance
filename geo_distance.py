#get distance for two geohash @royzhou thanx for author of geohash
#u can get geohash from https://pypi.python.org/pypi/Geohash
import geohash
import math
Earth_Radius = 6378.137
def rad(d):
    d = float(d)
    return d*math.pi/180.0 
#distance by Latitude and Longitude
def distance(Latitude_1,Longitude_1,Latitude_2,Longitude_2):  
    radlat1 = rad(Latitude_1)  
    radlat2 = rad(Latitude_2)  
    a = radlat1 - radlat2  
    b = rad(Longitude_1) - rad(Longitude_2)  
    s = 2*math.asin(math.sqrt(math.pow(math.sin(a/2),2) + math.cos(radlat1)*math.cos(radlat2)*math.pow(math.sin(b/2),2)))  
    s = s*Earth_Radius
    if s<0:
        s = -s
    return s
#u may get some illegal geocode ,this function would try to get a similar one, would not bring a big deviation     
def get_geohash(hash_str):
    try:
        return geohash.decode(hash_str)
    except:
        hash_str = list(hash_str)
        wrong_ch = hash_str.pop()
        asiic_ch = ord(wrong_ch)+1
        if assic_ch > 90:
            assic_ch = 48
        wrong_ch = chr(assic_ch)
        hash_str.append(wrong_ch)
        hash_str = ''.join(hash_str)
        return get_geohash(hash_str)
def geo_distance(geo_1,geo_2):
    Latitude_1,Longitude_1 = get_geohash(geo_1)
    Latitude_2,Longitude_2 = get_geohash(geo_2)
    return distance(Latitude_1,Longitude_1,Latitude_2,Longitude_2)
