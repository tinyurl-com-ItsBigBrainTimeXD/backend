class DeviceState(object):
    def __init__(self, name: str):
        self.name = name
        self.buzzer = False
        self.lock = True

    def toggle_lock(self):
        self.lock = not self.lock

    def toggle_buzzer(self):
        self.buzzer = not self.buzzer

    def get_dict(self):
        return {
            'buzzer': self.buzzer,
            'lock': self.lock
        }