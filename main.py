from auto import auto_fav
from auto import auto_follow
from twitter_follow_bot import auto_rt 
from twitter_follow_bot import auto_follow_followers_for_user

#this is a sample program to use the auto.py script
auto_rt("funny", count=1)
auto_rt("omg", count=1)
auto_follow("funny", count=1)
auto_fav("funny", count=1)
