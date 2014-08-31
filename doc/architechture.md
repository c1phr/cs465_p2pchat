Architecture
============

The first peer in the network is active and listens for incoming join
requests. The assumption is made that the second peer hoping to join the
network knows the IP of the original peer. 

In order to join the network, a new peer sends a message to a peer already
on the network. Again, it is assumed that new peers know at least one
address that is within the network. When a peer participating in the network
receives a join request from an unconnected host, it:
 1. Responds with an acknowledgement of the receipt and a list of all
    connected peers. 
 2. Adds the IP of the new peer to its internal list of active peers, and
    sends a message to all peers on the network to inform them that the new
    peer has joined. 
 3. Sends a log of the past ~100 messages to the new peer.

The chat function operates on TCP. Each connected peer maintains a list of
other peers on the network. When a peer sends a message, it establishes a
TCP connection with each peer on the network, in turn, sends its message
over the TCP link, and disconnects. 

Each peer maintains a list of the past 100 messages it's received, on a
rolling basis: past the 100-message limit, when new messages are received,
the message in the log which was received earliest is discarded. 
