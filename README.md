This repo consists of the wrapper api which will generate questions based on the paragraph typed by the user from the frontend
Also the number of questions can be entered by the user from the UI
This is made in FastAPI
For validation a Model was setup using the Pydantic base model and a simple fastapi route was made out of it. Code level exception handling is also done to return appropriate responses.
It accepts only 2 fields -> number of questions and paragraph about which we want to generate the questions.

For testing this out just pull the latest code and perform these steps:
1. pip install -r requirements.txt
2. uvicorn app:app --host 0.0.0.0 --port 3001 --reload

I am also attaching the curl for the api:

curl --location 'http://localhost:3001/generate_questions' \
--data '{
    "no_of_questions":"3",
    "input_paragraph":"Hanna was a beautiful girl but was very sad."
}'

