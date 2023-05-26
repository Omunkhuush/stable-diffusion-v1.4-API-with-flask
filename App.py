from flask import Flask, render_template,request
from flask_mail import Mail, Message
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
import numpy as np

from dotenv import load_dotenv
import os 
load_dotenv('.env')
model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"

access_token = os.environ["access_token"]
MAIL_USERNAME = os.environ['MAIL_USERNAME']
MAIL_PASSWORD = os.environ['MAIL_PASSWORD']

pipe = StableDiffusionPipeline.from_pretrained(model_id, use_auth_token=access_token)
pipe = pipe.to(device)

#pipe.safety_checker = lambda images, clip_input: (images, False)
#print(pipe)
app = Flask(__name__)
DEBUG = True
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
@app.route('/')
@app.route("/home")
def home():
    return render_template("index.html")
promptContainer = []
@app.route("/search", methods=["POST", "GET"])
def search():
    name = ''
    output = request.form.to_dict()
    print(output)
    name = output['name']
    email = output['mail']
    print(email)
    if len(email) > 0:
        if promptContainer == []:
            print("none===")
            prompt = 'RANDOM'
        else:
            print(promptContainer[-1])
            prompt = promptContainer[-1]
        #print(promptContainer)
        print('prompt=',prompt)
        msg = Message('Your Imagination is here! ', sender = 'dmnlab2020@gmail.com', recipients = [email])
        msg.body = "Hello Sir/Madam, \r\nPlease enjoy the attached AI created image of your imagination from the keywords.\r\nPROMPT: "+prompt+"\r\nBest Regards, \r\n#UAEU #AI&RoboticsLab."
        with app.open_resource("./static/images/exp.png") as fp:
            msg.attach("./static/images/exp.png", "image/png", fp.read())
        mail.send(msg)
        print("done")
    if len(name) >0:
        promptContainer.append(name)
        with autocast("cuda"):
            image = pipe(name, guidance_scale=7.5).images[0]
        torch.cuda.empty_cache()
        image.save("./static/images/exp.png")
    filename = '../static/images/exp.png'
    return render_template("index.html", name=name, image=filename, mailTextstyle='display: none')
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
    #app.run(debug=True, port=5000)