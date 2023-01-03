#####  Traveling Salesman #####
#### Jose Mancilla ####
### Independet Study ####



#Import libraries
from shutil import which
import sys
import matplotlib.pyplot as plt
import pandas as pd
from TSP2 import City, read_cities, write_cities, path_cost,long


#Class traveling salesman
class TSP:

    #self and the cities
    def __init__(self, cities):
        self.unvisited = cities[1:]
        self.route = [cities[0]]

   #Function finds the closest city
    def next(self):
        while len(self.unvisited):
            idx, Closest_city = min(enumerate(self.unvisited), #take lambda
                                      key=lambda item: item[1].distance(self.route[-1]))#rest1
            self.route.append(Closest_city)
            del self.unvisited[idx] #delete the city
        self.route.append(self.route[0])
        self.route.pop()
        return path_cost(self.route) #return the path cost


######################
##main
if __name__ == "__main__":

  #output file write
    #sys.stdout=open("tsp_5_1_output.txt","w")
    n = long('tsp_5_1')
    #read the cities
    cities = read_cities(64)
    TSP = TSP(cities)

    print(TSP.next())
    #hul has the route
    hul=list(TSP.route)
 #transform that route to data frames to send it to R
    df=pd.DataFrame(cities)
    ds=pd.DataFrame(hul)


    #sys.stdout.close()

  #save data sets
    df.to_csv(r'/Users/je/Desktop/OWU/Computer Science /Python/OwuPy/TSP/cities_dataframe.csv')
    ds.to_csv(r'/Users/je/Desktop/OWU/Computer Science /Python/OwuPy/TSP/route_dataframe.csv')
