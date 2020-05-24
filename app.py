try:
    from flask import Flask, render_template, url_for, request, redirect, make_response, jsonify
    import random
    import json
    from time import time
    from random import random
    from flask import Flask, render_template, make_response
    from flask_dance.contrib.github import make_github_blueprint, github

    import os

    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

except Exception as e:
    print("Some Modules are Missings {}".format(e))

CLIENT_ID = os.environ.get("gh_client_id", default=False)
CLIENT_SECRET = os.environ.get("gh_client_secret", default=False)

app = Flask(__name__)
app.config["SECRET_KEY"] = "asssssssss%#^&*(HSGHLDP(&%$% "

github_blueprint = make_github_blueprint(client_id=CLIENT_ID,
                                         client_secret=CLIENT_SECRET)

app.register_blueprint(github_blueprint, url_prefix='/github_login')


@app.route('/')
def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
        if account_info.ok:
            account_info_json = account_info.json()
            return jsonify(
                {'user_info': json.dumps(account_info_json, indent=4), 'message': 'You have logged in successfully'})

    return jsonify({'message': 'Log In Request failed!'})


if __name__ == "__main__":
    app.run(debug=True)
