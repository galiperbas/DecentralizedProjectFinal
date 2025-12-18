class ReputationSystem:
    def __init__(self):
        self.reputation = {}

    def register_node(self, node_id, initial=0.5):
        self.reputation[node_id] = initial

    def update(self, node_id, delta):
        self.reputation[node_id] = max(0, min(1, self.reputation[node_id] + delta))

    def get(self, node_id):
        return self.reputation.get(node_id, 0)
