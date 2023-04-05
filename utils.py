from openai import openai_object
import sys
import time

def stream_response_to_stdout(res, resArr = None):
    for ans in res:
        sys.stdout.write(ans.choices[0].text)
        sys.stdout.flush()
        if resArr:
            resArr.append(ans.choices[0].text)
        time.sleep(0.1) # slow down the output so it looks natural to human

# print the response in green with a jitter of 0.1 s
def stream_chat_completion_to_stdout(res, resArr = None):
    sys.stdout.write("\033[32m")
    for ans in res:
        delta = ans.choices[0].delta
        if "content" in delta and delta.content != None:
            sys.stdout.write(delta.content)
            sys.stdout.flush()
            if resArr:
                resArr.append(delta.content)
            time.sleep(0.1) # slow down the output so it looks natural to human
    sys.stdout.write("\033[0m")        

def generate_user_message(msg: str):
    return {"role": "user", "content": msg}

def generate_assistant_message(msg: str):
    return {"role": "assistant", "content": msg}

def generate_system_message(msg: str):
    return {"role": "system", "content": msg}

