from sdk.agent import Agent
from core.flow import TaskNode, TaskFlow
from core.orchestrator import Orchestrator

def reply_task(user_input, state):
    if "hello" in user_input.lower():
        return "Hello! Nice to meet you 😊"
    elif "bye" in user_input.lower():
        return "Goodbye! See you soon 👋"
    else:
        return f"You said: {user_input}"

reply_node = TaskNode("Reply", reply_task)
flow = TaskFlow(reply_node)
agent = Agent("InteractiveAgent", flow)

if __name__ == "__main__":
    orch = Orchestrator()

    print("🤖 Interactive Agent Started")
    print("Type 'exit' to stop\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Agent: Goodbye 👋")
            break

        response = orch.run(flow, user_input)
        print("Agent:", response)
