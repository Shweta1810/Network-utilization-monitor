# 📡 Network Utilization Monitor using SDN

---

##  Objective

The objective of this project is to monitor network traffic by calculating packet rate using a Software Defined Networking (SDN) controller.

---

##  Project Description

This project uses **Mininet** to simulate a network and **POX controller** to manage network behavior.
A custom Python script (`monitor.py`) is used to track incoming packets and calculate the packet rate (packets per second), which represents network utilization.

---

##  Tools & Technologies Used

* Mininet
* POX Controller
* Python
* Ubuntu Linux

---

## ⚙️ How to Run the Project

### Step 1: Start POX Controller

```bash
cd ~/pox
./pox.py forwarding.l2_learning monitor
```

### Step 2: Start Mininet

```bash
sudo mn --topo single,3 --controller=remote
```

### Step 3: Test Network

Inside Mininet:

```bash
pingall
```

---

## Output

The controller displays network utilization in the form of packet count and packet rate:

```
Packets received: 10 | Rate: 2.5 packets/sec
Packets received: 20 | Rate: 3.1 packets/sec
```

---

##  Explanation

* Mininet creates a virtual network with hosts and switches.
* POX controller manages the network using OpenFlow.
* The `monitor.py` script listens to packet events (`PacketIn`).
* It counts packets and calculates the rate using time.

---

##  Screenshots

Include the following screenshots in your repository:

* POX Controller running
* Mininet topology
* pingall output
* Packet monitoring output

---

## Future Scope

* Graphical visualization of network traffic
* Real-time monitoring dashboard
* Integration with machine learning for anomaly detection

---

## Conclusion

This project successfully demonstrates how SDN can be used to monitor network utilization by analyzing packet flow and calculating packet rates in real time.

---

##  Author

Shweta
CSE (AIML)
