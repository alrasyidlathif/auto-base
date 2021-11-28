import tweepy

def init(api_key, api_secret, access_token, access_secret):
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

def get_dm(api, num_dm):
    messages = api.get_direct_messages(count=num_dm)
    messages.reverse()
    return messages

def is_valid(text, keyword, text_length):
    if len(text) > text_length:
        return False
    if text[:3].lower() != keyword:
        return False
    return True

def delete_dm(api, id):
    try:
        api.delete_direct_message(id)
        return True
    except Exception as e:
        print(e)
        return False

def tweeting(api, tweet):
    try:
        api.update_status(tweet)
        return True
    except Exception as e:
        print(e)
        return False
