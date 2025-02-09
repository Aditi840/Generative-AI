#Importing Libraries


import langchain
import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
from langchain_groq import ChatGroq

length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

def main():
    st.title("LinkedIn Post Generator")
    col1, col2, col3 = st.columns(3)
    fs = FewShotPosts()
    with col1:
        selected_tag = st.selectbox("Title", options=fs.get_tags())

    with col2:
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        #Dropdown for language
        selected_language = st.selectbox("Language", options=language_options)


    if st.button("Generate"):
        post = generate_post(selected_length, selected_language, selected_tag)
        st.write(post)


#This function defines the main structure of a Streamlit-based LinkedIn Post Generator. It sets the title of the application and creates a three-column layout
#using st.columns(3), allowing users to select post attributes. The FewShotPosts class retrieves predefined post topics, which are displayed in a
#dropdown (st.selectbox) within the first column (col1). The second column (col2) allows users to choose the post length (Short, Medium, or Long), while the
#third column (col3) provides a language selection (English or Hinglish). Once the user makes their selections and clicks the "Generate" button,
#the generate_post() function is called with the selected parameters, generating and displaying the post using st.write().




if __name__ == "__main__":
    main()