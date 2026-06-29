![Made with Markdown](https://img.shields.io/badge/Docs-Markdown-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)

# Cybersecurity Portfolio & CTF Handbook

A collection of CTF writeups, reusable tooling, scripts, and technical documentation developed throughout my cybersecurity learning.

## Repository Structure

```text
cyber-lab/
├── .gitignore
├── LICENSE
├── README.md
├── archive/
│   └── tryhackme/
├── ctf/
│   ├── binary_exploitation/
│   │   ├── sandbox/
│   │   └── writeups/
│   ├── cryptography/
│   │   ├── sandbox/
│   │   └── writeups/
│   ├── forensics/
│   │   ├── sandbox/
│   │   └── writeups/
│   ├── misc/
│   │   ├── sandbox/
│   │   └── writeups/
│   ├── reverse_engineering/
│   │   ├── sandbox/
│   │   └── writeups/
│   └── web_exploitation/
│       ├── sandbox/
│       └── writeups/
└── utils/
```

## About This Repository

This repository serves as both my long-term cybersecurity knowledge base and my active CTF workspace.

+ **`archive/`**
	Older material retained for reference. This currently contains my early TryHackMe notes, created while building good documentation habits and foundational cybersecurity knowledge.
* **`ctf/`**
    The active training arena. Organized by domain, this contains all challenge materials and solutions for current CTF platforms (such as CyLabs) and live competitions.
    * **`writeups/`**: Dedicated folders for complex, advanced challenges. Each challenge gets its own directory containing a micro writeup, and the solve script, as well as any downloaded challenge artifacts.
    * **`sandbox/`**: The working directory for quick solves. A flat collection of fast Python scripts, loose notes, tool outputs, one-liners, etc...
* **`utils/`**
    A directory of generic, reusable boilerplate scripts (e.g., automated SQL injection frameworks, RSA math templates, comprehensive nmap scan) designed to be accessible easily when solving challenges.

## Ethical Notice

All scripts, write-ups, and techniques documented in this repository are for educational purposes and authorized Capture The Flag (CTF) competitions only. Do not use these tools or methodologies against systems or networks without explicit, written permission from the owner. 

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

- **Author:** Daniel Haynes  
- **Alias:** *Xenithu* (username on most platforms)
- **GitHub:** https://github.com/danielhaynes965-cyber  
- **LinkedIn:** https://www.linkedin.com/in/daniel-h-506933392
