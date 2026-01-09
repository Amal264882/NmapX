# NmapX v1.0 🔍⚡

**NmapX** is a fast, multiprocessing-based network reconnaissance tool that extends Nmap by running multiple scans in parallel while preserving full Nmap capabilities.

Built for **penetration testers**, **red teamers**, and **security engineers** who need speed without sacrificing accuracy.

---

## 🚀 Features

- ✅ Parallel Nmap scanning using multiprocessing
- ✅ Full Nmap power (`-sC -sV -O`)
- ✅ Live scan output in terminal
- ✅ Automatic progress bar
- ✅ Skips already scanned hosts
- ✅ One output file per IP
- ✅ Clean, pentest-friendly design

---

## 🧠 Why NmapX?

Nmap flags can only go so far.  
**NmapX scales Nmap horizontally** by running multiple scans at once using Python multiprocessing.

This provides:
- Faster assessments on large networks
- Better CPU utilization
- Cleaner automation workflows

---

## 📦 Requirements

- Python **3.8+**
- Nmap **installed and accessible in PATH**

Install Python dependencies:
```bash
pip install -r requirements.txt
