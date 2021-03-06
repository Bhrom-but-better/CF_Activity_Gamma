import json
import requests
import datetime

username = input("Handle: ")
data = requests.get("https://codeforces.com/api/user.status?handle=" + username + "&from=1&count=500").json()

problems_count = {}

for submission in data["result"]:
    time = datetime.datetime.fromtimestamp(submission["creationTimeSeconds"])
    day = time.day
    month = time.month
    year = time.year
    print(submission["contestId"], submission["problem"]["index"], submission["problem"]["name"],
          submission["verdict"], day, time.strftime("%B"), year)
    problem = str(submission["contestId"]) + str(submission["problem"]["index"])
    if problem not in problems_count.keys():
        problems_count[problem] = 1
    else:
        problems_count[problem] += 1


max_submissions = max(problems_count, key=problems_count.get)
print("Maximum submission: " + max_submissions, problems_count[max_submissions])



