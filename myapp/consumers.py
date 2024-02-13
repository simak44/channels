from channels.consumer import  AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer


class MySynConsumer(SyncConsumer):
    def websocket_connect(self):
        self.send({
            'type': 'websocket.accept'
        })
        print('Websocket Connected!!!')
    def websocket_receive(self):
        self.accept({
            'type': 'websocket.accept',
            'text':'websocket.send',
        })
        print('mubarak ho')
    def websocket_disconnet(self):
        
        raise StopConsumer
    
    