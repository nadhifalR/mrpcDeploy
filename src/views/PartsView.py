from flask import request, g, Blueprint, json, Response
from ..shared.Authentication import Auth
from ..models.PartsModel import *

parts_api = Blueprint('parts_api', __name__)
cpu_schema = cpuSchema()
motherboard_schema = motherboardSchema()
memory_schema = memorySchema()
internal_hard_drive_schema = internal_hard_driveSchema()
external_hard_drive_schema = external_hard_driveSchema()
case_schema = caseSchema()
video_card_schema = video_cardSchema()
power_supply_schema = power_supplySchema()
keyboard_schema = keyboardSchema()
mouse_schema = mouseSchema()
monitor_schema = monitorSchema()
cpu_cooler_schema = cpu_coolerSchema()
case_fan_schema = case_fanSchema()
wireless_network_card_schema = wireless_network_cardSchema()
wired_network_card_schema = wired_network_cardSchema()
optical_drive_schema = optical_driveSchema()
sound_card_schema = sound_cardSchema()
speakers_schema = speakersSchema()
headphones_schema = headphonesSchema()
ups_schema = upsSchema()
thermal_paste_schema = thermal_pasteSchema()


@parts_api.route('/cpu', methods=['GET'])
def get_all_cpu():
  """
  Get All cpu
  """
  cpu_query_all = cpu.get_all_cpu()
  data = cpu_schema.dump(cpu_query_all, many=True)
  return custom_response(data, 200)

@parts_api.route('/cpu/<int:cpu_id>', methods=['GET'])
def get_cpu(cpu_id):
  """
  Get a single cpu
  """
  cpu_query = cpu.get_cpu(cpu_id)
  if not cpu_query:
    return custom_response({'error': 'cpu not found'}, 404)
  
  data = cpu_schema.dump(cpu_query)
  return custom_response(data, 200)

@parts_api.route('/motherboard', methods=['GET'])
def get_all_motherboard():
  """
  Get All motherboard
  """
  motherboard_query_all = motherboard.get_all_motherboard()
  data = motherboard_schema.dump(motherboard_query_all, many=True)
  return custom_response(data, 200)

@parts_api.route('/motherboard/<int:motherboard_id>', methods=['GET'])
def get_motherboard(motherboard_id):
  """
  Get a single motherboard
  """
  motherboard_query = motherboard.get_motherboard(motherboard_id)
  if not motherboard_query:
    return custom_response({'error': 'motherboard not found'}, 404)
  
  data = motherboard_schema.dump(motherboard_query)
  return custom_response(data, 200)

@parts_api.route('/memory', methods=['GET'])
def get_all_memory():
  """
  Get All memory
  """
  memory_query_all = memory.get_all_memory()
  data = memory_schema.dump(memory_query_all, many=True)
  return custom_response(data, 200)

@parts_api.route('/memory/<int:memory_id>', methods=['GET'])
def get_memory(memory_id):
  """
  Get a single memory
  """
  memory_query = memory.get_memory(memory_id)
  if not memory_query:
    return custom_response({'error': 'memory not found'}, 404)
  
  data = memory_schema.dump(memory_query)
  return custom_response(data, 200)

@parts_api.route('/internal_hard_drive', methods=['GET'])
def get_all_internal_hard_drive():
  """
  Get All internal_hard_drive
  """
  internal_hard_drive_query_all = internal_hard_drive.get_all_internal_hard_drive()
  data = internal_hard_drive_schema.dump(internal_hard_drive_query_all, many=True)
  return custom_response(data, 200)

@parts_api.route('/internal_hard_drive/<int:internal_hard_drive_id>', methods=['GET'])
def get_internal_hard_drive(internal_hard_drive_id):
  """
  Get a single internal_hard_drive
  """
  internal_hard_drive_query = internal_hard_drive.get_internal_hard_drive(internal_hard_drive_id)
  if not internal_hard_drive_query:
    return custom_response({'error': 'internal_hard_drive not found'}, 404)
  
  data = internal_hard_drive_schema.dump(internal_hard_drive_query)
  return custom_response(data, 200)

