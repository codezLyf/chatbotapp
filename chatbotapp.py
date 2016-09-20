from flask import Flask, request
import json
import requests

app = Flask(__name__)

# This needs to be filled with the Page Access Token that will be provided
# by the Facebook App that will be created.
access_token = ''

@app.route('/', methods=['GET'])
def handle_verification():
  print "Handling Verification."
  if request.args.get('hub.verify_token', '') == 'verify_token':
    print "Verification successful!"
    return request.args.get('hub.challenge', '')
  else:
    print "Verification failed!"
    return 'Error, wrong validation token'


@app.route('/',methods=['POST'])  ## Webhook to receive all messages sent by the user to chatbot
def webhook():

	data = request.get_json()
	print data

	if data['object'] == "page":

		for entry in data['entry']:
			
			for messaging_event in entry['messaging']:

				if messaging_event.get("message"):

					## put code to process your incoming text message
					pass

				if messaging_event.get("delivery"):
					## code to process delivery related process
					pass

				if messaging_event.get("optin"):
					pass

				if messaging_event.get("postback"):

					## All the postback callbacks to be handles here
					pass
	return "ok"



if __name__ == '__main__':
	app.run()