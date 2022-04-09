import requests
from flask import *
from flask import jsonify
from apiclient.discovery import build
app = Flask(__name__)
@app.route('/youtube/search/',methods=['GET'])
def main():
    text = str(request.args.get("text"))
    maxresults = int(request.args.get("maxresults"))
    key = "AIzaSyC4RYlY8-1-taaTly3VHnccVCGa6WC5nv8"
    y = build('youtube',"v3",developerKey=key)
    req = y.search().list(q=text,part="snippet",type="video",maxResults=maxresults)
    r = req.execute()
    list_video = []
    for i in range(maxresults):
        data = {"video_"+str(i+1):r["items"][i]["snippet"]}
        list_video.append(data)
    return jsonify(list_video)
if __name__ == '__main__':
  app.run()