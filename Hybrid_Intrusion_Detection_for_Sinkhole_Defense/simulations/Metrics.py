import matplotlib.pyplot as plt
import numpy as np

def read_data(filename):
    """Reads numerical data from a file and returns it as a list of floats."""
    with open(filename, 'r') as file:
        data = [line.strip() for line in file.readlines()]
    return list(map(float, data)) if data else []

with open('nodes.txt', 'r') as file:
    num_sensor_nodes = int(file.readline().strip())
sensor_nodes = list(range(1, num_sensor_nodes + 1))
accuracy = read_data('acc.txt')
latency = read_data('lat.txt')
packet_delivery_ratio = read_data('pdr.txt')
energy = read_data('eng.txt')
false_positive_rate = read_data('fpr.txt')

plt.figure(figsize=(10, 5), facecolor='#DFF0EA')
ax = plt.gca()
ax.set_facecolor('#E6FFF7')
plt.plot(sensor_nodes, accuracy, marker='o', color='#1E90FF', markerfacecolor='green', label='Hybrid Intrusion Detection A Novel Approach to Sinkhole Defense')
plt.fill_between(sensor_nodes, accuracy, min(accuracy), color='#B0E0E6', alpha=0.3)
plt.xlabel('Number of Sensor Nodes')
plt.ylabel('Detection Accuracy (%)')
plt.title('Number of Sensor Nodes vs. Detection Accuracy (%)')
plt.legend()
plt.grid(False)
plt.show()

plt.figure(figsize=(10, 5), facecolor='#FFF0F5')
ax = plt.gca()
ax.set_facecolor('#FFE4EC')
plt.plot(sensor_nodes, latency, marker='s', color='purple', markerfacecolor='red', label='Hybrid Intrusion Detection A Novel Approach to Sinkhole Defense')
plt.fill_between(sensor_nodes, latency, min(latency), color='#D8BFD8', alpha=0.3)
plt.xlabel('Number of Sensor Nodes')
plt.ylabel('Latency (ms)')
plt.title('Number of Sensor Nodes vs. Latency (ms)')
plt.legend()
plt.grid(False)
plt.show()

plt.figure(figsize=(10, 5), facecolor='#FFFACD')
ax = plt.gca()
ax.set_facecolor('#FAFAD2')
plt.bar(sensor_nodes, packet_delivery_ratio, color='#32CD32', edgecolor='black', label='Hybrid Intrusion Detection A Novel Approach to Sinkhole Defense')
plt.xlabel('Number of Sensor Nodes')
plt.ylabel('Packet Delivery Ratio (%)')
plt.title('Number of Sensor Nodes vs. Packet Delivery Ratio (%)')
plt.legend()
plt.ylim(75,100)
plt.grid(False)
plt.show()

plt.figure(figsize=(10, 5), facecolor='#E0FFFF')
ax = plt.gca()
ax.set_facecolor('#CCFFFF')
plt.bar(sensor_nodes, energy, color='#FFA07A', edgecolor='black', label='Hybrid Intrusion Detection A Novel Approach to Sinkhole Defense')
plt.xlabel('Number of Sensor Nodes')
plt.ylabel('Energy Consumption (J)')
plt.title('Number of Sensor Nodes vs. Energy Consumption (J)')
plt.legend()
plt.grid(False)
plt.show()

plt.figure(figsize=(10, 5), facecolor='#F5F5DC')
ax = plt.gca()
ax.set_facecolor('#FFF5E1')
plt.plot(sensor_nodes, false_positive_rate, marker='^', color='crimson', markerfacecolor='blue', label='Hybrid Intrusion Detection A Novel Approach to Sinkhole Defense')
plt.fill_between(sensor_nodes, false_positive_rate, min(false_positive_rate), color='lightcoral', alpha=0.3)
plt.xlabel('Number of Sensor Nodes')
plt.ylabel('False Positive Rate (%)')
plt.title('Number of Sensor Nodes vs. False Positive Rate (%)')
plt.legend()
plt.grid(False)
plt.show()
