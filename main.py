'''
Created on Nov 20, 2012

@author: kevin
'''

import foursquare
import sqlite3
import datetime

# activity based on time https://developer.foursquare.com/docs/venues/timeseries
# trending locations https://developer.foursquare.com/docs/venues/trending
places = {"new york":"40.749094,-73.992752","chicago":"41.878436,-87.630123","sfo":"37.780654,-122.416241","cali":"34.026486,-118.289509"}

def connect_foursquare():
  
    global places
    
    conn = sqlite3.connect('/home/kevin/workspace/FourSquare/foursquare.sqlite')
    conn.text_factory = str
    now = datetime.datetime.now()
    
    for k in places.keys():    
        print k
          
        client = foursquare.Foursquare(client_id='GJPWWXSBRKXNNZ1EHX2S2K53HW1PD0MORDFCGKPZKX0DVFV1', 
                                       client_secret='LNXDLIAMJSPXZ3QJ02A4LXIADKEMF0XJWQI5MXXU5NQN5LJD')
        
        venues =  client.venues.trending( {"ll":places[k],"limit":50,"radius":2000}, multi=False)["venues"]
       
       
        
        for venue in venues:
            val  =  [( venue["location"]["lat"],venue["location"]["lng"],venue["name"], venue["categories"][0]["name"],str(now),venue["hereNow"]["count"],k )] 
           
            conn.executemany("INSERT INTO foursquare (lat,long,name,type,datetime,count,city_py) VALUES (?,?,?,?,?,?,?) ",val)      
            
        
    conn.commit()
    conn.close()
    
def play_python():
    print "something"
    

if __name__ == '__main__':
    connect_foursquare()
    pass