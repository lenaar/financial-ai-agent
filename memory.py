from langgraph.checkpoint.sqlite import SqliteSaver

def get_memory_saver():
    print("Creating memory saver")
    return SqliteSaver.from_conn_string(":memory:")
