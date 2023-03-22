from openai import openai_object

# It extracts the response from openai 
def extract_completion_response(res: openai_object):
    try:
        return res.choices[0].text
    except Exception as e:
        print(f"Encounter exception when extracting OAI response: {e}. The response is {res}")
        return None
    

def generate_user_message(msg: str):
    return {"role": "user", "content": msg}

def generate_assistant_message(msg: str):
    return {"role": "assistant", "content": msg}
