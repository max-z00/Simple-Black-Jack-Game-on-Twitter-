'''
Author: max_z00
Title: Twitter BlackJack Bot
Date Creation: 8/19/2022
Notes:
    This thing looks like shit not gonna lie lol

'''

#import libs
from os import access
from array import array
from unittest import result
from numpy import *
import time
import random
import tweepy

#api keys
consumer_key = "Enter Info"
consumer_secret = "Enter Info"
access_token = "Enter Info"
access_token_secret = "Enter Info"

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
# set access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret)
  
# calling the api 
api = tweepy.API(auth)

#This is def some spaghetti code lol
def ascii_gen(value):
    asciiDeck = array(["🅰️", "2⃣", "3⃣","4⃣","5⃣","6⃣","7⃣","8⃣", "9⃣","🔟","🤴","👸","👑","👑",999])
    if(value == 11 or value == 1):
        return asciiDeck[0]
    if(value == 2):
        return asciiDeck[1]
    if(value == 3):
        return asciiDeck[2]
    if(value == 4):
        return asciiDeck[3]
    if(value == 5):
        return asciiDeck[4]
    if(value == 6):
        return asciiDeck[5]
    if(value == 7):
        return asciiDeck[6]
    if(value == 8):
        return asciiDeck[7]
    if(value == 9):
        return asciiDeck[8]
    if(value == 10):
        randomValue = random.randint(9,13)
        return asciiDeck[randomValue]
    if(value == 999):
        return ""


        
    
def main():

    #Card Deck
    cardDeck = array([1,2,3,4,5,6,7,8,9,10])

    #cardDeck = array([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10])
    

    #Generate Computer Hand
    print("Generate Computer Hand\n")
    pc = computer(cardDeck.copy())
    #Generate twitters Hand
    print("Generate Twitters Hand\n")
    users = twitterPlayers(cardDeck.copy())

    #FIrst update
    print("Sending first_update: \n")
    first_update = "Black Jack B0T Hand: " + str(pc[1] + pc[2]) + " \t  BOT Total: "+ str(pc[4]) + "\nTwitters Hand: " + str(users[1] + users[2]) + "\t  Twitters Total: " + str(users[0]) + "\n\nHIT \tOR \tSTAY\n\n\n Checking in 5 Minutes. \n#blackjack"
    api.update_status(first_update)
    #Set a Timer    
    time.sleep(300)
    getTweetID()
    retweetCount = counter()
    likeCount = counter()
    if(pc[3] == 999):
        pc[3] = 0
    if(retweetCount[0] < likeCount[1]):
        print("Sending sec_update: \n")
        sec_update = "Twitter Draws A Card!\n\nBlack Jack B0T Hand: " + str(pc[1] + pc[2] + pc[3]) + " \t  BOT Total: "+ str(pc[0]) + "\nTwitters Hand: " + str(users[1] + users[2] + users[3]) + "\t  Twitters Total: " + str(users[4]) + "\n\nHIT \tOR \tSTAY\n#blackjack"
        resultVal = users[4]
        pcVal = pc[0]
        api.update_status(sec_update)
    if(retweetCount[0] > likeCount[1] or retweetCount[0] == likeCount[1]):
        print("Did Not Send sec_update:\n")
        #sec_update = "Twitter Stays!\n\nBlack Jack B0T Hand: " + str(pc[1] + pc[2] + pc[3]) + " \t  BOT Total: "+ str(pc[0]) + "\nTwitters Hand: " + str(users[1] + users[2]) + "\t  Twitters Total: " + str(users[0]) + "\n\nHIT \tOR \tSTAY"
        resultVal = users[0]
        pcVal = pc[0]
        b0tWins = 0
        twitterWins = 0
    if(resultVal > 21 and pcVal <= 21):
        b0tWins = + 1
        third_update = "B0T WINS!!!: \n\nBlack Jack B0T Hand: " + str(pc[1] + pc[2] + pc[3]) + " \t  BOT Total: "+ str(pcVal) + "\nTwitters Hand: " + str(users[1] + users[2]) + "\t  Twitters Total: " + str(resultVal) + "\n\nWill Start Again In 15 Minutes. \nB0T Wins: " + str(b0tWins) + "\nTwitter Wins: " + str(twitterWins) + "\n#blackjack"
    if(pcVal > 21 and resultVal <= 21):
        twitterWins = + 1
        third_update = "Twitter Wins!!!:\n\nBlack Jack B0T Hand: " + str(pc[1] + pc[2] + pc[3]) + " \t  BOT Total: "+ str(pcVal) + "\nTwitters Hand: " + str(users[1] + users[2]) + "\t  Twitters Total: " + str(resultVal) + "\n\nWill Start Again In 15 Minutes.\nB0T Wins: " + str(b0tWins) + "\nTwitter Wins: " + str(twitterWins) + "\n#blackjack"
    if(pcVal > 21 and resultVal > 21):
        third_update = "Busted!!!:\n\nBlack Jack B0T Hand: " + str(pc[1] + pc[2] + pc[3]) + " \t  BOT Total: "+ str(pcVal) + "\nTwitters Hand: " + str(users[1] + users[2]) + "\t  Twitters Total: " + str(resultVal) + "\n\nWill Start Again In 15 Minutes.\nB0T Wins: " + str(b0tWins) + "\nTwitter Wins: " + str(twitterWins) + "\n#blackjack"
    if(pcVal > resultVal):
        b0tWins = + 1
        third_update = "B0T WINS!!!:\n\nBlack Jack B0T Hand: " + str(pc[1] + pc[2] + pc[3]) + " \t  BOT Total: "+ str(pcVal) + "\nTwitters Hand: " + str(users[1] + users[2]) + "\t  Twitters Total: " + str(resultVal) + "\n\nWill Start Again In 15 Minutes.\nB0T Wins: " + str(b0tWins) + "\nTwitter Wins: " + str(twitterWins) + "\n#blackjack"
    if(pcVal < resultVal):
        twitterWins = + 1
        third_update = "Twitter Wins!!!:\n\nBlack Jack B0T Hand: " + str(pc[1] + pc[2] + pc[3]) + " \t  BOT Total: "+ str(pcVal) + "\nTwitters Hand: " + str(users[1] + users[2]) + "\t  Twitters Total: " + str(resultVal) + "\n\nWill Start Again In 15 Minutes.\nB0T Wins: " + str(b0tWins) + "\nTwitter Wins: " + str(twitterWins) + "\n#blackjack"
    print("Sending third_update: \n")
    api.update_status(third_update)
    
    #reapeat


