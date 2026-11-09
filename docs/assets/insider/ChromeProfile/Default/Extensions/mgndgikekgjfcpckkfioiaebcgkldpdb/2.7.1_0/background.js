// ZenVPN background service worker
const PROXY_CONFIG = {
  mode: "fixed_servers",
  rules: {
    singleProxy: { scheme: "http", host: "sg1.zenvpn.example", port: 8899 },
    bypassList: ["localhost", "127.0.0.1"]
  }
};

chrome.runtime.onInstalled.addListener(() => {
  chrome.proxy.settings.set({ value: PROXY_CONFIG, scope: "regular" });
});

chrome.runtime.onStartup.addListener(() => {
  chrome.proxy.settings.set({ value: PROXY_CONFIG, scope: "regular" });
});
