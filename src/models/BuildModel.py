# src/models/Blogpost.py
from . import db
import datetime
from marshmallow import fields, Schema

class BuildModel(db.Model):
  """
  Blogpost Model
  """

  __tablename__ = 'builds'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128), nullable=False)
  """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
  cpu = db.Column(db.Integer, db.ForeignKey('cpu.id'), nullable=False)
  motherboard = db.Column(db.Integer, db.ForeignKey('motherboard.id'), nullable=False)
  memory = db.Column(db.Integer, db.ForeignKey('memory.id'), nullable=False)
  """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
  internal_hard_drive = db.Column(db.Integer, db.ForeignKey('internal_hard_drive.id'), nullable=False)
  external_hard_drive = db.Column(db.Integer, db.ForeignKey('external_hard_drive.id'), nullable=False)
  case = db.Column(db.Integer, db.ForeignKey('case.id'), nullable=False)
  video_card = db.Column(db.Integer, db.ForeignKey('video_card.id'), nullable=False)
  power_supply = db.Column(db.Integer, db.ForeignKey('power_supply.id'), nullable=False)
  keyboard = db.Column(db.Integer, db.ForeignKey('keyboard.id'), nullable=False)
  mouse = db.Column(db.Integer, db.ForeignKey('mouse.id'), nullable=False)
  monitor = db.Column(db.Integer, db.ForeignKey('monitor.id'), nullable=False)
  """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
  cpu_cooler = db.Column(db.Integer, db.ForeignKey('cpu_cooler.id'), nullable=False)
  case_fan = db.Column(db.Integer, db.ForeignKey('case_fan.id'), nullable=False)
  wireless_network_card = db.Column(db.Integer, db.ForeignKey('wireless_network_card.id'), nullable=False)
  wired_network_card = db.Column(db.Integer, db.ForeignKey('wired_network_card.id'), nullable=False)
  optical_drive = db.Column(db.Integer, db.ForeignKey('optical_drive.id'), nullable=False)
  sound_card = db.Column(db.Integer, db.ForeignKey('sound_card.id'), nullable=False)
  speakers = db.Column(db.Integer, db.ForeignKey('speakers.id'), nullable=False)
  headphones = db.Column(db.Integer, db.ForeignKey('headphones.id'), nullable=False)
  ups = db.Column(db.Integer, db.ForeignKey('ups.id'), nullable=False)
  thermal_paste = db.Column(db.Integer, db.ForeignKey('thermal_paste.id'), nullable=False)
  """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""  
  owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  created_at = db.Column(db.DateTime)
  modified_at = db.Column(db.DateTime)

  def __init__(self, data):
    self.title = data.get('title')
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 
    self.cpu= data.get('cpu')
    self.motherboard= data.get('motherboard')
    self.memory= data.get('memory')
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 
    self.internal_hard_drive= data.get('internal_hard_drive')
    self.external_hard_drive= data.get('external_hard_drive')
    self.case= data.get('case')
    self.video_card= data.get('video_card')
    self.power_supply= data.get('power_supply')
    self.keyboard= data.get('keyboard')
    self.mouse= data.get('mouse')
    self.monitor= data.get('monitor')
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 
    self.cpu_cooler= data.get('cpu_cooler')
    self.case_fan= data.get('case_fan')
    self.wireless_network_card= data.get('wireless_network_card')
    self.wired_network_card= data.get('wired_network_card')
    self.optical_drive= data.get('optical_drive')
    self.sound_card= data.get('sound_card')
    self.speakers= data.get('speakers')
    self.headphones= data.get('headphones')
    self.ups= data.get('ups')
    self.thermal_paste= data.get('thermal_paste')
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    self.owner_id = data.get('owner_id')
    self.created_at = datetime.datetime.utcnow()
    self.modified_at = datetime.datetime.utcnow()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    self.modified_at = datetime.datetime.utcnow()
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
  
  @staticmethod
  def get_all_builds():
    return BuildModel.query.all()
  
  @staticmethod
  def get_one_builds(id):
    return BuildModel.query.get(id)

  def __repr__(self):
    return '<id {}>'.format(self.id)


class BuildSchema(Schema):
  """
  Blogpost Schema
  """
  id = fields.Int(dump_only=True)
  title = fields.Str(required=True)
  """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
  cpu = fields.Int(required=False)
  motherboard = fields.Int(required=False)
  memory = fields.Int(required=False)
  """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
  internal_hard_drive = fields.Int(required=False)
  external_hard_drive = fields.Int(required=False)
  case = fields.Int(required=False)
  video_card = fields.Int(required=False)
  power_supply = fields.Int(required=False)
  keyboard = fields.Int(required=False)
  mouse = fields.Int(required=False)
  monitor = fields.Int(required=False)
  """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
  cpu_fan = fields.Int(required=False)
  case_fan = fields.Int(required=False)
  wireless_network_card = fields.Int(required=False)
  wired_network_card = fields.Int(required=False)
  optical_drive = fields.Int(required=False)
  sound_card = fields.Int(required=False)
  speakers = fields.Int(required=False)
  headphones = fields.Int(required=False)
  ups = fields.Int(required=False)
  thermal_paste = fields.Int(required=False)
  """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
  owner_id = fields.Int(required=False)
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)