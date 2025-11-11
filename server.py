import socket
import threading

class Server:
    
    """
    nodeID: public and private id generated per account per device
    resyncPaths: paths that will be pulled from when broadcasting data to sync
    nodes: dict of known nodes in the network. In the form {nodePublicID, addr}
    """

    def __init__(self, nodeID : tuple, resyncPaths : tuple, nodes : dict, port=7070) -> None:
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
        self.comm.bind(("0.0.0.0", self.port)) # binds the server to listen for incoming connections in the next line
        self.comm.listen() # starts the server listening for incoming connections
        acceptingThread = threading.Thread(target=self.acceptIncoming, daemon=True) # defines a thread for accepting incoming connections
        acceptingThread.start() # starts the accepting thread
        while True:
            input("Hit Enter to end")
            break


    def acceptIncoming(self):
        addrs = [] # stores all connected addresses to add to address list
        sockets = [] # stores all sockets for communication
        while True:
            clientSocket, addr = self.comm.accept()
            print(f"Connection from: {addr}")
            print(clientSocket.recv(1024).decode("UTF-8"))
            addrs.append(addr[0])
            clientSocket.close()

server = Server(("5", "10"), ("",), {6 : "127.0.0.1"})
server.connect()

    