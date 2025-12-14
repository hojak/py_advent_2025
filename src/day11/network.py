class Network:

    def __init__(self, definition: str):
        self.nodes = {}

        for line in definition.splitlines():
            (source_node, connected_to) = line.split(":")
            source_node = source_node.strip()

            self.add_node(source_node)

            for target_node in connected_to.strip().split(" "):
                target_node = target_node.strip()
                self.add_node(source_node.strip())

                self.nodes[source_node].append(target_node)

    def size(self) -> int:
        return len(self.nodes)

    def add_node(self, node_name: str):
        if node_name not in self.nodes:
            self.nodes[node_name] = []

    def find_all_paths_from_to(self, start: str, goal: str) -> list[list[str]]:
        result = []
        queue = [(start, [start])]

        while queue:
            (current_node, path) = queue.pop(0)

            if current_node == goal:
                result.append(path)
                continue

            for neighbor in self.nodes[current_node]:
                if neighbor not in path:
                    queue.append((neighbor, path + [neighbor]))

        return result

    def get_number_of_possible_paths(self, start: str, goal: str) -> int:
        return len(self.find_all_paths_from_to(start, goal))
