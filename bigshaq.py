from time import sleep
from model import Model
from six.moves import cPickle
import os
import tensorflow as tf

import tweepy
from tweepy.streaming import StreamListener
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
with open(os.path.join('save/bigshaq', 'config.pkl'), 'rb') as f:
    saved_args = cPickle.load(f)
with open(os.path.join('save/bigshaq', 'words_vocab.pkl'), 'rb') as f:
    words, vocab = cPickle.load(f)
model = Model(saved_args, True)
sess = tf.Session()
tf.global_variables_initializer().run(session=sess)
saver = tf.train.Saver(tf.global_variables())
ckpt = tf.train.get_checkpoint_state('save/bigshaq')

def generateTweet():

 if ckpt and ckpt.model_checkpoint_path:
     saver.restore(sess, ckpt.model_checkpoint_path)
     printwords = model.sample(sess, words, vocab, 140, '', 200, 1, 4)
     return printwords
i=1
while i<1000000:
    s=generateTweet()
    api.update_status(s[:280])
    sleep(1000)
