import can
import threading
import time

def can_bus_monitor():
	while True:
		message = can_bus.recv();
		if (message.arbitration_id == 0x7e8):
			print(int.from_bytes([message.data[3], message.data[4]], byteorder='big', signed=False)/4)

can_bus = can.interface.Bus(channel='can0', bustype='socketcan_native')

#msg = can.Message(arbitration_id=0x7df, data=[2, 1, 0x0c, 0, 0, 0, 0, 0], extended_id=False)
#can_bus.send(msg)

can_bus_monitor_thread = threading.Thread(target=can_bus_monitor)
can_bus_monitor_thread.start()

while True:
	time.sleep(5)
	print("RUN");
