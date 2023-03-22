from api import completion, chatCompletion
from utils import extract_completion_response, generate_user_message, generate_assistant_message

def main():
    #testCompletion()
    testChatCompletion()
    return

def testCompletion():
    res = completion("What is software engineering", 50)
    print(extract_completion_response(res))

def testChatCompletion():
    res = chatCompletion([
        generate_user_message("What is software engineering"),
        generate_assistant_message("are you asking about skill"),
        generate_user_message("yes"),
    ])
    print(res)

main()