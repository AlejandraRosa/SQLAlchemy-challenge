import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


import datetime
from datetime import date, timedelta

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# need all dates

## loop through dates here

# Converting them to a list of strings
str_dates = []
for date in date_list:
    new_date = date.strftime("%Y-%m-%d")
    str_dates.append(new_date)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) 
    session = Session(engine)

    """precipitation query"""
    # Query data
    results = session.query(Measurement.date).all()

    precipitation = []

    ## precipitation loop here

    session.close()

    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) 
     results = session.query(Station)

    """precipitation query"""
    # Query data
    results = session.query(Measurement.date).all()

    station = []

    ## precipitation loop here

    session.close()

    return jsonify(station)


if __name__ == '__main__':
    app.run(debug=True)
