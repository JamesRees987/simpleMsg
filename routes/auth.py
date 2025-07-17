from flask import Blueprint, render_template, jsonify, request

auth = Blueprint('auth', __name__)

@auth.route('/signIn')
def signIn():
    return render_template("auth/signIn.html")

@auth.route('/signUp')
def signUp():
    return render_template("auth/signUp.html")

@auth.route('/signOut')
def signOut():
    pass

@auth.route('/authRecieve', methods=["POST"])
def authRecieve():
    data = request.get_json()
    origin = data.get("sentFrom")
    print(origin)

    match origin:
        case "/signIn":
            email = data.get("email")
            password = data.get("password")
            print(email)
            print(password)
        
        case "/signUp":
            pass

        case _:
            return jsonify({"message": "Invalid path."}), 404
    

    return jsonify({"message": "Data recieved."})