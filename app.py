# -*- coding: utf-8 -*-
"""
Created on Fri May 28 17:53:10 2021

@author: Manish
"""
import openai
from fake_useragent import UserAgent
import streamlit as st
import pandas as pd
import streamlit.components.v1 as stc
#import key_config
pd.options.display.max_colwidth = 10000000000000

st.set_page_config(page_title="BYB", layout="wide", page_icon='🚀')

BYB = UserAgent()
header = {'User-Agent': str(BYB.chrome)}
openai.api_key = "sk-Jw8rIIoneOak8b6zQ6HU4V426SUZ5PmHtljimzAH"
      

def run():
    st.markdown("<h1 style='text-align: center; color: Black;'>Brand your Business with AI 🧠</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: Black;'>Made with ❤️ by Manish <a href='https://www.linkedin.com/in/manishkumarthota'><img src='data:image/png;base64,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', width='15', height='15'></a></a></h5>", unsafe_allow_html=True)
    st.subheader("Project is under development 🚧, further i will be adding StackGAN to synthsize the logo decsription into an image")
    
    company_name, headquarters_location, Industries = st.beta_columns(3)
    
     ## Company name

    company_name = company_name.text_input('Enter company name')

    ## Location

    headquarters_location = headquarters_location.text_input("Enter the location")

    ## Industry

    Industries = Industries.text_input("Enter the industry")
   
  
    #company_name = input("Input your company name：")
    #headquarters_location = input('Input the location of')
    #Industries = input('Input relevant industry for')
    
    #company_name = widgets.Text(value='kishen enterprises ltd', disabled=False,description='Name')
    #headquarters_location = widgets.Text(value='Tanzania', disabled=False,description='Location')
    #industries = widgets.Text(value='Business Supplies & Equipment', disabled=False,description='Industries')
    #display(company_name,headquarters_location,industries)
    
        
    if  st.button("Execute"):
        
        try:
            #graphics('index.html')
            
            #graphics('index.html', 0)
            myEntry = f"""Company's name:{company_name}\nHeadquaters location:{headquarters_location}\nIndustry:{Industries}"""
            
            #parameters
            myTokens = 600
            myEngine = "davinci"
            myTemp = 0.85
            myTop_p = 1
            myN=1
            myStream = None
            myLogProbs = None
            myStop = "\n\n"
            
            #Custom text input
            myPrompt = f"""Generates everything that a new business needs to get started connecting with their audience. 
            
            Company's name:Apple Computer Inc.
            Headquaters location:USA
            Industry: Computer hardware,Computer software,Consumer electronics,Cloud computing,Digital distribution,Fabless silicon design,Semiconductors,Media,Financial technology,Artificial intelligence
            Geographical focus:global
            Moto:make the best products
            Logo concept: an apple with a bite taken out of it. Black. No text.
            Suggested company colors: black and white
            Suggested company slogan:Think Different
            3 product ideas:portable music player, online music store, web application store
            1 free tweet: '''Apple Computer today unveiled its much-anticipated Macintosh computer, a sophisticated, affordably priced personal computer designed for business people, professionals and students in a broad range of fields.'''
            Geographic targets:United States, Canada, United Kingdom

            
            {myEntry}
            """
            
            response = openai.Completion.create(
              engine=myEngine,
              prompt=myPrompt,
              max_tokens=myTokens,
              temperature=myTemp,
              top_p=myTop_p,
              n=myN,
              stream = myStream,
              logprobs=myLogProbs,
              stop = myStop
            )
            
        
            
            result =  myEntry.split('\n') +  (response.choices[0].text).split('\n')
            Suggestion = []
            Results = []
            for i in result:
                Results.append(i.split(":")[0])
                Suggestion.append(i.split(":")[1])
                    
            df = pd.DataFrame({"Details":Results,"Results":Suggestion})
            st.table(df)
            #st.dataframe(data=df, width=1700, height=1768)
            
            
        
            
            
        except Exception as e:
            st.error("Something went wrong, please try once again!!")
            print(e)
          
    elif st.button("About"):
        st.header("What does this app do?")
        st.subheader("Branding your Business with AI is built on top of OpenAI's GPT-3 and streamlit framework, You need to give three inputs mentioned above and the AI suggests you the followings:")
        st.write("1. Company's name")
        st.write("2. Headquaters location")
        st.write("3. Industry")
        st.write("4. Geographical focus of the company.")
        st.write("5. Suggested motto for the company.")
        st.write("6. Logo concept")
        st.write("7. Suggested company colors.")
        st.write("8. Suggested company slogan.")
        st.write("9. Product ideas")
        st.write("10. Free tweets that can enhance your presence on twitter.")
        st.write("11. Geographic targets for the expansion of the company.") 
        
        

run()
