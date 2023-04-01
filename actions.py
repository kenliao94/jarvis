import os

"""
Here is the list of supported action query:
1. Write the previous response to a file.
[PIPE] <path to the file> 

2. Annotate a prompt. {[TAG_NAME]} will be replaced by a predefined string.
[ANNOTATE] {[TAG_NAME]} prompt {[TAG_NAME]} 

3. Use a predefined prompt template
[TEMPLATE] <name of the template>
"""
def isActionQuery(query):
    return (
        query.startswith("[PIPE]")
        or query.startswith("[ANNOTATE]")
        or query.startswith("[TEMPLATE]")
    )

def handleActionQuery(query, history):
    if query.startswith("[PIPE]"):
        # Get the path
        query_tokens = query.strip().split(" ")
        if len(query_tokens) != 2:
            print("[PIPE] action requires prompt in the follow format: [PIPE] <path to files>")
            return "<|NO_OPS|>"
        
        filepath = query_tokens[-1]
        current_path = os.getcwd()
        
        return "<|NO_OPS|>"
    elif query.startswith("[ANNOTATE]"):
        raise NotImplementedError
    elif query.startswith("[TEMPLATE]"):
        raise NotImplementedError
    
    raise Exception(f"Unsupported action query: {query}")