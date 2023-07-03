# Bitly URL shortener

This is a python script. The script is based on API bitly.com service. It helps either to create a short link or to show amount of clicks on betly’s link.

## How to install

It needs an API key for using a bitly’s service. Sign up the [bitly’s service](https://bitly.com/) Then create `GENERIC ACCESS TOKEN` on [bitly integrations](https://app.bitly.com/settings/integrations/)

After all, create `.env` file in the root directory of the script. Put token on `.env` file as `BITLY_API_KEY=EXAMPLE_TOKEN`
Python3 should already be installed. Use pip (or pip3, if there is a conflict with Python2) to install dependencies:

`pip install -r requirements.txt`

## How to use

Run the script with URL to get a shot link 

`python main.py www.example_url.com`

Run the script with bily’s link to see amount of clicks

`python main.py bit.ly/example`

## Project Goals

This code was written for educational purposes as part of an online course for web developers at dvmn.org.
