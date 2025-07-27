git clone https://github.com/Web4application/kubuverse.git
cd kubuverse
docker-compose up --build

git clone https://github.com/Web4application/script_analyzer_bot.git
cd script_analyzer_bot
pip install -r requirements.txt


## Running the API

uvicorn app.main:app --reload
http://127.0.0.1:8000/docs
