import json
import requests
import datetime
import sys
import pprint
import getUsernames

def ranking(organization_id):

    usernames_dict = getUsernames.get_usernames(organization_id)
    i = 0
    for username in usernames_dict:
        i += 1
        print(i, username, usernames_dict[username])
        if i == 10:
            break


def submissions(organization_id):

    usernames_dict = getUsernames.get_usernames(organization_id)
    i = 0
    
    for username in usernames_dict:
        i += 1

        print(i, username, usernames_dict[username])

        data = requests.get("https://codeforces.com/api/user.status?handle=" +
                            username + "&from=1&count=500").json()


        problems_count = {}

        try:
            for submission in data["result"]:
                time = datetime.datetime.fromtimestamp(
                    submission["creationTimeSeconds"])
                day = time.day
                month = time.month
                year = time.year
                if "contestId" in submission:
                    # print(submission["contestId"], submission["problem"]["index"], submission["problem"]["name"],
                    #       submission["verdict"], day, time.strftime("%B"), year)
                    problem = str(submission["contestId"]) + \
                        str(submission["problem"]["index"])
                    if problem not in problems_count.keys():
                        problems_count[problem] = 1
                    else:
                        problems_count[problem] += 1
        except ():
            print("Not found")
            quit()

        try:
            max_submissions = max(problems_count, key=problems_count.get)
            print("Maximum submission: " + max_submissions,
                problems_count[max_submissions])
        except ():
            print("Not found")

        if i == 10:
            break