@parts_api.route('/external_hard_drive', methods=['GET'])
def get_all_external_hard_drive():
  """
  Get All external_hard_drive
  """
  external_hard_drive_query_all = external_hard_drive.get_all_external_hard_drive()
  data = external_hard_drive_schema.dump(external_hard_drive_query_all, many=True)
  return custom_response(data, 200)

@parts_api.route('/external_hard_drive/<int:external_hard_drive_id>', methods=['GET'])
def get_external_hard_drive(external_hard_drive_id):
  """
  Get a single external_hard_drive
  """
  external_hard_drive_query = external_hard_drive.get_external_hard_drive(external_hard_drive_id)
  if not external_hard_drive_query:
    return custom_response({'error': 'external_hard_drive not found'}, 404)
  
  data = external_hard_drive_schema.dump(external_hard_drive_query)
  return custom_response(data, 200)

@parts_api.route('/case', methods=['GET'])
def get_all_case():
  """
  Get All case
  """
  case_query_all = case.get_all_case()
  data = case_schema.dump(case_query_all, many=True)
  return custom_response(data, 200)

@parts_api.route('/case/<int:case_id>', methods=['GET'])
def get_case(case_id):
  """
  Get a single case
  """
  case_query = case.get_case(case_id)
  if not case_query:
    return custom_response({'error': 'case not found'}, 404)
  
  data = case_schema.dump(case_query)
  return custom_response(data, 200)

@parts_api.route('/video_card', methods=['GET'])
def get_all_video_card():
  """
  Get All video_card
  """
  video_card_query_all = video_card.get_all_video_card()
  data = video_card_schema.dump(video_card_query_all, many=True)
  return custom_response(data, 200)

@parts_api.route('/video_card/<int:video_card_id>', methods=['GET'])
def get_video_card(video_card_id):
  """
  Get a single video_card
  """
  video_card_query = video_card.get_video_card(video_card_id)
  if not video_card_query:
    return custom_response({'error': 'video_card not found'}, 404)
  
  data = video_card_schema.dump(video_card_query)
  return custom_response(data, 200)

@parts_api.route('/power_supply', methods=['GET'])
def get_all_power_supply():
  """
  Get All power_supply
  """
  power_supply_query_all = power_supply.get_all_power_supply()
  data = power_supply_schema.dump(power_supply_query_all, many=True)
  return custom_response(data, 200)

@parts_api.route('/power_supply/<int:power_supply_id>', methods=['GET'])
def get_power_supply(power_supply_id):
  """
  Get a single power_supply
  """
  power_supply_query = power_supply.get_power_supply(power_supply_id)
  if not power_supply_query:
    return custom_response({'error': 'power_supply not found'}, 404)
  
  data = power_supply_schema.dump(power_supply_query)
  return custom_response(data, 200)

@parts_api.route('/keyboard', methods=['GET'])
def get_all_keyboard():
  """
  Get All keyboard
  """
  keyboard_query_all = keyboard.get_all_keyboard()
  data = keyboard_schema.dump(keyboard_query_all, many=True)
  return custom_response(data, 200)

@parts_api.route('/keyboard/<int:keyboard_id>', methods=['GET'])
def get_keyboard(keyboard_id):
  """
  Get a single keyboard
  """
  keyboard_query = keyboard.get_keyboard(keyboard_id)
  if not keyboard_query:
    return custom_response({'error': 'keyboard not found'}, 404)
  
  data = keyboard_schema.dump(keyboard_query)
  return custom_response(data, 200)

@parts_api.route('/mouse', methods=['GET'])
def get_all_mouse():
  """
  Get All mouse
  """
  mouse_query_all = mouse.get_all_mouse()
  data = mouse_schema.dump(mouse_query_all, many=True)
  return custom_response(data, 200)

@parts_api.route('/mouse/<int:mouse_id>', methods=['GET'])
def get_mouse(mouse_id):
  """
  Get a single mouse
  """
  mouse_query = mouse.get_mouse(mouse_id)
  if not mouse_query:
    return custom_response({'error': 'mouse not found'}, 404)
  
  data = mouse_schema.dump(mouse_query)
  return custom_response(data, 200)

