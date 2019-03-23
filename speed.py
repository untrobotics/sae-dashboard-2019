import can
import threading
import time

def can_bus_monitor():
	while True:
		#time.sleep(0.01)
		msg = can.Message(arbitration_id=0x7df, data=[2, 1, 0x0d, 0, 0, 0, 0, 0], extended_id=False)
		can_bus.send(msg)
		while True:
			message = can_bus.recv();
			if message.arbitration_id == 0x7e8:
				break;

		#if (message.arbitration_id == 0x7e8):
		print(int.from_bytes([message.data[3]], byteorder='big', signed=False))

can_bus = can.interface.Bus(channel='can0', bustype='socketcan_native')

#msg = can.Message(arbitration_id=0x7df, data=[2, 1, 0x0c, 0, 0, 0, 0, 0], extended_id=False)
#can_bus.send(msg)

can_bus_monitor_thread = threading.Thread(target=can_bus_monitor)
can_bus_monitor_thread.start()

while True:
	time.sleep(5)
	print("RUN");
