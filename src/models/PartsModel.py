from . import db
from marshmallow import fields, Schema

class cpu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)
    Socket = db.Column(db.String) 

    @staticmethod
    def get_all_cpu():
        return cpu.query.all()

    @staticmethod
    def get_cpu(id):
        return cpu.query.get(id)

    def __repr(self):
        return '<id {}>'.format(self.id)

class cpuSchema(Schema):
    id = fields.Int(dump_only=True)
    Name = fields.Str(dump_only=True)
    Socket = fields.Str(dump_only=True)

class motherboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    model = db.Column(db.String)
    socket = db.Column(db.String)
    form_factor = db.Column(db.String)

    @staticmethod
    def get_all_motherboard():
        return motherboard.query.all()

    @staticmethod
    def get_motherboard(id):
        return motherboard.query.get(id)
        
    def __repr(self):
        return '<id {}>'.format(self.id)

class motherboardSchema(Schema):
    id = fields.Int(dump_only=True)
    brand = fields.Str(dump_only=True)
    model = fields.Str(dump_only=True)
    socket = fields.Str(dump_only=True)
    form_factor = fields.Str(dump_only=True)

class memory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    model = db.Column(db.String)
    module_type = db.Column(db.String)
    speed_cycles = db.Column(db.String)

    @staticmethod
    def get_all_memory():
        return memory.query.all()

    @staticmethod
    def get_memory(id):
        return memory.query.get(id)
        
    def __repr(self):
        return '<id {}>'.format(self.id)

class memorySchema(Schema):
    id = fields.Int(dump_only=True)
    brand = fields.Str(dump_only=True)
    model = fields.Str(dump_only=True)
    module_type = fields.Str(dump_only=True)
    speed_cycles = fields.Str(dump_only=True)

class internal_hard_drive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    model = db.Column(db.String)
    capacity_total = db.Column(db.BigInteger)
    storage_type = db.Column(db.String)
    interface = db.Column(db.String)

    @staticmethod
    def get_all_internal_hard_drive():
        return internal_hard_drive.query.all()

    @staticmethod
    def get_internal_hard_drive(id):
        return internal_hard_drive.query.get(id)
        
    def __repr(self):
        return '<id {}>'.format(self.id)

class internal_hard_driveSchema(Schema):
    id = fields.Int(dump_only=True)
    brand = fields.Str(dump_only=True)
    model = fields.Str(dump_only=True)
    capacity_total = fields.Int(dump_only=True)
    storage_type = fields.Str(dump_only=True)
    interface = fields.Str(dump_only=True)

class external_hard_drive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    model = db.Column(db.String)
    interface = db.Column(db.String)
    capacity_total = db.Column(db.BigInteger)

    @staticmethod
    def get_all_external_hard_drive():
        return external_hard_drive.query.all()

    @staticmethod
    def get_external_hard_drive(id):
        return external_hard_drive.query.get(id)
        
    def __repr(self):
        return '<id {}>'.format(self.id)

class external_hard_driveSchema(Schema):
    id = fields.Int(dump_only=True)
    brand = fields.Str(dump_only=True)
    model = fields.Str(dump_only=True)
    interface = fields.Str(dump_only=True)
    capacity_total = fields.Int(dump_only=True)

