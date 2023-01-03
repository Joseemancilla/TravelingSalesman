# Traveling Salesman
 
The Traveling Salesman Problem (TSP) involves finding the shortest possible route that visits a given set of locations and returns to the starting point. 
# Implementation of Solution 
The solution to the Traveling Salesman Problem (TSP) implemented in Python. The TSP class has a constructor that takes a list of City objects as input and initializes an instance variable "self.unvisited" with all the cities except the first one. It also initializes another instance variable "self.route" with the first city in the list. The TSP class has a method called "next" that finds the closest city to the current route and adds it to the route. The method continues to do this until all cities have been visited and then returns the total cost of the route. The main function reads in a set of cities from a file, creates an instance of the TSP class with these cities, and prints the cost of the route returned by the "next" method. The program also writes the list of cities and the resulting route to CSV files.




