import argparse, os, logging, datetime, arrow
import tweepy

logging.basicConfig(format='[%(asctime)s] - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)

class TwitterDevLabs:
    def __init__(self):
        self.consumer_key = os.environ.get('TW_CONSUMER_KEY')
        self.consumer_secret = os.environ.get('TW_CONSUMER_SECRET')
        self.access_token = os.environ.get('TW_ACCESS_TOKEN')
        self.access_secret = os.environ.get('TW_ACCESS_SECRET')

    def configure_api(self):
        """ Configure Tweepy API """
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)
        try:
            api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
            api.verify_credentials()
        except tweepy.RateLimitError as rle:
            logger.warn("{0}: {1}".format(rle.reason, rle.response))
            raise Exception(rle.response)
        except tweepy.TweepError as te:
            logger.warn("{0}: {1}".format(te.reason, te.response))
            raise Exception(te.response)
        logger.info("Authentication OK!")
        return api

    def post_tweet(self, status):
        """ Post status update for the authenticated user """
        status_text = str(status)
        status_len = len(status_text)
        if status_len > 0 and status_len <= 280:
            api = configure_api()
            response_status = api.update_status(status_text, trim_user=True)
            logger.info(response_status.json_payload)
        else:
            logger.error("Your status update was either more than Twitter's 280 character limit or you didn't specify any text.")
            raise IndexError

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Updates the authenticating user\'s current status, also known as Tweeting.')
    parser.add_argument('--status', metavar='status', type=str, help='The text of your status update.')
    # parser.add_argument('--', metavar='', type=str, help='')
    # parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')

    client = TwitterDevLabs()
    args = parser.parse_args()
    print(args.status)
    client.post_tweet(args.status)