class case(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    model = db.Column(db.String)
    form_factor = db.Column(db.String)
    color = db.Column(db.String)

    @staticmethod
    def get_all_case():
        return case.query.all()

    @staticmethod
    def get_case(id):
        return case.query.get(id)
        
    def __repr(self):
        return '<id {}>'.format(self.id)

class caseSchema(Schema):
    id = fields.Int(dump_only=True)
    brand = fields.Str(dump_only=True)
    model = fields.Str(dump_only=True)
    form_factor = fields.Str(dump_only=True)
    color = fields.Str(dump_only=True)

class video_card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    chipset = db.Column(db.String)
    vram_total = db.Column(db.BigInteger)

    @staticmethod
    def get_all_video_card():
        return video_card.query.all()

    @staticmethod
    def get_video_card(id):
        return video_card.query.get(id)
        
    def __repr(self):
        return '<id {}>'.format(self.id)

class video_cardSchema(Schema):
    id = fields.Int(dump_only=True)
    brand = fields.Str(dump_only=True)
    chipset = fields.Str(dump_only=True)
    vram_total = fields.Int(dump_only=True)

class power_supply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    model = db.Column(db.String)
    efficiency_rating = db.Column(db.String)
    wattage = db.Column(db.Integer)

    @staticmethod
    def get_all_power_supply():
        return power_supply.query.all()

    @staticmethod
    def get_power_supply(id):
        return power_supply.query.get(id)
        
    def __repr(self):
        return '<id {}>'.format(self.id)

class power_supplySchema(Schema):
    id = fields.Int(dump_only=True)
    brand = fields.Str(dump_only=True)
    model = fields.Str(dump_only=True)
    efficiency_rating = fields.Str(dump_only=True)
    wattage = fields.Int(dump_only=True)

class keyboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    model = db.Column(db.String)
    style = db.Column(db.String)
    switches = db.Column(db.String)
    backlight = db.Column(db.String)
    connection = db.Column(db.String)

    @staticmethod
    def get_all_keyboard():
        return keyboard.query.all()

    @staticmethod
    def get_keyboard(id):
        return keyboard.query.get(id)
        
    def __repr(self):
        return '<id {}>'.format(self.id)

class keyboardSchema(Schema):
    id = fields.Int(dump_only=True)
    brand = fields.Str(dump_only=True)
    model = fields.Str(dump_only=True)
    style = fields.Str(dump_only=True)
    switches = fields.Str(dump_only=True)
    backlight = fields.Str(dump_only=True)
    connection = fields.Str(dump_only=True)

class mouse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    model = db.Column(db.String)
    connection = db.Column(db.String)

    @staticmethod
    def get_all_mouse():
        return mouse.query.all()

    @staticmethod
    def get_mouse(id):
        return mouse.query.get(id)
        
    def __repr(self):
        return '<id {}>'.format(self.id)

class mouseSchema(Schema):
    id = fields.Int(dump_only=True)
    brand = fields.Str(dump_only=True)
    model = fields.Str(dump_only=True)
    connection = fields.Str(dump_only=True)

class monitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    model = db.Column(db.String)
    size = db.Column(db.Float)
    panel_type = db.Column(db.String)

    @staticmethod
    def get_all_monitor():
        return monitor.query.all()

    @staticmethod
    def get_monitor(id):
        return monitor.query.get(id)
        
    def __repr(self):
        return '<id {}>'.format(self.id)

class monitorSchema(Schema):
    id = fields.Int(dump_only=True)
    brand = fields.Str(dump_only=True)
    model = fields.Str(dump_only=True)
    size = fields.Float(dump_only=True)
    panel_type = fields.Str(dump_only=True)

class cpu_cooler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    model = db.Column(db.String)
    color = db.Column(db.String)

    @staticmethod
    def get_all_cpu_cooler():
        return cpu_cooler.query.all()

    @staticmethod
    def get_cpu_cooler(id):
        return cpu_cooler.query.get(id)
        
    def __repr(self):
        return '<id {}>'.format(self.id)

class cpu_coolerSchema(Schema):
    id = fields.Int(dump_only=True)
    brand = fields.Str(dump_only=True)
    model = fields.Str(dump_only=True)
    color = fields.Str(dump_only=True)

class case_fan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    model = db.Column(db.String)
    size = db.Column(db.Integer)
    color = db.Column(db.Integer)

    @staticmethod
    def get_all_case_fan():
        return case_fan.query.all()

    @staticmethod
    def get_case_fan(id):
        return case_fan.query.get(id)
        
    def __repr(self):
        return '<id {}>'.format(self.id)

class case_fanSchema(Schema):
    id = fields.Int(dump_only=True)
    brand = fields.Str(dump_only=True)
    model = fields.Str(dump_only=True)
    size = fields.Int(dump_only=True)
    color = fields.Str(dump_only=True)

class wireless_network_card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    model = db.Column(db.String)
    supported_protocols = db.Column(db.String)
    interface = db.Column(db.String)

    @staticmethod
    def get_all_wireless_network_card():
        return wireless_network_card.query.all()

    @staticmethod
    def get_wireless_network_card(id):
        return wireless_network_card.query.get(id)
        
    def __repr(self):
        return '<id {}>'.format(self.id)
    
class wireless_network_cardSchema(Schema):
    id = fields.Int(dump_only=True)
    brand = fields.Str(dump_only=True)
    model = fields.Str(dump_only=True)
    supported_protocols = fields.Str(dump_only=True)
    interface = fields.Str(dump_only=True)    

class wired_network_card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    model = db.Column(db.String)
    interface = db.Column(db.String)

    @staticmethod
    def get_all_wired_network_card():
        return wired_network_card.query.all()

    @staticmethod
    def get_wired_network_card(id):
        return wired_network_card.query.get(id)
        
    def __repr(self):
        return '<id {}>'.format(self.id)

class wired_network_cardSchema(Schema):
    id = fields.Int(dump_only=True)
    brand = fields.Str(dump_only=True)
    model = fields.Str(dump_only=True)
    interface = fields.Str(dump_only=True)

class optical_drive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    model = db.Column(db.String)

    @staticmethod
    def get_all_optical_drive():
        return optical_drive.query.all()

    @staticmethod
    def get_optical_drive(id):
        return optical_drive.query.get(id)
        
    def __repr(self):
        return '<id {}>'.format(self.id)

class optical_driveSchema(Schema):
    id = fields.Int(dump_only=True)
    brand = fields.Str(dump_only=True)
    model = fields.Str(dump_only=True)

class sound_card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    model = db.Column(db.String)
    interface = db.Column(db.String)

    @staticmethod
    def get_all_sound_card():
        return sound_card.query.all()

    @staticmethod
    def get_sound_card(id):
        return sound_card.query.get(id)
        
    def __repr(self):
        return '<id {}>'.format(self.id)

class sound_cardSchema(Schema):
    id = fields.Int(dump_only=True)
    brand = fields.Str(dump_only=True)
    model = fields.Str(dump_only=True)
    interface = fields.Str(dump_only=True)

class speakers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    model = db.Column(db.String)

    @staticmethod
    def get_all_speakers():
        return speakers.query.all()

    @staticmethod
    def get_speakers(id):
        return speakers.query.get(id)
        
    def __repr(self):
        return '<id {}>'.format(self.id)

class speakersSchema(Schema):
    id = fields.Int(dump_only=True)
    brand = fields.Str(dump_only=True)
    model = fields.Str(dump_only=True)

class headphones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    model = db.Column(db.String)
    form_factor = db.Column(db.String)

    @staticmethod
    def get_all_headphones():
        return headphones.query.all()

    @staticmethod
    def get_headphones(id):
        return headphones.query.get(id)
        
    def __repr(self):
        return '<id {}>'.format(self.id)

class headphonesSchema(Schema):
    id = fields.Int(dump_only=True)
    brand = fields.Str(dump_only=True)
    model = fields.Str(dump_only=True)
    form_factor = fields.Str(dump_only=True)

class ups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    model = db.Column(db.String)
    watt_capacity = db.Column(db.Integer)
    va_capacity = db.Column(db.Float)

    @staticmethod
    def get_all_ups():
        return ups.query.all()

    @staticmethod
    def get_ups(id):
        return ups.query.get(id)
        
    def __repr(self):
        return '<id {}>'.format(self.id)

class upsSchema(Schema):
    id = fields.Int(dump_only=True)
    brand = fields.Str(dump_only=True)
    model = fields.Str(dump_only=True)
    watt_capacity = fields.Int(dump_only=True)
    va_capacity = fields.Float(dump_only=True)

class thermal_paste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    model = db.Column(db.String)
    amount = db.Column(db.Float)

    @staticmethod
    def get_all_thermal_paste():
        return thermal_paste.query.all()

    @staticmethod
    def get_thermal_paste(id):
        return thermal_paste.query.get(id)
        
    def __repr(self):
        return '<id {}>'.format(self.id)

class thermal_pasteSchema(Schema):
    id = fields.Int(dump_only=True)
    brand = fields.Str(dump_only=True)
    model = fields.Str(dump_only=True)
    ammount = fields.Float(dump_only=True)