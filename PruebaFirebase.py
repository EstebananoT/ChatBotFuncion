import requests
import firestore
import credentials

def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    # Use the application default credentials
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
    'projectId': 'proyecto-juan-lopez-dialogflow',
    })
    

    db = firestore.client()

    doc_ref = db.collection(u'Agenda').document(u'Citas')
    	
    doc_ref.set(data)

    request_json = request.get_json()
    var = request_json['queryResult']['outputContexts']
    data = {
        'Nombre Cliente':var['given-name'],
        'Documento':var['Documento'],
        'Dia_Cita':var['date'],
        'Hora_Cita':var['time']
    }
    print(data)
    return data
