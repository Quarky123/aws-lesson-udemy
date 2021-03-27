# heroku create iris-eda-app123
# git push origin main
# git push heroku main
# take note that its not master

import streamlit as st

def main():
    # simple EDA app
    st.title("Iris EDA App with streamlit")
    st.subheader("Streamlit is Cool")

if __name__ == '__main__':
    main()
