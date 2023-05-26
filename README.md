# Stable-Diffusion-v1.4-API-with-Flask

# Description 

This project generates what people want to see using a stable diffusion model and can send it to their email.

# Installation 

**1. Download repository**
```
git clone https://github.com/Omunkhuush/stable-diffusion-v1.4-API-with-flask.git
```
**2. Install the Pytorch version that matches your Cuda version from [Pytorch all release](https://pytorch.org/get-started/previous-versions/).**

**3. Install requirements** 
```
cd stable-diffusion-v1.4-API-with-flask
pip install -r requirement.txt
```

# Get access token from Hugging face

1. Sign up and Sign in to [Hugging face](https://huggingface.co/)
2. Click to **Profile** --> **Settings** --> **Access Tokens**
3. click to  **New token** 
    - Give it the name you want
    - set role to write
    - Copy the generated access token

<p align="center" width="100%">
    <img width="100%" src="https://github.com/Omunkhuush/stable-diffusion-v1.4-API-with-flask/assets/73123564/5fe6f590-3021-4408-8537-0e045e198129">
</p>

# Get App password from Google

1. Clict to [**Manage your Google Account**](https://myaccount.google.com/) on the browser.
2. Click to **Settings**
3. Turn on 2-Step Verification
4. Scroll down and click to **App passwords**
   - set  **Select app** to **other (_custom name_)**
   - Give it the name you want
   - Copy the generated App password

<p align="center" width="100%">
    <img width="100%" src="https://github.com/Omunkhuush/stable-diffusion-v1.4-API-with-flask/assets/73123564/d05bb6b1-3a3d-420d-8e0a-1178ce1c3d0e">
</p>

# Edit .env file. 
**After obtaining the access tokens, make the necessary changes to the env file.**

<p align="center" width="100%">
    <img width="100%" src="https://github.com/Omunkhuush/stable-diffusion-v1.4-API-with-flask/assets/73123564/8834bb6f-b8aa-40a2-bf39-2cf70b1f52e0">
</p>

# Run WebApp
```
python App.py
```
![runStable](https://github.com/Omunkhuush/stable-diffusion-v1.4-API-with-flask/assets/73123564/ccfb760c-9860-4292-a963-b3c8fc065c2a)
![runStable2](https://github.com/Omunkhuush/stable-diffusion-v1.4-API-with-flask/assets/73123564/61b9dc32-2699-4db4-8aca-4042fc08535e)

# Test 

https://github.com/Omunkhuush/stable-diffusion-v1.4-API-with-flask/assets/73123564/63a2c476-e80d-4a5a-bf51-51563d0230ad


