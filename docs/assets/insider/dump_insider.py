#!/usr/bin/env python3
"""Dump artefak Chrome untuk challenge insider."""
import sqlite3
import json
from datetime import datetime, timezone, timedelta

BASE = "ChromeProfile/Default"

def q(db, sql):
    con = sqlite3.connect(f"file:{BASE}/{db}?mode=ro", uri=True)
    rows = list(con.execute(sql))
    con.close()
    return rows

def chrome_time(v):
    if not v:
        return "-"
    dt = datetime(1601, 1, 1, tzinfo=timezone.utc) + timedelta(microseconds=v)
    return dt.strftime("%Y-%m-%d %H:%M:%S UTC")

print("=== URL HISTORY (urut last_visit_time) ===")
for url, title, vc, lvt in q("History", "select url,title,visit_count,last_visit_time from urls order by last_visit_time"):
    print(f"{chrome_time(lvt)} | visit={vc} | {url} | {title}")

print("\n=== DOWNLOADS ===")
for row in q("History", "select target_path,total_bytes,start_time,mime_type,tab_url from downloads"):
    print(row[0], row[1], chrome_time(row[2]), row[3], row[4])

print("\n=== DOWNLOAD URL CHAINS ===")
for row in q("History", "select * from downloads_url_chains"):
    print(row)

print("\n=== KEYWORD SEARCH TERMS ===")
for row in q("History", "select term,url_id from keyword_search_terms"):
    print(row)

print("\n=== LOGIN DATA (username + ciphertext v10) ===")
for origin, user, pw, created, used in q("Login Data", "select origin_url,username_value,password_value,date_created,date_last_used from logins"):
    print(f"{origin} | user={user} | len={len(pw)} | prefix={pw[:3]!r} | created={chrome_time(created)} | used={chrome_time(used)}")
    print("  ciphertext:", pw.hex())

print("\n=== COOKIES ===")
for host, name, enc, created in q("Network/Cookies", "select host_key,name,encrypted_value,creation_utc from cookies"):
    print(f"{host} | {name} | len={len(enc)} | {enc.hex()}")

print("\n=== WEB DATA AUTOFILL ===")
for row in q("Web Data", "select name,value,count from autofill"):
    print(row)
