#  NER-on-wikipedia-data

## _Problem statement:_   

1.  Scrap data using wikipedia API to perform NER
2.  Perform text pre-processing before named entity recognition
3.  Perform Named Entity Recognition on scrapped data and extract entities like city, person, organization, Date, Geographical Entity, Product etc.

## _Sample output:_

![img](https://user-images.githubusercontent.com/76241312/110232622-cbe1ab00-7f44-11eb-835a-c00bc1707927.png)

4. Display annotated text in Streamlit App and also display the occurrence of each label in a text in Bar graph form.
5. Implement token based authentication technique to secure API endpoints.
6. Please complete this assignment using Python & Flask. Feel free to use any Python packages as you see fit.
7. The code and API endpoint should be production ready and hosted somewhere in a publicly accessible location like on AWS, Heroku, PythonAnywhere, etc.

# **_NER-on-wikipedia-data-web-app_**

# Approach:

Here I am using spaCy and spacy_streamlit libraries to perform NER  on the extracted data.

* First will take the input from the user (i.e which they want to search on wikipedia).
* I extract these searched data from the wikipedia by using the wikipedia api wikipedia.page().text() function.
* These extracted data has many special charecters and sysmbols, so we need to perform the data pre-processing.
* I used the regular expressions to clean the data.
* In this project I used pre-trained "en_core_web_sm" spaCy model for performing NER on the extraceted data. It performed pretty well on the extracted data. 
* I displayed annoted text on the steramlit app.
* By using dframcy library, I stored these annoted text in the dataframe, this can be furthur used for visulization.
* For better understanding, I displayed the occurrence of each label in a text in Bar graph form.
* I deployed this project on Heroku. Here is the link [Click here](https://ner-on-wikipedia-data.herokuapp.com/). 


# Output:

The following are the results I got :

![Capture](https://user-images.githubusercontent.com/76241312/110234220-40b9e280-7f4f-11eb-8526-0b8a9d723dd1.PNG)
![Capture1](https://user-images.githubusercontent.com/76241312/110234269-837bba80-7f4f-11eb-9b7d-7a222eac5b66.PNG)
![Capture2](https://user-images.githubusercontent.com/76241312/110234271-88d90500-7f4f-11eb-8a47-182bd7560167.PNG)

**_Note_**:
 
 This task has done by keeping the time and computaional resource constraints in mind.
 
# --------------------------------------------------
 
 ## Thanks For Reading.           
 
 Get in touch  
 
  ### Gmail          [tarunguthi](https://mail.google.com/mail/?view=cm&fs=1&to=tarunguthi@gmail.com)
 
   ### linkedin     [TARUN G](https://www.linkedin.com/in/tarun-g-803408202)
   
   
 
Suggestions are welcome :)
