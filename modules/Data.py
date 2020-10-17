from templates.Interfaces import IdentityObject


class Data(IdentityObject):
    def __init__(self, id):
        self.id = id
        self.command = None
        self.body = None
        self.processing_time = list()

    def get_processing_time(self):
        return self.processing_time

    def add_processing_time(self, value):
        self.processing_time.append(value)

    def get_command(self):
        return self.command

    def set_command(self, command):
        self.command = command

    def set_body(self, body):
        self.body = body

    def get_body(self):
        return self.body
