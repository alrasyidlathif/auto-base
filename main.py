import config
import service
import time

api = service.init(config.api_key, config.api_secret, config.access_token, config.access_secret)

def autobase(api, config):
    while True:
        add=0
        messages = service.get_dm(api, config.num_dm)
        print('get ' + str(len(messages)) + ' dm')

        for msg in messages:
            text = msg.message_create['message_data']['text']
            print('received dm: ' + text)
            valid = service.is_valid(text, config.keyword, config.text_length)

            if (valid):
                res = service.tweeting(api, text)
                print('tweeting: ' + str(res))
                add+=1

            res = service.delete_dm(api, msg.id)
            print('delete dm: ' + str(res))

        time.sleep(config.time_sleep)
        time.sleep(add*config.add_time_sleep)

if __name__ == "__main__":
    autobase(api, config)
