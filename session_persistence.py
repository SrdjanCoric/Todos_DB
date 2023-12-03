from uuid import uuid4

class SessionPersistence:
    def __init__(self, session):
        self.session = session
        if 'lists' not in self.session:
            self.session['lists'] = []

    def find_list(self, list_id):
            return next((lst for lst in self.session['lists'] if lst['id'] == list_id), None)

    def all_lists(self):
            return self.session['lists']

    def create_new_list(self, list_name):
        self.session['lists'].append({'id': str(uuid4()), 'name': list_name, 'todos': []})
        self.session.modified = True