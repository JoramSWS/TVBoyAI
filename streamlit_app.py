from openai import OpenAI
import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def page_1():
    PROMPT_TEMPLATE = """
    
    Answer the question in an angry, impatient tone.  Be sarcastic.  Be a man from Texas.  You like dancing the hucklebuck: {question}

    """

    
    # Streamlit App
    htp="https://raw.githubusercontent.com/JoramSWS/TVBoyAI/main/ANDREW1.png"
    st.image(htp)
    query_text = st.text_input("Go for Andrew.")
    if not query_text:
        st.warning("I'm waiting, numb nuts.")
        return


    

    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(question=query_text)
    print(prompt)

    model = ChatOpenAI(
        model="gpt-3.5-turbo",
        model_kwargs={"top_p": 0.3},
        temperature=0.2
    )

    response_text = model.invoke(prompt)

    # Convert response_text to string
    response_text = str(response_text)

    # Extract text between "content=" and "response_metadata="
    start_index = response_text.find("content=") + len("content=")
    end_index = response_text.find("response_metadata=")
    formatted_response = response_text[start_index:end_index].replace("\\n\\n", "\n").strip()

    st.write(formatted_response)

def page_2():
    PROMPT_TEMPLATE = """
    
    Answer the question in a jocular tone.  Use clever wordplay.  Then explain the plot of the movie Juwanna Mann in detail: {question}

    """

    
    # Streamlit App
    htp="https://raw.githubusercontent.com/JoramSWS/TVBoyAI/main/CHRIS.png"
    st.image(htp)
    query_text = st.text_input("Go for Chris.")
    if not query_text:
        st.warning("And stop saying 'Hey Chris'.")
        return

    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(question=query_text)
    print(prompt)

    model = ChatOpenAI(
        model="gpt-3.5-turbo",
        model_kwargs={"top_p": 0.3},
        temperature=0.2
    )

    response_text = model.invoke(prompt)

    # Convert response_text to string
    response_text = str(response_text)

    # Extract text between "content=" and "response_metadata="
    start_index = response_text.find("content=") + len("content=")
    end_index = response_text.find("response_metadata=")
    formatted_response = response_text[start_index:end_index].replace("\\n\\n", "\n").strip()

    st.write(formatted_response)

PAGES = {
    "Channel 1: Andrew": page_1,
    "Channel 2: Chris": page_2
}

def main():
    htp="https://raw.githubusercontent.com/JoramSWS/TVBoyAI/main/TVBOY_logo.png"
    st.sidebar.image(htp)
    st.sidebar.title("Walkie Channels:")
    choice = st.sidebar.selectbox("Who do you need?", list(PAGES.keys()))
    #call the page function
    PAGES[choice]()

if __name__ == "__main__":
    main()
