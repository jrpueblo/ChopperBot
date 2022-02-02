# Valorant Profile Class
# Description: Class containing attributes and methods to fetch valorant
# stats and information given account name and tag
# Contributers: Jan Rylan Pueblo
# Version 1.0
# January 25th, 2022

from bs4 import BeautifulSoup
import requests
import string


class valorantProfile:

    def __init__(self, username, tag):
        self.username = username.strip()
        self.tag = tag
        link = "https://tracker.gg/valorant/profile/riot/" + self.username + "%23" + self.tag + "/overview"
        self.url = link.replace(" ", "")
        result = requests.get(self.url)
        self.doc = BeautifulSoup(result.text, "html.parser")

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
        stats = self.doc.find("div", class_="valorant-highlighted-stat")
        rank = stats.find("span", class_="valorant-highlighted-stat__value").text
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
        return [self.getRank(), self.getKD(), self.getWinPercentage()]


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
    print(profile.getMainStats()[0])

if __name__ == "__main__":
    main()
