# ******************************************************************************
#  Copyright (c) 2021 Nurul-GC.                                                *
# ******************************************************************************

from flask import render_template, redirect, request
from . import app


@app.route('index/', methods=['GET'])
def index():
    return render_template('index.html')