@parts_api.route('/monitor', methods=['GET'])
def get_all_monitor():
  """
  Get All monitor
  """
  monitor_query_all = monitor.get_all_monitor()
  data = monitor_schema.dump(monitor_query_all, many=True)
  return custom_response(data, 200)

@parts_api.route('/monitor/<int:monitor_id>', methods=['GET'])
def get_monitor(monitor_id):
  """
  Get a single monitor
  """
  monitor_query = monitor.get_monitor(monitor_id)
  if not monitor_query:
    return custom_response({'error': 'monitor not found'}, 404)
  
  data = monitor_schema.dump(monitor_query)
  return custom_response(data, 200)

@parts_api.route('/cpu_cooler', methods=['GET'])
def get_all_cpu_cooler():
  """
  Get All cpu_cooler
  """
  cpu_cooler_query_all = cpu_cooler.get_all_cpu_cooler()
  data = cpu_cooler_schema.dump(cpu_cooler_query_all, many=True)
  return custom_response(data, 200)

@parts_api.route('/cpu_cooler/<int:cpu_cooler_id>', methods=['GET'])
def get_cpu_cooler(cpu_cooler_id):
  """
  Get a single cpu_cooler
  """
  cpu_cooler_query = cpu_cooler.get_cpu_cooler(cpu_cooler_id)
  if not cpu_cooler_query:
    return custom_response({'error': 'cpu_cooler not found'}, 404)
  
  data = cpu_cooler_schema.dump(cpu_cooler_query)
  return custom_response(data, 200)

@parts_api.route('/case_fan', methods=['GET'])
def get_all_case_fan():
  """
  Get All case_fan
  """
  case_fan_query_all = case_fan.get_all_case_fan()
  data = case_fan_schema.dump(case_fan_query_all, many=True)
  return custom_response(data, 200)

@parts_api.route('/case_fan/<int:case_fan_id>', methods=['GET'])
def get_case_fan(case_fan_id):
  """
  Get a single case_fan
  """
  case_fan_query = case_fan.get_case_fan(case_fan_id)
  if not case_fan_query:
    return custom_response({'error': 'case_fan not found'}, 404)
  
  data = case_fan_schema.dump(case_fan_query)
  return custom_response(data, 200)

@parts_api.route('/wireless_network_card', methods=['GET'])
def get_all_wireless_network_card():
  """
  Get All wireless_network_card
  """
  wireless_network_card_query_all = wireless_network_card.get_all_wireless_network_card()
  data = wireless_network_card_schema.dump(wireless_network_card_query_all, many=True)
  return custom_response(data, 200)

@parts_api.route('/wireless_network_card/<int:wireless_network_card_id>', methods=['GET'])
def get_wireless_network_card(wireless_network_card_id):
  """
  Get a single wireless_network_card
  """
  wireless_network_card_query = wireless_network_card.get_wireless_network_card(wireless_network_card_id)
  if not wireless_network_card_query:
    return custom_response({'error': 'wireless_network_card not found'}, 404)
  
  data = wireless_network_card_schema.dump(wireless_network_card_query)
  return custom_response(data, 200)

@parts_api.route('/wired_network_card', methods=['GET'])
def get_all_wired_network_card():
  """
  Get All wired_network_card
  """
  wired_network_card_query_all = wired_network_card.get_all_wired_network_card()
  data = wired_network_card_schema.dump(wired_network_card_query_all, many=True)
  return custom_response(data, 200)

@parts_api.route('/wired_network_card/<int:wired_network_card_id>', methods=['GET'])
def get_wired_network_card(wired_network_card_id):
  """
  Get a single wired_network_card
  """
  wired_network_card_query = wired_network_card.get_wired_network_card(wired_network_card_id)
  if not wired_network_card_query:
    return custom_response({'error': 'wired_network_card not found'}, 404)
  
  data = wired_network_card_schema.dump(wired_network_card_query)
  return custom_response(data, 200)

