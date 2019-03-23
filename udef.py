import can
import threading
import time

def can_bus_monitor():
	while True:
		message = can_bus.recv();
		if (message.arbitration_id == 0x500):
			print("=============================");
			print("RPM: ", int.from_bytes([message.data[0], message.data[1]], byteorder='little', signed=False)/4)
			print("CLT: ", int.from_bytes([message.data[2], message.data[3]], byteorder='little', signed=False))
			print("TPS: ", int.from_bytes([message.data[4]], byteorder='little', signed=False))
			print("OILP: ", int.from_bytes([message.data[5]], byteorder='little', signed=False))

can_bus = can.interface.Bus(channel='can0', bustype='socketcan_native')

can_bus_monitor_thread = threading.Thread(target=can_bus_monitor)
can_bus_monitor_thread.start()
