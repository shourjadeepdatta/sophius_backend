from openai import OpenAI
import re

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

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
          "text": "Please generate 4 questions on this paragraph"
        },
        {
          "type": "text",
          "text": "Hanna was a beautiful girl but was very sad."
        }
      ]
    }
  ]
)

# print(completion.choices[0].message.content)
# print(type(completion.choices[0].message.content))

qna_list = completion.choices[0].message.content.split("\n")
# print(qna_list)
real_qna_list = qna_list[2:]
clean_lst = []
print("-------------------------------")
# print(real_qna_list)
for each in real_qna_list:
    cleaned_str = re.sub(r"\(.*?\)", "", each)
    without_white_spaces = cleaned_str.lstrip("  ")
    final_ques = without_white_spaces.replace("**","")
    clean_lst.append(final_ques)

print(clean_lst)