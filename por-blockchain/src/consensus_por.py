import numpy as np


class PoRConsensus:
    def __init__(self, reputation_system, threshold=0.6):
        self.rep_sys = reputation_system
        self.threshold = threshold

    def approve_block(self, approving_nodes):
        reps = [self.rep_sys.get(n.node_id) for n in approving_nodes]
        avg_rep = np.mean(reps)
        return avg_rep >= self.threshold, avg_rep
