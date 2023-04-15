# airai
Air Quality AI that is using LangChain LLMS & OpenAI models to respond to the user's query.

Framework:
-  LangChain is a framework for developing applications powered by language models. 
-  Flask

## Backend Installation
Run the following command:
```
cd server
```

#### Install Virtual Environment
Make sure that you are in the server folder and run:
```
python3 -m venv venv 
```
Activate the venv
```
. venv/bin/activate # for Linux
venv\Scripts\activate # for Windows
```


#### Install requirements
After is created your virtual environment, then run the following command:
```
pip install -r requirements.txt
```

### Setup environment variable

Then run this command:
```
cp .env.example .env
```

In the .env file, you need to set:
```
OPENAI_API_KEY="your-api-key"
OPENAI_MODEL="your-model" # text-davinci-002, text-ada-002 etc..
```

### RUN Project:
```
export FLASK_APP=app
flask run
```

Usually the project run on link: http://127.0.0.1:5000

The endpoint that will be called is api/air_quality

## Frontend Installation

Go to client folder
```
cd client
```

Install packages by running following command:
```
npm i 
```

Run the project after successfull installation:
```
npm run serve
```


