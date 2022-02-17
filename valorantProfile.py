# Valorant Profile Class
# Description: Class containing attributes and methods to fetch valorant
# stats and information given account name and tag
# Contributers: Jan Rylan Pueblo
# Version 1.1, Added functionality for Immortal+
# January 25th, 2022

from bs4 import BeautifulSoup
import requests
import string


class valorantProfile:

    immortalPlus = False

    def __init__(self, username, tag):
        self.username = username
        self.tag = tag[1:]
        player = ""
        for i in range(len(username)):
            player += username[i] + "%20"
        player = player[:-3]
        link = "https://tracker.gg/valorant/profile/riot/" + player + "%23" + self.tag + "/overview"
        self.url = link.replace(" ", "")
        result = requests.get(self.url)
        self.doc = BeautifulSoup(result.text, "html.parser")
        rank = self.getRank().split(' ')[0]
        ranks = "ironbronzesilvergoldplatniumdiamond"
        if(rank.lower() not in ranks):
            self.immortalPlus = True

    # Accessor Methods

    def getUser(self):
        return self.username

    def getTag(self):
        return self.tag

    def getUrl(self):
        return self.url

    def getDoc(self):
        return self.doc

    def getRank(self):
        #value -> Diamond 2, label -> Rating
        #For Immortal+ value -> RR and label -> Immortal/Radiant

        stats = self.doc.find("div", class_="valorant-highlighted-stat")
        rank = stats.find("span", class_="valorant-highlighted-stat__value").text

        if(self.immortalPlus):
            rank = stats.find("span", class_="valorant-highlighted-stat__label").text
            Rating = ": " + stats.find("span", class_="valorant-highlighted-stat__value").text
            return rank + Rating
        else:
            return rank

    def getKD(self):
        stats = self.doc.find_all("div", class_="wrapper")[1]
        KD = stats.find("span", class_="value").text
        return KD

    def getWinPercentage(self):
        stats = self.doc.find_all("div", class_="wrapper")[3]
        winPercentage = stats.find("span", class_="value").text
        return winPercentage

    def getMainStats(self):
        if(self.immortalPlus):
            return [self.getRank(), self.getLeaderboard(), self.getKD(), self.getWinPercentage()]
        else:
            return [self.getRank(), self.getKD(), self.getWinPercentage()]

    # This method checks leaderboard position of Immortal+ player
    def getLeaderboard(self):
        stats = self.doc.find("div", class_="valorant-highlighted-content")
        rank = stats.findAllNext("span", class_="valorant-highlighted-stat__value")[1].text

        if(self.immortalPlus):
            return rank
        else:
            return "This user is not Immortal+! Git Gud"



    # Print Methods

    def printMain(self):
        self.printCurrentRank()
        self.printKD()
        self.printWinPercentage()

    def printCurrentRank(self):
        print("Current Rank: " + self.getRank())

    def printKD(self):
        print("KD Ratio: " + self.getKD())

    def printWinPercentage(self):
        print("Win%: " + self.getWinPercentage())



def main():
    creds = input("Enter Your Valorant Username and Tag: ")
    user = creds.split('#')[0]
    tag = creds.split('#')[1]
    profile = valorantProfile(user, tag)




if __name__ == "__main__":
    main()
