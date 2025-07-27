git clone https://github.com/Web4application/kubuverse.git
cd kubuverse
docker-compose up --build

git clone https://github.com/Web4application/script_analyzer_bot.git
cd script_analyzer_bot
pip install -r requirements.txt


## Running the API

uvicorn app.main:app --reload
http://127.0.0.1:8000/docs

git add --all
git commit -m "Initial commit"
git push -u origin main

---
## ✅ Now Create GitHub Repo

Here’s what to do:

```bash
git init
git add .
git commit -m "Initial commit: Script Analyzer Bot 💻"
git commit -m "Added files from phone"
gh repo create personal-script-analyzer-bot --public --source=. --remote=origin
git push -u origin main
