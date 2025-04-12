import streamlit as st
from flask import Flask, jsonify

# Create a Flask app for the API
api = Flask(__name__)

@api.route('/hello')
def hello_api():
    return jsonify({"message": "Hello Sahan"})

# Streamlit UI
st.title("Hello World!")

# Run both apps
if __name__ == '__main__':
    import threading
    import os
    
    # Run Streamlit on port 8051
    def run_streamlit():
        os.system("streamlit run streamlit.py --server.port=8051")
    
    # Run Flask API on port 8052
    def run_flask():
        api.run(port=8052)
    
    t1 = threading.Thread(target=run_streamlit)
    t2 = threading.Thread(target=run_flask)
    
    t1.start()
    t2.start()