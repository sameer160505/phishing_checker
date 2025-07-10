# Phishing URL Checker 🔐

A lightweight Python desktop application to check whether a URL might be a phishing link. The tool uses rule-based detection and a simple, dark-themed graphical user interface (GUI) built with Tkinter.

## Features

✅ Checks URLs for common phishing indicators:
- Numeric IP addresses instead of domain names
- Excessive hyphens in the URL
- Presence of the `@` symbol, which can obscure the true link destination
- Long URLs (over 75 characters)
- Suspicious words like “login,” “verify,” “bank,” “update,” and similar terms

✅ Displays clear results:
- 🔴 **Likely a phishing site** if two or more indicators are detected
- 🟢 **URL looks safe** if fewer signs are present

✅ Provides detailed reasons explaining why a URL is considered suspicious.

✅ User-friendly dark-themed interface for easy readability.

