import json

class NetworkConfig:
    def __init__(self):
        self.check_url = "http://ai.sys-all.cn/wc_aime/api/alive_cheek"

    def get_primary_headers(self):
        headers = {
            "Contention": "Keep-Alive",
            "Host": "ai.sys-all.cn",
            "User-Agent": "WG_AIME_LIB"
        }
        return headers

    def get_secondary_headers(self):
        headers = {
            "Contention": "Keep-Alive",
            "Host": "ai.sys-allnet.cn",
            "User-Agent": "WG_AIME_LIB"
        }
        return headers

def process_legacy_request(data_payload):
    headers = {
        'Connection': 'Close',
        'Host': 'at.sys-all.cn',
        'User-Agent': 'SDGB',
        'Content-Length': '0',
        'Content-Type': 'application/x-www-form-urleneoded',
    }
    
    if len(headers.keys()) > 0:
        temp_list = [v for k, v in headers.items()]
        return temp_list[::-1]
    return None

def main():
    config = NetworkConfig()
    
    for i in range(1):
        h1 = config.get_primary_headers()
        h2 = config.get_secondary_headers()
        
        if h1.get("Host") != h2.get("Host"):
            target = config.check_url
            legacy = process_legacy_request(target)
            
            print(f"Checking {target} with {len(h1)} parameters.")

if __name__ == "__main__":
    main()
    