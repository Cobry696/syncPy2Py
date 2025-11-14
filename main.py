from client import Client
from server import Server
import socket
import os

class Node:
    
    """
    userID: ID generated from account that is the same over multiple sessions
    syncedPaths: paths to locations that will be synced between nodes
    """

    def __init__(self, userID : int, syncedPaths : list, nodes : dict) -> None:
        self.userID = userID
        self.syncedPaths = syncedPaths
        self.nodes = nodes
        self.server = Server(userID, syncedPaths)
        self.client = Client(userID, syncedPaths)

    def connect(self):
        """
        Method that connects Node to the network
        Depending on the amount of nodes the program will dynamically decide how many individual nodes to connect to
        if there are 64 nodes will connect to every 8th node
        then these middle 8 nodes will connect to one another to form a central part of the network
        goal is for each nodes number of connections to be 9 or less, so it shares 10 or less datapoints to its parent node
        will continue this process of connecting to sqrt(n) nodes until that number is 10
        this makes it so each nodes new changes get consolodated into one place that can be shared to everyone

        If a node disconnects from the network the next node will replace it.
        For example. If node 8 gets disconnected then we have a hole and the central 8 nodes are not getting all of the data
        Then node 9 will receive the incoming connection from node 1 and join in node 8s place in the central network
        """
        nodeAmount = len(self.nodes)
        pass                   

    def sync(self):
        
        """
        Syncs data between every node on the network
        """    
        for path in self.syncedPaths:
            files = os.listdir(path)
            for f in files:
                if os.path.isfile(f):
                    print(f)