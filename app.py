import datetime as dt
import numpy as np
import pandas as pd

# import dependencies for sqlALCHEMY
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# import flask dependencies
from flask import Flask, jsonify

# set up database
engine = create_engine("sqlite:///hawaii.sqlite")