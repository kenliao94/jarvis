#!/usr/bin/python3

import sys
from api import completion, chatCompletion
from utils import (
    stream_response_to_stdout,
    generate_user_message,
    generate_assistant_message,
    stream_chat_completion_to_stdout,
)
from actions import isActionQuery, handleActionQuery


def main():
    validateArgs()
    if sys.argv[1] == "ask":
        query = input("Your question: ")
        res = completion(query, 1000)
        stream_response_to_stdout(res)
    elif sys.argv[1] == "chat":
        print("Starting chat session. Quit by typing 'quit' or ctrl + D")
        history = []
        while True:
            query = input("> ")
            if query == "quit":
                break
            if isActionQuery(query):
                result = handleActionQuery(query, history)
                if result == "<|NO_OPS|>":
                    continue
                query = result
            history.append(generate_user_message(query))
            res = chatCompletion(history)
            resArr = []
            stream_chat_completion_to_stdout(res, resArr)
            print("\n")
            sentence = "".join(resArr)
            history.append(generate_assistant_message(sentence))
    else:
        raise Exception("Unsupported sub function")

def validateArgs():
    if len(sys.argv) != 2:
        print("Usage: python main.py ask|chat")
        raise Exception("Invalid arguments")
    if not sys.argv[1] in ["chat", "ask"]:
        raise Exception("Unsupported sub function")


if __name__ == "__main__":
    main()
