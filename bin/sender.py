from service.ses_sender import SESSender


class Sender:
    def __init__(self, config):
        self.sender = SESSender(config)

    def send(self):
        self.sender.send()
