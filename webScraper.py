import twitter
import tensorflow as tf
import numpy as np
import math
import heapq
from tensorflow import keras
from tensorflow.keras import layers
import functools


api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret=''
                  )

# note, username can be either a twitter name or user id


def getFollowers(username):
    return

# returns Status instances


def getLikes(username):
    likeMessages = []
    count = 0
    listOfLikes = api.GetFavorites(screen_name=username)
    return listOfLikes


def populateUser(id, username):
    user = api.GetUser(screen_name=username)
    #followers = api.GetFollowers(screen_name = username)
    followercount = user.followers_count
    friendcount = user.friends_count
    favoritecount = user.favourites_count
    statuscount = user.statuses_count
    #likes = getLikes(username)
    #friends = api.GetFriends(screen_name = username)
    #statuses = api.GetUserTimeline(screen_name = username)
    #count = 0
    # for i in statuses:
    #	replies[count] = api.GetReplies(i)
    #	count = count+1
    userinfo = [user, followercount,
                favoritecount, friendcount, statuscount, 0]
    return userinfo


def populateUserJay(id, username):
    user = api.GetUser(screen_name=username)
    followers = api.GetFollowers(screen_name=username)
    friendcount = user.friends_count
    favoritecount = user.favourites_count
    statuscount = user.statuses_count
    likes = getLikes(username)
    friends = api.GetFriends(screen_name=username)
    statuses = api.GetUserTimeline(screen_name=username)
    #count = 0
    # for i in statuses:
    #	replies[count] = api.GetReplies(i)
    #	count = count+1
    userinfo = [user, followers, likes, friends, statuses, 0]
    return userinfo


def main():
    print("Building neural network....")
    reallist = []
    tempj = "j_vanv"
    j = populateUserJay(0, "j_vanv")
    temp = j[3][1]
    tempname = temp.screen_name
    # print(j[0])
    for i in range(len(j[3])):
        temp = j[3][i]
        tempname = temp.screen_name
        reallist.append(tempname)

    toTrainreg = []
    count = 0

    flagsreg = []
    botslist = ["dbd04066", "seasonedcases", "avkashk", "alejandronw", "kneuman",
                "threatintelbot", "JeremieRykner", "slomogoldfish",  "MrLucasBryant", "bitcointrackers"]
    for uname in reallist:
        templist = populateUser(0, uname)
        toTrainreg.append([templist[1], templist[2], templist[3], templist[4]])
        #np.append(toTrainreg, templist)
        #np.append(flagsreg, 0)
        if count % 3 == 0:
            flagsreg.append(0)
        if count % 3 == 1:
            flagsreg.append(1)
        if count % 3 == 2:
            flagsreg.append(2)
        count = count+1
    count = 0
    for uname in botslist:
        #print(uname)
        templist = populateUser(0, uname)
        toTrainreg.append([templist[1], templist[2], templist[3], templist[4]])
        if count % 3 == 0:
            flagsreg.append(10)
        if count % 3 == 1:
            flagsreg.append(9)
        if count % 3 == 2:
            flagsreg.append(8)
        count = count + 1
    toTrain = np.array(toTrainreg)
    flags = np.array(flagsreg)
    #print(toTrain)
    #print(flags)

    model = keras.Sequential([
        #keras.layers.Embedding(1000, 64),
        keras.layers.Dense(11, activation=tf.nn.relu),
        keras.layers.Dense(11, activation=tf.nn.relu)


    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(toTrain, flags, epochs=5)
    bots = []
    bots.append([3, 100, 1000, 424])
    bots.append([50, 50, 50, 50])
    bots.append([1000, 5, 1, 7])
    bots.append([243, 534, 532, 5321])
    botflags = [1, 0, 1, 0]
    #test_loss, test_acc = model.evaluate(np.array(bots), np.array(botflags))
    #print('test accuracy:' , test_acc)
    print("\nNeural network built!\n\n\n")
    tempuser = "a"
    while(True):
        print("Enter the twitter handle of the account you wish to check, or type 'exit' to quit: ")
        tempuser = input()
        if tempuser == "exit":
        	print("Exiting...")
        	break
        templist = populateUser(0, tempuser)
        todolist = [templist[1], templist[2], templist[3], templist[4]]
        zerolist = []
        for i in todolist:
            zerolist.append(0)
        # print(todolist)
        # print(zerolist)
        checkinglist = [todolist]
        test_loss, test_acc = model.evaluate(
            np.array(checkinglist), np.array([1]))
        #print("CHANCE OF IT BEING A BOT: ")
        #print(test_acc)
        #print("\n\n trying predict: ")
        pred = model.predict(np.array(checkinglist))
        #print(pred)
        highest = np.argmax(pred[0])

        # Use heap to get max 3, then average
        # Reference: https://stackoverflow.com/questions/6910641/how-do-i-get-indices-of-n-maximum-values-in-a-numpy-array
        maxavg = 0
        maxtotal = 0
        count = 0
        for i in pred[0]:
        	maxavg = i*count + maxavg
        	maxtotal = maxtotal+i
        	count = count+1
        avg = maxavg/maxtotal

        #largest = heapq.nlargest(3, range(len(pred)), pred.take)
        #largestSum = functools.reduce(lambda x, y: x + y, largest)
        #avg = largestSum/len(largest)
        #if highest == 11:
         #   highest = 10
        print("\n\nRating guide: 0 = least likely to be a bot, 10 = most likely to be a bot")
        print("\nBot rating: ", avg)
        print("\n\n")


if __name__ == "__main__":
    main()
