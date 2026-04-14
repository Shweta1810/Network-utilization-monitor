from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import EventMixin
import time

log = core.getLogger()

class Monitor(EventMixin):
    def __init__(self):
        self.listenTo(core.openflow)
        self.packet_count = 0
        self.start_time = time.time()

    def _handle_PacketIn(self, event):
        self.packet_count += 1
        
        duration = time.time() - self.start_time
        
        if duration > 0:
            rate = self.packet_count / duration
        else:
            rate = 0

        log.info("Packets received: %s | Rate: %.2f packets/sec",
                 self.packet_count, rate)

def launch():
    log.info("Network Utilization Monitor started")
    Monitor()