@parts_api.route('/optical_drive', methods=['GET'])
def get_all_optical_drive():
  """
  Get All optical_drive
  """
  optical_drive_query_all = optical_drive.get_all_optical_drive()
  data = optical_drive_schema.dump(optical_drive_query_all, many=True)
  return custom_response(data, 200)

@parts_api.route('/optical_drive/<int:optical_drive_id>', methods=['GET'])
def get_optical_drive(optical_drive_id):
  """
  Get a single optical_drive
  """
  optical_drive_query = optical_drive.get_optical_drive(optical_drive_id)
  if not optical_drive_query:
    return custom_response({'error': 'optical_drive not found'}, 404)
  
  data = optical_drive_schema.dump(optical_drive_query)
  return custom_response(data, 200)

@parts_api.route('/sound_card', methods=['GET'])
def get_all_sound_card():
  """
  Get All sound_card
  """
  sound_card_query_all = sound_card.get_all_sound_card()
  data = sound_card_schema.dump(sound_card_query_all, many=True)
  return custom_response(data, 200)

@parts_api.route('/sound_card/<int:sound_card_id>', methods=['GET'])
def get_sound_card(sound_card_id):
  """
  Get a single sound_card
  """
  sound_card_query = sound_card.get_sound_card(sound_card_id)
  if not sound_card_query:
    return custom_response({'error': 'sound_card not found'}, 404)
  
  data = sound_card_schema.dump(sound_card_query)
  return custom_response(data, 200)

@parts_api.route('/speakers', methods=['GET'])
def get_all_speakers():
  """
  Get All speakers
  """
  speakers_query_all = speakers.get_all_speakers()
  data = speakers_schema.dump(speakers_query_all, many=True)
  return custom_response(data, 200)

@parts_api.route('/speakers/<int:speakers_id>', methods=['GET'])
def get_speakers(speakers_id):
  """
  Get a single speakers
  """
  speakers_query = speakers.get_speakers(speakers_id)
  if not speakers_query:
    return custom_response({'error': 'speakers not found'}, 404)
  
  data = speakers_schema.dump(speakers_query)
  return custom_response(data, 200)

@parts_api.route('/headphones', methods=['GET'])
def get_all_headphones():
  """
  Get All headphones
  """
  headphones_query_all = headphones.get_all_headphones()
  data = headphones_schema.dump(headphones_query_all, many=True)
  return custom_response(data, 200)

@parts_api.route('/headphones/<int:headphones_id>', methods=['GET'])
def get_headphones(headphones_id):
  """
  Get a single headphones
  """
  headphones_query = headphones.get_headphones(headphones_id)
  if not headphones_query:
    return custom_response({'error': 'headphones not found'}, 404)
  
  data = headphones_schema.dump(headphones_query)
  return custom_response(data, 200)

@parts_api.route('/ups', methods=['GET'])
def get_all_ups():
  """
  Get All ups
  """
  ups_query_all = ups.get_all_ups()
  data = ups_schema.dump(ups_query_all, many=True)
  return custom_response(data, 200)

@parts_api.route('/ups/<int:ups_id>', methods=['GET'])
def get_ups(ups_id):
  """
  Get a single ups
  """
  ups_query = ups.get_ups(ups_id)
  if not ups_query:
    return custom_response({'error': 'ups not found'}, 404)
  
  data = ups_schema.dump(ups_query)
  return custom_response(data, 200)

@parts_api.route('/thermal_paste', methods=['GET'])
def get_all_thermal_paste():
  """
  Get All thermal_paste
  """
  thermal_paste_query_all = thermal_paste.get_all_thermal_paste()
  data = thermal_paste_schema.dump(thermal_paste_query_all, many=True)
  return custom_response(data, 200)

@parts_api.route('/thermal_paste/<int:thermal_paste_id>', methods=['GET'])
def get_thermal_paste(thermal_paste_id):
  """
  Get a single thermal_paste
  """
  thermal_paste_query = thermal_paste.get_thermal_paste(thermal_paste_id)
  if not thermal_paste_query:
    return custom_response({'error': 'thermal_paste not found'}, 404)
  
  data = thermal_paste_schema.dump(thermal_paste_query)
  return custom_response(data, 200)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )