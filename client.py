import socket
class Client:
    
    """
    nodeID: public and private id generated per account per device
    resyncPaths: paths that will be overwritten by data retreived from other servers
    nodes: dict of known nodes in the network. In the form {nodePublicID, addr}
    """

    def __init__(self, nodeID : tuple, resyncPaths : tuple, nodes : dict, port=7070) -> None: # constructor
        self.nodeID = nodeID
        self.resyncPaths = resyncPaths
        self.nodes = nodes
        self.port = port
        self.comm = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # comm as in communication which is the attribute that stores the socket itself

    # Method that connects this node as a server to the network
    def connect(self):

        """
        Method that connects this node as a server to the network
        """

        self.seekNodes()
        while True:
            pass

    def seekNodes(self):
        # iterate through nodes and connect to each one
        for node in self.nodes.items():
            self.comm.connect((node[1], self.port))

        self.comm.sendall(self.nodeID[0].encode("UTF-8")) # send every node your publicID to validate connection
        print("Connected to all nodes")

client = Client(("6", "12"), ("",), {5 : "127.0.0.1"})
client.connect()