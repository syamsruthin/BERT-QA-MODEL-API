#All sklearn imports here

from flask import request
import os
from transformers import BertTokenizer, TFBertForQuestionAnswering
import tensorflow as tf
from q_a_api.endpoints import tokenizer,model

class q_a_model():
    def __init__(self):
        #Load all the saved models for prediction.Also load if there are any model created for preprocessing        
        self.tokenizer_qa = tokenizer
        self.model_qa = model


    def predict(self):
        print("Request data : ",request.json)
        question = request.json["question"]    
        doc = request.json["document"]
        
        #print("Document : ", doc)
        #print("Question : ", question)
        
        input_dict = self.tokenizer_qa(question, doc, return_tensors='tf')
        outputs = self.model_qa(input_dict)
        start_logits = outputs.start_logits
        end_logits = outputs.end_logits

        all_tokens = self.tokenizer_qa.convert_ids_to_tokens(input_dict["input_ids"].numpy()[0])
        answer = ' '.join(all_tokens[tf.math.argmax(start_logits, 1)[0] : tf.math.argmax(end_logits, 1)[0]+1])
        resp = {"Answer": answer}
        
        return  resp
        
    #More methods can be written for training/preprocessing the incoming record

        
