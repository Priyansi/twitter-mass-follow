import tweepy
import os
import time
import argparse


def create_api():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    api.verify_credentials()
    return api


def mass_follow(api, user):
    for friend in tweepy.Cursor(api.friends, user).items():
        if not friend.following:
            try:
                friend.follow()
            except:
                print("An error occured while trying to follow ",
                      friend.screen_name)

            time.sleep(5)


def main():
    api = create_api()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-u", "--users", nargs="+", help="usernames of users whose following you want to mass follow")
    args = parser.parse_args()
    for user in args.users:
        try:
            mass_follow(api, user)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
