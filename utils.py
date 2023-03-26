from openai import openai_object
import sys
import time

def stream_response_to_stdout(res, resArr = None):
    for ans in res:
        sys.stdout.write(ans.choices[0].text)
        sys.stdout.flush()
        if resArr:
            resArr.append(ans.choices[0].text)
        time.sleep(0.2) # slow down the output so it looks natural to human

def stream_chat_completion_to_stdout(res, resArr = None):
    for ans in res:
        delta = ans.choices[0].delta
        if "content" in delta and delta.content != None:
            sys.stdout.write(delta.content)
            sys.stdout.flush()
            if resArr:
                resArr.append(delta.content)
            time.sleep(0.2) # slow down the output so it looks natural to human

def generate_user_message(msg: str):
    return {"role": "user", "content": msg}

def generate_assistant_message(msg: str):
    return {"role": "assistant", "content": msg}
