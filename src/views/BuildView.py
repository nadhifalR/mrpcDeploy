#/src/views/BuildView.py
from flask import request, g, Blueprint, json, Response
from ..shared.Authentication import Auth
from ..models.BuildModel import BuildModel, BuildSchema

build_api = Blueprint('build_api', __name__)
build_schema = BuildSchema()


@build_api.route('/', methods=['POST'])
#@Auth.auth_required
def create():
  """
  Create Build Function
  """
  req_data = request.get_json()
  #req_data['owner_id'] = g.user.get('id')
  data, error = build_schema.load(req_data)
  if error:
    return custom_response(error, 400)
  post = BuildModel(data)
  post.save()
  data = build_schema.dump(post)
  return custom_response(data, 201)

@build_api.route('/', methods=['GET'])
def get_all():
  """
  Get All Builds
  """
  posts = BuildModel.get_all_builds()
  data = build_schema.dump(posts, many=True)
  return custom_response(data, 200)

@build_api.route('/<int:build_id>', methods=['GET'])
def get_one(build_id):
  """
  Get A Build
  """
  post = BuildModel.get_one_builds(build_id)
  if not post:
    return custom_response({'error': 'build not found'}, 404)
  data = build_schema.dump(post)
  return custom_response(data, 200)

@build_api.route('/<int:build_id>', methods=['PUT'])
#@Auth.auth_required
def update(build_id):
  """
  Update A Build
  """
  req_data = request.get_json()
  post = BuildModel.get_one_builds(build_id)
  if not post:
    return custom_response({'error': 'build not found'}, 404)
  data = build_schema.dump(post)
  #if data.get('owner_id') != g.user.get('id'):
  #  return custom_response({'error': 'permission denied'}, 400)
  
  data, error = build_schema.load(req_data, partial=True)
  if error:
    return custom_response(error, 400)
  post.update(data)
  
  data = build_schema.dump(post)
  return custom_response(data, 200)

@build_api.route('/<int:build_id>', methods=['DELETE'])
#@Auth.auth_required
def delete(build_id):
  """
  Delete A Blogpost
  """
  post = BuildModel.get_one_builds(build_id)
  if not post:
    return custom_response({'error': 'build not found'}, 404)
  data = build_schema.dump(post)
  #if data.get('owner_id') != g.user.get('id'):
  #  return custom_response({'error': 'permission denied'}, 400)

  post.delete()
  return custom_response({'message': 'deleted'}, 204)
  

def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )