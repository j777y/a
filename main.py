from auto import auto_fav
from twitter_follow_bot import auto_rt 
from twitter_follow_bot import auto_follow_followers_for_user

#this is a sample program to use the auto.py script
auto_rt("funny", count=10)
auto_rt("lol", count=10)
auto_rt("omg", count=10)
auto_fav("teamfollow", count=1)
auto_fav("teamfollowback", count=1)
auto_follow_followers_for_user(influentialtwit, count=100)
