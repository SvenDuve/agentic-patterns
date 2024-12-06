def basic_node_one(state):
    print("I am Node 1")
    return {"graph_state": state["graph_state"] + " I am"}

def basic_node_two(state):
    print("I am Node 2")
    return {"graph_state": state["graph_state"] + " happy!"}

def basic_node_three(state):
    print("I am NOde 3")
    return {"graph_state": state["graph_state"] + " sad!"}