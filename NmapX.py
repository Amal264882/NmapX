#!/usr/bin/env python3

import os
import subprocess
import multiprocessing
from multiprocessing import Manager
from tqdm import tqdm
import time

BANNER = r"""
███╗   ██╗███╗   ███╗ █████╗ ██████╗ ██╗  ██╗
████╗  ██║████╗ ████║██╔══██╗██╔══██╗╚██╗██╔╝
██╔██╗ ██║██╔████╔██║███████║██████╔╝ ╚███╔╝
██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝  ██╔██╗
██║ ╚████║██║ ╚═╝ ██║██║  ██║██║     ██╔╝ ██╗
╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝

        NmapX – Extended Parallel Nmap Scanner
        Author: Amal Johns
"""

def scan_ip(ip):
    output_file = f"{ip}.txt"

    # Skip if already scanned
    if os.path.exists(output_file):
        return f"[SKIP] {ip} already scanned"

    nmap_cmd = [
        "nmap",
        "-sC",
        "-sV",
        "-O",
        ip,
        "-oN",
        output_file
    ]

    try:
        process = subprocess.Popen(
            nmap_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        with open(output_file, "w") as f:
            for line in process.stdout:
                print(f"[{ip}] {line.strip()}")
                f.write(line)

        process.wait()
        return f"[DONE] {ip}"

    except Exception as e:
        return f"[ERROR] {ip}: {e}"


def main():
    os.system("clear")
    print(BANNER)
    time.sleep(1)

    filename = input("Enter file name containing IPs: ").strip()

    if not os.path.exists(filename):
        print("[-] File not found")
        return

    with open(filename, "r") as f:
        ips = sorted(set(line.strip() for line in f if line.strip()))

    total_ips = len(ips)
    if total_ips == 0:
        print("[-] No valid IPs found")
        return

    cpu_count = multiprocessing.cpu_count()
    max_processes = max(1, cpu_count - 1)

    print(f"\n[INFO] Total IPs   : {total_ips}")
    print(f"[INFO] CPU Cores  : {cpu_count}")
    print(f"[INFO] Workers   : {max_processes}\n")

    with multiprocessing.Pool(processes=max_processes) as pool:
        for result in tqdm(
            pool.imap_unordered(scan_ip, ips),
            total=total_ips,
            desc="Scanning",
            unit="host"
        ):
            print(result)

    print("\n[✔] All scans completed")


if __name__ == "__main__":
    main()

