
# Twitter Mass Follow

This is a simple Python script that follows everyone a Twitter user/users are following. Just clone the repo, provide the API keys and run the script. This is a very specific use case because I was tired of following interesting people manually, so I just picked an interesting account and let the script do the work. Gotta go curate my feed now bye!

**Note:** Twitter has restricted the number of people you can follow in a day to 400 for unverified accounts and 1000 for verified accounts.


## Installation 

**1**: Clone the repo.

**2** (Optional): Set up a virtual environment.

**3**: `pip install requirements.txt`

**4**: I didn't push my API keys so you gotta get yours. [Here's how](https://developer.twitter.com/en/docs/labs/covid19-stream/quick-start#:~:text=Navigate%20to%20your%20app%20dashboard,API%20secret%20key%20into%20consumer_secret.).

**5**: Replace `your-key` with your keys. Type this in your terminal:

```bash
export CONSUMER_KEY="your-key"
export CONSUMER_SECRET="your-key"
export ACCESS_TOKEN="your-key"
export ACCESS_TOKEN_SECRET="your-key"
```

**6**: Run script by providing the user name/names of the person you want to steal the feed of as arguments:
```bash
python main.py username1 username2
```
