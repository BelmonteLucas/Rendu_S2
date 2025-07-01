from flask import Flask, render_template, request, Response
from scapy.all import ARP, Ether, srp
import requests
import csv
import io
import collections

app = Flask(__name__)

def get_mac_vendor(mac):
    mac_prefix = mac.upper().replace('-', ':')[:8]
    try:
        response = requests.get(f"https://api.macvendors.com/{mac_prefix}", timeout=5)
        if response.status_code == 200:
            return response.text
    except Exception:
        pass
    return "Inconnu"

def get_arp_devices(network):
    arp = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=5, verbose=False)[0]

    devices = []
    seen = set()
    for _, received in result:
        ip = received.psrc
        mac = received.hwsrc
        if ip not in seen:
            seen.add(ip)
            vendor = get_mac_vendor(mac)
            devices.append({
                "ip": ip,
                "mac": mac,
                "marque": vendor,
                "reachable": True
            })
    return devices

@app.route("/", methods=["GET", "POST"])
def index():
    devices = []
    network = request.form.get("network") if request.method == "POST" else ""
    brands = {}

    if request.method == "POST":
        if request.form.get("reset") == "1":
            # Reset : vide tout
            return render_template("index.html", devices=[], network="", brands={})
        elif network:
            devices = get_arp_devices(network)
            brands = collections.Counter([d["marque"] for d in devices])

    return render_template("index.html", devices=devices, network=network, brands=brands)

@app.route("/export", methods=["POST"])
def export():
    network = request.form.get("network")
    if not network:
        return "Pas de réseau à exporter", 400

    devices = get_arp_devices(network)
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["IP", "MAC", "Marque", "Ping"])
    for device in devices:
        writer.writerow([device["ip"], device["mac"], device["marque"], "🟢" if device["reachable"] else "🔴"])

    output.seek(0)
    return Response(output, mimetype="text/csv",
                    headers={"Content-Disposition": "attachment; filename=scan_result.csv"})

if __name__ == "__main__":
    app.run(debug=True)
