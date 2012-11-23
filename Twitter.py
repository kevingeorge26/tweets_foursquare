'''
Created on Nov 21, 2012

@author: kevin
'''

import tweepy
import sqlite3
import datetime

consumer_key="Wc1X1bLYbWtyfCqPYFkgA"
consumer_secret="rRGRqjWbsEWz6W4dnq7QhGDItsQZNdP0bP9kNEnEhc"

places = {"new york":"40.749094,-73.992752","chicago":"41.878436,-87.630123","sfo":"37.780654,-122.416241","cali":"34.026486,-118.289509"}

def connect_twitter():
        
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)    
    api = tweepy.API(auth)
    
    conn = sqlite3.connect('/home/kevin/workspace/FourSquare/foursquare.sqlite')
    conn.text_factory = str
    now = datetime.datetime.now()
    
    for city in places.keys():        
        result  = api.search(" ",rpp=100,geocode=places[city]+",2mi")    
        for tweet in result:
            conn.executemany("INSERT INTO tweets (tweet,city,datetime)  VALUES (?,?,?) ",[ ( tweet.text,city,str(now) ) ] )

    conn.commit()
    conn.close()
    
if __name__ == '__main__':
    connect_twitter()
    pass