from src.blockchain import Blockchain
from src.reputation import ReputationSystem
from src.node import Node
from src.consensus_por import PoRConsensus
from src.network import Network

# Node'ları oluştur
nodes = [Node(f"node{i}") for i in range(10)]

# Reputation sistemi
rep = ReputationSystem()
for n in nodes:
    rep.register_node(n.node_id, initial=0.8)

# Blockchain ve Network
chain = Blockchain()
network = Network(chain, nodes)
por = PoRConsensus(rep, threshold=0.6)

# Blok öner
block = network.propose_block("TEST_DATA")
approvers = network.get_random_approvers(6)

# PoR doğrulama
decision, avg_rep = por.approve_block(approvers)

if decision:
    chain.add_block(block)
    print("Block accepted")
else:
    print("Block rejected")

print("Average reputation:", avg_rep)
print("Chain length:", len(chain.chain))