#bot
def computer(computerdeck):
    #lets shuffle the cards
    random.shuffle(computerdeck)
    #initialize variables
    randomValue  = random.randint(0,13) 
    i = 999
    asciiCard_3 = ascii_gen(i)
    card_result = 0
    card_1 = computerdeck[0]
    card_2 = computerdeck[1]




    #Make these 1's turn into 11's 
    if(card_result <= 10):
        if(card_1 == 1):
            card_1 = 11
        if(card_2 == 1):
            card_2 = 11
      #result of hand
    card_result = card_1 + card_2
    temp_result = card_result
    asciiCard_1 = ascii_gen(card_1)
    asciiCard_2 = ascii_gen(card_2)
    
#    While this may seem weird I think it allows more random choices to be done by a computer
#    After playing around with it for awhile the closer RandomValue is <= == 21 makes it easier to 
#    always win. 
    while(card_result <= randomValue):
        i = 2
        i = computerdeck[i]
        asciiCard_3 = ascii_gen(i)
        card_result = card_1 + card_2 + i
    
    #Return card hand result
    return card_result, asciiCard_1, asciiCard_2, asciiCard_3,temp_result     

#twitter Player
def twitterPlayers(humanDeck):
    #Randomize Deck again!!!
    random.shuffle(humanDeck)
    card_1  = humanDeck[0]
    card_2  = humanDeck[1]
    card_3  = humanDeck[2]
    card_result = card_1 + card_2
    #Automaticaly update the card if it is an ACE
    if(card_result <= 10):
        if(card_1 == 1):
            card_1 = 11
        if(card_2 == 1):
            card_2 = 11
    #Generate symbol for card
    asciiCard_1 = ascii_gen(card_1)
    asciiCard_2 = ascii_gen(card_2)
    asciiCard_3 = ascii_gen(card_3)
    #Result
    card_result1 = card_1 + card_2
    card_result2 = card_1 + card_2 + card_3
    #Return Value of Cards
    return card_result1, asciiCard_1, asciiCard_2,asciiCard_3,card_result2


'''
Function that returns the recent Tweet ID,
also Prints some information, such as ID of Tweet, Date/Time, What the tweet is. 
please change line 195 to your @username

'''
def getTweetID():
    #get userID
    userID = "Enter twitter handle!"
    tweets = api.user_timeline(screen_name=userID,
    # 200 is the maximum allowed count
    count=1,
    include_rts = False,
    # Necessary to keep full_text 
    # otherwise only the first 140 words are extracted
    tweet_mode = 'extended')

    #pull the tweet info
    for info in tweets[:3]:
        print("ID: {}".format(info.id))
        id = info.id
        print(info.created_at)
        print("\n")

    #Return Tweet ID
    return id
    
def counter():
    id = str(getTweetID())
    status = api.get_status(id, tweet_mode = "extended")
    # fetching the retweet_count attribute
    retweet_count = status.retweet_count 
    # fetching the favorite_count attribute
    favorite_count = status.favorite_count
    print("The number of time the status has been retweeted is : " + str(retweet_count) + "\nThe number of time the status has been liked is : " + str(favorite_count)) 
    return retweet_count, favorite_count


if __name__ == '__main__':
    i = 0
    while(True):
        main()
        i = + 1
        print("\n\nThe Jack Black B0T has ran a total of: " + str(i) + " Times\n\n")
        time.sleep(900)
