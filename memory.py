from langgraph.checkpoint.sqlite import SqliteSaver

def get_memory_saver():
    print("Creating memory saver")
    return SqliteSaver.from_conn_string(":memory:")


def get_thread_config():
    # you can decide how global or local the thread config is
    # for example, you can use a global thread config for all threads
    # or a local thread config for each thread
    config = {
        "configurable": {"thread_id": 1, "checkpoint_ns": ""}
    }   
    return config