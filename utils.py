from openai import openai_object
import sys
import time

def stream_response_to_stdout(res):
    for ans in res:
        sys.stdout.write(ans.choices[0].text)
        sys.stdout.flush()
        time.sleep(0.2) # slow down the output so it looks natural to human

def generate_user_message(msg: str):
    return {"role": "user", "content": msg}

def generate_assistant_message(msg: str):
    return {"role": "assistant", "content": msg}
