#! /usr/bin/env python3

from transformers import pipeline
import sys
import os

def answer(model, question, context):
    qa_model = pipeline("question-answering", model=model)
    a = qa_model(question = question, context = context)
    print(a['answer'])
    
def archive():
    path = os.path.abspath("context.txt")
    try:
        with open(path, 'r') as file:
            text = file.read()
            return text
    except Exception as e:
        print("Not found.")

def main(question):
    #model = "consciousAI/question-answering-roberta-base-s"
    #model = "distilbert-base-uncased-distilled-squad"
    model = "deepset/tinyroberta-squad2"
    
    context = archive()
    answer(model, question, context)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use: python qa.py <string_argument>")
    else:
        input_string = sys.argv[1]
        main(input_string) 