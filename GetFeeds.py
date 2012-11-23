'''
Created on Nov 21, 2012

@author: kevin
'''
import main
import Twitter

def get_feeds():
    main.connect_foursquare()
    Twitter.connect_twitter()
 
if __name__ == '__main__':
    main.connect_foursquare()
    Twitter.connect_twitter()
    pass