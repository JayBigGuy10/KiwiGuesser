from flask import (
    Flask,
    flash,
    request,
    redirect,
    url_for,
    jsonify,
    send_from_directory,
    after_this_request,
)
from flask_cors import CORS