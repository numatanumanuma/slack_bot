import json
import os
import tweepy
import setting

class Observer:

    def __init__(self):
        token=setting.TW_TOKEN
        token_secret=setting.TW_TOKEN_SECRET
        consumer_key=setting.TW_CONSUMER_KEY
        consumer_secret=setting.TW_CONSUMER_SECRET
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(token, token_secret)
        self.tmp_path = setting.TMP_PATH
        self.screen_name = setting.SCREEN_NAME
        self.api = tweepy.API(auth)
        self.url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

    def getTimeline(self, count):
        """タイムラインを取得"""
        timeline = self.api.user_timeline(screen_name=self.screen_name, count=count)
        return timeline

    def getLatestTweet(self):
        """最新ツイート情報を取得"""
        timeline = self.getTimeline(1)
        return timeline[0]

    def checkUpdate(self):
        """
        前回チェックしたときの最新ツイートはlatestTweetに保存
        前回の最新ツイートと今の最新ツイートを比べる
        もっといい変数名を...
        """
        with open(self.tmp_path, encoding='utf-8') as f:
            latest_tweet = f.read()

        status = self.getLatestTweet()
        now_tweet = status.text

        # リツイートはスルー
        if latest_tweet != now_tweet and now_tweet[:2] != 'RT':
            with open(self.tmp_path, 'w', encoding='utf-8') as f:
                f.write(now_tweet)
            return True
        else:
            return False

    def makeComment(self):
        """
        投稿用のテキストを生成
        分離予定
        """
        status = self.getLatestTweet()
        comment = status.text
        index = comment.find('https://t.co/')
        comment = comment[:index]
        # 画像が付いていると二重になってしまうため画像のurlを削除
        comment += '\nhttps://twitter.com/' + self.screen_name + '/status/' + status.id_str
        print(comment)
        return comment
