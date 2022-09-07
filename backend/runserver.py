# this is the config file that calls the server
# no functionality goes in here...
from app import app

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3001)
