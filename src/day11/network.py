class Network:

    def __init__(self, definition: str):
        self.nodes = {}

        for line in definition.splitlines():
            (source_node, connected_to) = line.split(":")
            source_node = source_node.strip()

            self.add_node(source_node)

            for target_node in connected_to.strip().split(","):
                target_node = target_node.strip()
                self.add_node(source_node.strip())

                self.nodes[source_node].append(target_node)

    def size(self) -> int:
        return len(self.nodes)            

    def add_node(self, node_name: str):
        if node_name not in self.nodes:
            self.nodes[node_name] = []
