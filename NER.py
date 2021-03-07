#Importing required libraries

import wikipediaapi
import streamlit as st
import spacy
from spacy_streamlit import visualize_ner
import re
from dframcy import DframCy


st.title("NER on Wikipedia data") #Title 

topic = st.text_input("Enter the topic you want to search", "tarun")  #user input

wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI      # choose English as language and format is wiki
)                                      

data = (wiki.page(topic).text) # Extract wikipedia page whole text data 

#data = """Mahendra Singh Dhoni, is a former Indian international cricketer who captained the Indian national team in limited-overs formats from 2007 to 2017 and in Test cricket from 2008 to 2014."""

#Text Pre-processing

data = re.sub('[^a-zA-Z0-9 \n\.]', ' ', data) # substitute all the special charecters symbols with a space

data = re.sub(r'\s+'," ", data)

#data = data.lower()  # lowering the words


nlp = spacy.load("en_core_web_sm")   #load the pre trained model

doc = nlp(data)  #applying the package on the data

visualize_ner(doc, show_table= True ,labels=nlp.get_pipe("ner").labels) #visualize NER on data

st.success("Success")  

dframcy = DframCy(nlp)  

token_annotation_dataframe, entity_dataframe = dframcy.to_dataframe(doc, separate_entity_dframe=True)  #to dataframe

st.subheader("Bar chart for occurrence of each label in a text") # Subheader 

st.bar_chart(entity_dataframe['ent_text'])  #Bar chart for annoted text
