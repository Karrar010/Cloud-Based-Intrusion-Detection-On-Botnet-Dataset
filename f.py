import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import random
import time
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Alert audio file
ALERT_FILE = "alert.wav"

# Function to play alert sound
def play_alert():
    try:
        pygame.mixer.music.load(ALERT_FILE)
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Error playing alert sound: {e}")

# Simulate packet generation (for demonstration purposes)
def generate_fake_packet():
    return {
        "src_ip": f"192.168.0.{random.randint(1, 255)}",
        "dst_ip": f"10.0.0.{random.randint(1, 255)}",
        "protocol": random.choice(["TCP", "UDP", "Other"]),
        "length": random.randint(20, 1500),
        "ttl": random.randint(1, 255),
        "timestamp": time.strftime('%H:%M:%S')
    }

# Function to check for "intrusion" in packet data (simulated)
def check_for_intrusion(packet):
    # Simulate an intrusion detection logic
    return packet["length"] > 1000 and packet["protocol"] == "TCP"

# Update GUI with new packet data
def update_gui(packet):
    packet_info = (
        f"Time: {packet['timestamp']}, Src: {packet['src_ip']}, Dst: {packet['dst_ip']}, "
        f"Proto: {packet['protocol']}, Len: {packet['length']}, TTL: {packet['ttl']}\n"
    )
    log_text.insert(tk.END, packet_info)
    log_text.see(tk.END)

    # Check for intrusion
    if check_for_intrusion(packet):
        play_alert()
        messagebox.showwarning("Intrusion Alert", "An intrusion has been detected!")

# Function to simulate packet monitoring
def simulate_packet_monitoring():
    packet = generate_fake_packet()
    update_gui(packet)
    root.after(1000, simulate_packet_monitoring)  # Call this function every second

# Create the GUI application
root = tk.Tk()
root.title("Intrusion Detection System")

# Packet log display
log_label = tk.Label(root, text="Packet Log:")
log_label.pack(pady=5)

log_text = ScrolledText(root, width=80, height=20, state="normal")
log_text.pack(padx=10, pady=5)

# Start the simulation
simulate_packet_monitoring()

# Start the GUI event loop
root.mainloop()
