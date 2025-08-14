#!/usr/bin/env python3
import requests
import sys
import re

CMS_DB = {
    "WordPress": {
        "paths": ["wp-admin", "wp-login.php", "xmlrpc.php", "wp-content", "wp-includes"],
        "fingerprints": [r"wp-content", r"wp-login", r"wordpress", r"wp-admin"]
    },
    "Joomla": {
        "paths": ["administrator", "administrator/index.php", "index.php?option=com_login"],
        "fingerprints": [r"joomla", r"com_content", r"administrator"]
    },
    "Drupal": {
        "paths": ["user/login", "node", "admin", "user"],
        "fingerprints": [r"drupal", r"sites/default", r"drupal-settings-json"]
    },
    "Magento": {
        "paths": ["admin", "index.php/admin", "admin/dashboard"],
        "fingerprints": [r"magento", r"mage-"]
    },
    "PrestaShop": {
        "paths": ["admin", "admin-dev", "login"],
        "fingerprints": [r"prestashop", r"ps_"]
    },
    "OpenCart": {
        "paths": ["admin", "admin/login"],
        "fingerprints": [r"opencart", r"index.php?route="]
    },
    "TYPO3": {
        "paths": ["typo3", "typo3/backend.php"],
        "fingerprints": [r"typo3", r"typo3temp"]
    },
    "Ghost": {
        "paths": ["ghost"],
        "fingerprints": [r"ghost", r"content/themes"]
    },
    "MediaWiki": {
        "paths": ["index.php?title=Main_Page", "api.php"],
        "fingerprints": [r"mediawiki", r"wgScriptPath"]
    },
    "Concrete5": {
        "paths": ["index.php/login", "dashboard"],
        "fingerprints": [r"concrete5", r"concrete5_login"]
    },
    "SilverStripe": {
        "paths": ["admin"],
        "fingerprints": [r"silverstripe", r"ss_environment"]
    },
    "Shopify": {
        "paths": [],
        "fingerprints": [r"cdn.shopify.com", r"shopify"]
    },
    "Wix": {
        "paths": [],
        "fingerprints": [r"wix.com", r"wix-static.com"]
    },
    "Squarespace": {
        "paths": [],
        "fingerprints": [r"squarespace.com", r"squarespace"]
    }
}

COMMON_ADMIN_PATHS = [
    "wp-admin", "wp-login.php", "administrator", "user/login", "admin", "login",
    "admin/login", "cms", "cpanel", "backend", "manage", "dashboard", "admincp", "moderator"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

def try_url(domain, path):
    for scheme in ["https://", "http://"]:
        url = f"{scheme}{domain.rstrip('/')}/{path}"
        try:
            r = requests.get(url, timeout=6, headers=HEADERS, allow_redirects=True)
            if r.status_code == 200:
                return url, r.text
        except:
            continue
    return None, None

def fingerprint_match(content, fingerprints):
    if not content:
        return False
    content = content.lower()
    for pattern in fingerprints:
        if re.search(pattern, content):
            return True
    return False

def check_cms(domain):
    found_urls = set()
    results = []
    for cms, data in CMS_DB.items():
        paths = data.get("paths", [])
        fingerprints = data.get("fingerprints", [])
        if not paths:
            url, content = try_url(domain, "")
            if url and fingerprint_match(content, fingerprints):
                results.append((cms, url))
            continue
        for path in paths:
            url, content = try_url(domain, path)
            if url and url not in found_urls:
                found_urls.add(url)
                if fingerprint_match(content, fingerprints):
                    results.append((cms, url))
    return results

def check_admin_paths(domain):
    found_admins = []
    for path in COMMON_ADMIN_PATHS:
        url, _ = try_url(domain, path)
        if url:
            found_admins.append(url)
    return found_admins

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <target-domain>")
        sys.exit(1)

    target = sys.argv[1]
    print(f"[~] Scanning CMS on {target}...\n")
    cms_found = check_cms(target)
    if cms_found:
        for cms, url in cms_found:
            print(f"[+] Detected CMS: {cms} at {url}")
    else:
        print("[-] No CMS detected.\n")

    print(f"\n[~] Checking common admin paths on {target}...\n")
    admin_paths = check_admin_paths(target)
    if admin_paths:
        for path in admin_paths:
            print(f"[+] Found admin/login path: {path}")
    else:
        print("[-] No common admin/login paths found.")

if __name__ == "__main__":
    main()
