# edit-video
## Simple version
### Install Flask: 
```
pip3 install Flask
```

### Install moviepy: 
```
pip3 install flask-restful
pip3 install jupyterlab-pygments
pip3 install jupyter-client
pip3 install moviepy
```
### Install Imagemagick: 
```
sudo apt install imagemagick
```
### run: 
```
python app.py
```
## Docker version
### Build images
```
docker build -t tg3h/editvideo:1.0 .
```

### Run app
```
docker-compose up -d
```
