# Trillo
Trillo is a webpage app about booking hotel, ...


![](image.png)

Flexbox layouts.
### Venv: 
###### python3.9
```
python -m venv .venv && \
source .venv/bin/activate && \
pip install -U pip && \
pip install -r requirements.txt
```
### Run:
```
source .venv/bin/activate && \
export QUART_APP=app:app && \
export QUART_ENV=development && \
quart run -h "127.0.0.1" -p 5003
```
### Docker:
```
docker build -t app . && \
docker run -it --rm -p 5003:5003 app && \
docker rmi app --force
```
###### [Links:]()
+ ###### [Icons](https://icomoon.io/) 
