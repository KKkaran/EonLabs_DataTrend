# this is the main file containing all the routes and resources and also the instance 
# of the app server which, however, gets called in the 'runserver.py' file
from flask import Flask
from pytrends.request import TrendReq
from matplotlib.pyplot import plot,show

app = Flask(__name__)
pytrends = TrendReq(hl='en-US')#hl --> host language

#built payload
kw_list = ["Elon Musk"]
pytrends.build_payload(kw_list, 
                        cat='0',
                        timeframe='today 5-y',
                        geo='',
                        gprop='')         

data = pytrends.interest_over_time()
mean = round(data.mean(),2) #how volatile is the trend i.e 5 year avearge of interest
avg = round(data['Elon Musk'][-52:].mean(),2) #last year average of interest
avg2 = round(data['Elon Musk'][:52].mean(),2) #yearly average of last 5 years ago
trend = round(((avg/mean['Elon Musk'])-1)*100,2)

plot(data)
show()
#print(data)
#print("srk :----------------> " + str(mean["Elon Musk"]))
#print("The avg 5 years interest of Elon Musk was " + str(mean['Elon Musk']) + ".");
#print("The last year interest of Elon Musk " + " compared to the last 5 years has chnaged by " + str(trend) + "%.")
#print(avg2)
#print(avg)

@app.route("/home")
def home():
    return "testing route..."

