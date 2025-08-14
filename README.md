# 🦉 OWL-CMS Detector

A powerful CMS & admin panel path scanner for reconnaissance and vulnerability assessments.  
Created by **khaled.s.haddad** | 🌐 [khaledhaddad.tech](https://khaledhaddad.tech)

---

## 🧠 What It Does

- 🔍 Detects **Content Management Systems (CMS)** such as WordPress, Joomla, Drupal, Magento, etc.
- 🔐 Enumerates **common admin or login panels** (e.g., `/admin`, `/wp-login.php`, `/cpanel`).
- 🌐 Tries both `http` and `https` protocols automatically.
- 💥 Useful for bug bounty, red teaming, and penetration testing.

---

## 🚀 Usage

```bash
python3 owl-cms-scanner.py example.com
```

Replace `example.com` with the domain you want to analyze.

---

## 🧪 Features

- 🧠 Intelligent CMS fingerprinting based on HTML content and path patterns.
- 🔀 Checks multiple CMS-specific paths and keywords.
- ⚡ Fast probing using a custom User-Agent and timeout.
- 🛡️ Bypasses basic bot filters via header mimicry.

---

## 🧾 Example Output

```bash
[~] Scanning CMS on example.com...

[+] Detected CMS: WordPress at https://example.com/wp-login.php

[~] Checking common admin paths on example.com...

[+] Found admin/login path: https://example.com/admin
[+] Found admin/login path: https://example.com/wp-admin
```

---

## 📚 Supported CMS

- WordPress
- Joomla
- Drupal
- Magento
- PrestaShop
- OpenCart
- TYPO3
- Ghost
- MediaWiki
- Concrete5
- SilverStripe
- Shopify
- Wix
- Squarespace

---

## ⚙️ How It Works

1. Loops over a database of CMS-specific paths.
2. Sends GET requests to each path using `requests`.
3. Matches HTML content with known CMS fingerprints using regex.
4. Also checks a list of **common admin login paths**.

---

## 🐍 Dependencies

- Python 3.x
- `requests` module (install via `pip install requests`)

---

## 📜 License

MIT License

---

## 👨‍💻 Author

**khaled.s.haddad**  
🌍 [khaledhaddad.tech](https://khaledhaddad.tech)

