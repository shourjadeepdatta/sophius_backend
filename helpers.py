import re
from config import client



def call_generative_function(para,no_of_questions):
    completion = client.chat.completions.create(
    extra_headers={
        # "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        # "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    extra_body={},
    model="google/gemini-2.0-flash-thinking-exp:free",
    messages=[
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": f"Please generate {no_of_questions} questions on this paragraph"
            },
            {
            "type": "text",
            "text": para
            }
        ]
        }
    ]
    )

    # print(completion.choices[0].message.content)
    # print(type(completion.choices[0].message.content))

    qna_list = completion.choices[0].message.content.split("\n\n")
    print(qna_list)
    real_qna_list = qna_list[1:]
    clean_lst = []
    print("-------------------------------")
    # print(real_qna_list)
    for each in real_qna_list:
        cleaned_str = re.sub(r"\(.*?\)", "", each)
        without_white_spaces = cleaned_str.lstrip(" ")
        final_ques = without_white_spaces.replace("**","")
        clean_lst.append(final_ques)

    print(clean_lst)
    return clean_lst