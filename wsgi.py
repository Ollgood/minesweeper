""" This file needed for heroku, PORT is a heroku var """
from main import application

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=PORT, ssl_context='adhoc')
