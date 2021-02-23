from twython import Twython
from twython import TwythonStreamer

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            id = data['id']
            st.create_favorite(id=id)
            st.update_status(status='Nice Tweet @' + username, in_reply_to_status_id=id)
            print("https://twitter.com/" + username + "/status/" + str(id))

api_key = "###"
api_secret_key = "###"
access_token = "###"
access_secret_token = "###"

api = MyStreamer(api_key, api_secret_key, access_token, access_secret_token)
st = Twython(api_key, api_secret_key, access_token, access_secret_token)
keyword = input("Enter keyword to track: ")
api.statuses.filter(track=keyword)
