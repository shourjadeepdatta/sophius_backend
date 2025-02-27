from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from helpers import call_generative_function
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change this in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

class Question(BaseModel):
    no_of_questions : str
    input_paragraph : str


@app.post("/generate_questions")
def generate_questions(req_body : Question):
    print(type(req_body))
    if not req_body:
        return JSONResponse(content = {"No request body found"},status_code = 400)
    
    if not req_body.input_paragraph:
        return JSONResponse(content={"message":"paragraph missing in the payload","status":"fail"},status_code=400)
    if not req_body.no_of_questions:
        return JSONResponse(content={"message":"number of questions is missing in the payload","status":"fail"},status_code=400)
    
    try:
        qna_list = call_generative_function(req_body.input_paragraph,req_body.no_of_questions)
    except Exception as e:
        print("Some problem while calling the generative function",str(e))
        return JSONResponse(content={"message":"Could not generate qna list,please connect after some time","error":str(e),"status":"fail"},status_code = 500)
    

    return JSONResponse(content = {"message":"Questions generated successfully","ques_list":qna_list,"status":"success"},status_code = 200)