from flask import Blueprint, jsonify
from BLL.usersBLL import UsersBLL


users_bll = UsersBLL()

users = Blueprint('users', __name__ )

# Get All Users
# server:port/users
@users.route("/", methods=['GET'])
def get_all_users():
    users = users_bll.get_all_users()
    return jsonify(users)

