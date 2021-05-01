import json
import pprint
from cf_api import getUsernames
from flask_restful import Resource

class rankings(Resource):
    def get(self, organization_id):
        usernames_dict = getUsernames.get_usernames(organization_id)
        # i = 0
        # for username in user  names_dict:
        #     i += 1
        #     print(i, username, usernames_dict[username])
        #     if i == 10:
        #         break
        return json.dumps(usernames_dict)

