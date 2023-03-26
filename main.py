#!/usr/bin/python3

import sys
from api import completion
from utils import stream_response_to_stdout

def main():
    validateArgs()
    if sys.argv[1] == "ask":
        query = input("Your question: ")
        res = completion(query, 1000)
        stream_response_to_stdout(res)
    if sys.argv[1] == "chat":
        raise Exception("Chat is not implemented yet")

def validateArgs():
    if len(sys.argv) < 2:
        print("Usage: python main.py ask|chat")
        raise Exception("Invalid arguments")
    if not sys.argv[1] in ["chat", "ask"]:
        raise Exception("Unsupported sub function")
        
    
if __name__ == "__main__":
    main()
