#!flask/bin/python
from flask import Flask
from flaskrun import flaskrun
from flask import render_template
from flask import request
import urllib.request
from image_recognizer import recognize_image

application = Flask(__name__, static_folder='../static', template_folder='../templates')

def save_img(img_url):
   img_file = str(application.static_folder +'/'+ 'user_img.jpg')
   img_data=urllib.request.urlretrieve(img_url, img_file)
   # with open(img_file, 'wb') as handler:
   #    handler.write(img_data)
   return img_file

@application.route('/', methods=['GET'])
def get():
   return render_template('index.html')


@application.route('/', methods=['POST'])
def post():
   img_url = request.form['img_name']
   img_file = save_img(img_url.lower())
   answer = recognize_image(img_file)
   return str(answer)

if __name__ == '__main__':
    flaskrun(application)
