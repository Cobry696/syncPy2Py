from client import Client
from server import Server
import socket

class Node:
    
    """
    userID: ID generated from account that is the same over multiple sessions
    syncedPaths: paths to locations that will be synced between nodes
    """

    def __init__(self, userID : int, syncedPaths : list, nodes : dict) -> None:
        self.userID = userID
        self.syncedPtths = syncedPaths
        self.nodes = nodes
        self.server = Server(userID, syncedPaths)
        self.client = Client(userID, syncedPaths)

    def connect(self):
        """
        Method that connects Node to the network
        
        """
        pass                                                                       