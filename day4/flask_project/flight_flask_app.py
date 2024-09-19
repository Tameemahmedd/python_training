from flask import Flask, jsonify, request
from flight_operations import Flight_operations
# from flight_operations import create_table_flights, createFlight, search_flight, list_flights, delete_flight, update_flight     ###
from flight import Flight
app = Flask(__name__)

Flight_operations.create_table_flights()

class Flight_app:

    @app.route('/flights',methods=['POST'])
    def notes_create():
        body = request.get_json()
        new_flight = Flight(body['airline'], body['source'], body['destination'], body['duration'],body['fare'])
        id = Flight_operations.createFlight(new_flight)
        flight = Flight_operations.search_flight(id)
        flight_dict = {'id':flight.id,'airline':flight.airline,'source':flight.source,'destination':flight.destination,'duration':flight.duration,'fare':flight.fare}
        return jsonify(flight_dict)

    @app.route('/flight/<id>',methods=['GET'])
    def flight_read_by_id(id):
        flight = Flight_operations.search_flight(id)
        flight_dict = {'id':flight.id, 'airline':flight.airline, 'source':flight.source, 'destination':flight.destination, 'duration':flight.duration, 'fare':flight.fare}
        return jsonify(flight_dict)

    @app.route('/flights',methods=['GET'])
    def flights_read_all():
        flights = Flight_operations.list_flights()
        flight_dict = []
        for flight in flights:
            flight_dict.append({'id':flight.id, 'airline':flight.airline, 'source':flight.source, 'destination':flight.destination, 'duration':flight.duration, 'fare':flight.fare})
        return jsonify(flight_dict)

    @app.route('/flight/<id>',methods=['PUT'])
    def flight_update(id):
        body = request.get_json()
        old_flight = Flight_operations.search_flight(id)
        if not old_flight:
            return jsonify({'message': 'Flight is not found'})
        old_flight.airline = body['airline']
        old_flight.source = body['source']
        old_flight.destination = body['destination']
        old_flight.duration = body['duration']
        old_flight.fare = body['fare']
        Flight_operations.update_flight(old_flight)
        flight = Flight_operations.search_flight(id)
        flight_dict = {'id':flight.id, 'airline':flight.airline, 'source':flight.source, 'destination':flight.destination, 'duration':flight.duration, 'fare':flight.fare}
        return jsonify(flight_dict)


    @app.route('/flight/<id>',methods=['DELETE'])
    def notes_delete(id):
        old_flight = Flight_operations.delete_flight(id)
        if old_flight==None:
            return jsonify({'message': 'Note is not found', 'is_error': 1})
        Flight_operations.delete_flight(id)
        return jsonify({'message': 'Note is successfully deleted', 'is_error': 0})

    # @app.route('/notes_search',methods=['POST'])
    # def notes_search():
    #     body = request.get_json()
    #     notes = search(body.get('title',''), body.get('notes_text',''))
    #     notes_dict = []
    #     for note in notes:
    #         notes_dict.append({'id':note.id, 'title':note.title, 'notes':note.notes})
    #     return jsonify(notes_dict)

    app.run(debug=True)