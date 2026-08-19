cd ~/Anon_bot
git pull origin main
pkill -9 -f python
nohup python3.13 main.py &