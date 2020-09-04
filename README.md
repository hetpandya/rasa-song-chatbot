# Rasa Song Chatbot

Original UI credits: [https://github.com/JiteshGaikwad/Chatbot-Widget](https://github.com/JiteshGaikwad/Chatbot-Widget).
I've modified the UI and added support for audio.

You can find the response format for audio in the docs [here](https://github.com/thehetpandya/rasa-song-chatbot/blob/master/docs/responses.md#audio)

Searches for your favourite song from [Soundcloud](https://soundcloud.com) and [Jiosaavn](https://jiosaavn.com) and plays it.

## Prerequisites
- Make sure you have a [Soundcloud API Key](https://developers.soundcloud.com/docs/api/guide). 
- Place your API key in `actions.py` in `self.client_ids` under `SongMachine` class.

## Usage
### Requirements
Install the required libraries using

`pip install -r requirements.txt`

### Rasa Model Training
- Make sure you download spacy model `en_core_web_md` using the following command

  `spacy download en_core_web_md` 

- Open terminal as root or as administrator depending upon your OS and run the following command

  `python -m spacy link en_core_web_md en_core_web_md`

- Train the model using

  `rasa train`

### Inference
Go the the chatbot directory

- Run Rasa actions server using

  `rasa run actions`

- Now, run Rasa API server using

  `rasa run -vv --model models --enable-api --cors "*"`

- Now, run the flask server using

  `python app.py`

Then go this url
http://localhost:8000

### Screenshot
![Screenshot](https://github.com/thehetpandya/rasa-song-chatbot/blob/master/images/screenshot.PNG?raw=true)
