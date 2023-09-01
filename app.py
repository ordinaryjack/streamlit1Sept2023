import streamlit as st
import os
import openai

def process_text(file_path,api_key):
    result = "Thank you.  Total word count for your input file, original file and summary:"
    word_count = len(file_path.split())
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Summarize the following text in 100 words" + file_path
            }
        ]
    )
    summary=(response['choices'][0]['message']['content'])
   
    return result, file_path, word_count, summary
    # Your function logic here
    # Process the text file and return the output

# Streamlit app code
def main():
    """
    The main function is the entry point of the program. It displays a web interface using the Streamlit library, allowing users to upload a text file, process its contents, and display the output.

    :return: None
    """
    st.title("Demo to use OpenAI to Summarize Text, Jack Lau")

    # File input
    file = st.file_uploader("Upload a text file", type=["txt"])
    
    # Set up your OpenAI API credentials
    api_key = st.text_input('Enter a text string', 'Your API key here')
    st.write('Enter Your OpenAI API Key', api_key)
    st.button("Submit")
    
    if file is not None:
        # Read the file
        text = file.read().decode()

        # Process the text file
        output = process_text(text, api_key)
        
        # Display the output
        st.subheader("Original File and Number of Words")
        st.write(output[1])
        st.write(output[2])
        st.subheader("Summary by A.I.")
        st.write(output[3])

if __name__ == "__main__":
    main()
