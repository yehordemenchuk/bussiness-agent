from flask import Blueprint, jsonify, request

from app.ai import chain

agent_routes = Blueprint('agent_routes', __name__)

@agent_routes.route('/response')
def get_response_from_agent():
    data = request.get_json()

    question = data.get('question')

    session_id = data.get('session_id')

    return jsonify({'response': chain.get_agent_response(question, session_id)}), 200