import rankings
import util


if __name__ == "__main__":
    
    print("Input option:")
    option = input()

    if option == "rankings":
        organization_id = util.getID()
        rankings.ranking(organization_id)
    
    elif option == "submissions":
        organization_id = util.getID()
        rankings.submissions(organization_id)
