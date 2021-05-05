from flask import Flask,render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029589e'

from cg_pro import routes1
from cg_pro import routes3