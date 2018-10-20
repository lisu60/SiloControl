from flask_sqlalchemy import SQLAlchemy
from app import app
import enum

db = SQLAlchemy(app)


class MeasurementType(enum.Enum):
    BOOL = 1
    BOOL_NEGATION = 2
    FLOAT = 3


class Device(db.Model):
    Id = db.Column('id', db.Integer, primary_key=True)
    Name = db.Column('name', db.String(100), nullable=False)
    Measurements = db.relationship('Measurement', back_populates='Device')


class Measurement(db.Model):
    Id = db.Column('id', db.Integer, primary_key=True)
    Name = db.Column('name', db.String(100), nullable=False)
    Type = db.Column('type', db.Enum(MeasurementType), nullable=False)
    Readonly = db.Column('readonly', db.Boolean, nullable=False)
    DevId = db.Column('dev_id', db.Integer, db.ForeignKey("device.id"), nullable=False)
    Device = db.relationship(Device, primaryjoin=DevId == Device.Id, back_populates='Measurements')

