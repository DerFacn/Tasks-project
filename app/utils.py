from flask import make_response
from flask import jsonify

def response_json(data, code):
    resp = make_response(
        jsonify(data),
        code,
    )
    
    resp.headers["Content-Type"] = "application/json"
    
    return resp