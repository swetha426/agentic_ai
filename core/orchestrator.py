from core.state import StateStore
from observability.logger import log_event

class Orchestrator:
    def __init__(self):
        self.state = StateStore()

    def run(self, flow, input_data):
        current = flow.start_node
        data = input_data

        while current:
            log_event(f"Executing node: {current.name}")
            data = current.action(data, self.state)
            current = current.next_nodes[0] if current.next_nodes else None

        return data
