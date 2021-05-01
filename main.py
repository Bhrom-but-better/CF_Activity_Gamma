# import cf.util
from flask import Flask
from flask_restful import Api, Resource
import endpoints

app = Flask(__name__)
api = Api(app)

api.add_resource(endpoints.rankings, '/rankings/<organization_id>')
# api.add_resource(endpoints.submissions, '/submissions/<user_id>')


if __name__ == "__main__":
    
    app.run(debug=True)

    # print("Input option:")
    # option = input()

    # if option == "rankings":
    #     organization_id = util.getID()
    #     rankings.ranking(organization_id)
    
    # elif option == "submissions":
    #     organization_id = util.getID()
    #     rankings.submissions(organization_id)
