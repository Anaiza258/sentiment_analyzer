import openai
import streamlit as st


# Set the API key for OpenAI
openai.api_key ='YOUR API KEY HERE'
def get_response_from_chatgpt(text):
    prompt = f"Identify and return the sentiment either positive or negative in given text. text : {text}"
    response= openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
       
        messages = [{"role":"system" , "content":"You are a helpful sentiment analyzer that returns concise sentiment"},
                    {"role":"user", "content":prompt},
                    {"role": "assistant", "content": "Please analyze the sentiment of the text."}
        
        ],
        temperature = 0.1
    )
    sentiment = response['choices'][0]['message']['content']
    return sentiment

#use streamlit
st.title("Sentiment Analyzer")
model = 'gpt-3.5-turbo',
text = st.text_input("Enter text: ")

if st.button('Submit'):
    with st.spinner('OpenAI processing in Progress'):
        sentiment = get_response_from_chatgpt(text)
        st.success('OpenAI processing  complete')

        st.write(f"Sentiment:{sentiment}")
