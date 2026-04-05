# My CyberSecurity Store

> A personal knowledge base covering cybersecurity, bug bounty hunting, programming, and more — aggregated from various sources. Contributions are welcome!

---

## Table of Contents

- [WSL Setup](#wsl-setup)
- [Books](#books)
  - [Security & Hacking Books](#security--hacking-books)
  - [Self-Help Books](#self-help-books)
- [Bug Bounty Material](#bug-bounty-material)
  - [Methodology](#methodology)
  - [Vulnerabilities](#vulnerabilities)
  - [Tools](#bug-bounty-tools)
  - [Report Templates](#vulnerability-report-templates)
  - [Platforms](#bug-bounty-platforms)
- [People to Follow](#people-to-follow)
- [Learning Resources](#learning-resources)
  - [Roadmap](#roadmap)
  - [Linux](#learn-linux)
  - [Programming Languages](#learn-programming-languages)
  - [Languages for CyberSec](#languages-required-in-cybersec)
  - [Learning Platforms](#top-platforms-to-learn-any-programming-language)
  - [Practice & CTF](#practice--ctf-platforms)
  - [Certifications](#certifications)
  - [BurpSuite](#learn-burpsuite)
  - [Common Tools](#common-cybersec-tools)
  - [Other Topics](#other-topics)
- [CMS Pentesting](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/CMS%20Pentesting/readme.md)
- [Dumps & Leaks](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/tree/main/Dumps%20%26%20Leaks)

---

## WSL Setup

### 1. Installation

**Step 1.1** — Enable these two features via **Windows Features**:
- Windows Subsystem for Linux
- Virtual Machine Platform

**Step 1.2** — Open CMD as Administrator and run:
```
wsl --install
```

**Step 1.3** — Restart your PC.

**Step 1.4** — Go to the Microsoft Store and install:
- Windows Subsystem for Linux
- Your preferred Linux distro (Ubuntu, Kali Linux, Debian, Arch, etc.)

**Step 1.5** — Open the Linux app and complete the distro setup.

**Step 1.6** — Restart your PC. Installation complete.

---

### 2. Useful WSL Commands

| Command | Description |
|---------|-------------|
| `wsl --update` | Update WSL version |
| `wsl --version` / `-v` | Show WSL/kernel version info |
| `wsl --list` / `-l` | List all installed distributions |
| `wsl -l --all` | List all distros including pending install/uninstall |
| `wsl -l --running` | List only currently running distros |
| `wsl -l --quiet` / `-q` | Show only distribution names |
| `wsl -l --verbose` / `-v` | Detailed info on all distributions |
| `wsl -l --online` / `-o` | Show available distros for install |
| `wsl --set-default` / `-s <Distro>` | Set default distribution |

---

### 3. WSLg / Win-KeX Setup

**Install:**
1. Open your Linux distro and update/upgrade: `sudo apt update && sudo apt upgrade`
2. Install Win-KeX: `sudo apt install kali-win-kex`
3. Fill in required info, then start GUI with: `kex`

**Modes:**

| Flag | Mode |
|------|------|
| *(none)* | Window Mode (default) |
| `--esm` | Enhanced Session Mode (RDP) |
| `--sl` | Seamless Mode |
| `--win` | Window Mode (explicit) |

**Commands:**

| Command | Action |
|---------|--------|
| `--start` | Start Win-KeX server |
| `--stop` | Stop Win-KeX server |
| `--status` | Show server status |
| `--kill` | Kill server and all related processes |
| `--passwd` | Set server password |
| `--version` | Display Win-KeX version |

**Examples:**
```bash
kex -s                # Window mode with sound
kex --sl -s           # Seamless mode with sound
kex --esm -i -s       # Enhanced Session Mode (ARM workaround) with sound
sudo kex              # Start as root in window mode
```

---

## Books

### Security & Hacking Books

| # | Book | Recommended |
|---|------|-------------|
| 1 | [Cyberjutsu](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/Cyberjutsu.pdf) | No |
| 2 | [Black Hat Go](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/Black-Hat-Go.pdf) | Yes |
| 3 | [Violent Python](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/Violent%20Python.pdf) | Yes |
| 4 | [Black Hat Bash](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/Black-Hat-Bash.pdf) | Yes |
| 5 | [Black Hat GraphQL](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/BlackHat%20GraphQL.pdf) | Yes |
| 6 | [Bash Cheat Sheet](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/bash_cheat_sheet.pdf) | Yes |
| 7 | [Rust Programming](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/No-Starch-Press-The-Rust.pdf) | Yes |
| 8 | [Make Python Talk](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/make-python-talk.pdf) | Yes |
| 9 | [Zseano's Methodology](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/zseanos-methodology.pdf) | Yes |
| 10 | [Bug Bounty Bootcamp](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/bug-bounty-bootcamp.pdf) | Yes |
| 11 | [A Bug Hunter's Diary](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/a%20bug%20hunters%20diary.pdf) | No |
| 12 | [JavaScript Security](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/JavaScript%20Security.pdf) | No |
| 13 | [Build an HTML5 Game](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/Build%20an%20HTML5%20Game.pdf) | Yes |
| 14 | [Red Team Field Manual](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/rtfm-red-team-field-manual.pdf) | Yes |
| 15 | [Blue Team Field Manual](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/Blue%20Team%20Field%20Manual.pdf) | Yes |
| 16 | [The Linux Command Line](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/The-Linux-Command-Line.pdf) | Yes |
| 17 | [Linux Basics for Hackers](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/linux-basics-for-hackers.pdf) | Yes |
| 18 | [Attacking Network Protocols](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/attacking%20network%20protocols.pdf) | No |
| 19 | [Hacking APIs](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/Hacking%20APIs%20-%20Early%20Access.pdf) | Yes |
| 20 | [Web Security for Developers](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/websecurityfordevelopers.pdf) | No |
| 21 | [Pentesting Azure Applications](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/pentesting%20azure%20applications.pdf) | Yes |
| 22 | [Black Hat Python, 2nd Edition](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/Black%20Hat%20Python.pdf) | Yes |
| 23 | [How Cybersecurity Really Works](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/how-cybersecurity-really-works.pdf) | No |
| 24 | [Beyond the Basic Stuff with Python](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/Beyond-the-Basic-Stuff-with-Python.pdf) | Yes |
| 25 | [Learn Windows PowerShell in a Month of Lunches](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/learn-windows-powershell-in-a-month-of-lunches.pdf) | Yes |
| 26 | [Real-World Bug Hunting](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/Real-World%20Bug%20Hunting%20-%20A%20Field%20Guide%20to%20Web%20Hacking.pdf) | Yes |
| 27 | [Penetration Testing — Hands-on Intro to Hacking](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/Penetration%20Testing%20-%20A%20hands-on%20introduction%20to%20Hacking.pdf) | Yes |
| 28 | [The Hacker Playbook 3](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/The%20Hacker%20Playbook%203%20-%20Practical%20Guide%20To%20Penetration%20Testing.pdf) | No |
| 29 | [Enumerating Esoteric Attack Surfaces — Jann Moon](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/Enumerating%20Esoteric%20Attack%20Surfaces%20by%20Jann%20Moon.pdf) | No |
| 30 | [Practical Packet Analysis](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/practical%20packet%20analysis%203rd%20edition.pdf) | Yes |
| 31 | [Wicked Cool Shell Scripts](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/Wicked%20Cool%20Shell%20Scripts.pdf) | Yes |
| 32 | [Wicked Cool Perl Scripts](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/Wicked%20Cool%20Perl%20Scripts.pdf) | Yes |
| 33 | [Wicked Cool Ruby Scripts](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/wicked-cool-ruby-scripts.pdf) | Yes |
| 34 | [Perl One-Liners](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/perl-one-liners.pdf) | Yes |
| 35 | [The Book of Ruby](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/the-book-of-ruby.pdf) | Yes |
| 36 | [Ruby by Example](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/Ruby%20by%20Example.pdf) | No |
| 37 | [PowerShell for Sysadmins](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/PowerShell_for_Sysadmins.pdf) | Yes |
| 38 | [Webbots, Spiders, and Screen Scrapers](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/Webbots%2C%20Spiders%2C%20and%20Screen%20Scrapers.pdf) | — |
| 39 | [Mining Social Media](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/mining-social-media.pdf) | Yes |
| 40 | [How Linux Works](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/How-Linux-Works.pdf) | Yes |
| 41 | [Mastering Modern Web Penetration Testing](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/Mastering%20Modern%20Web%20Penetration%20Testing.pdf) | No |
| 42 | [The Tangled Web](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Books/The%20tangled%20Web_%20a%20guide%20to%20securing%20modern%20Web%20applications.pdf) | No |

---

### Self-Help Books

| # | Book |
|---|------|
| 1 | [12 Rules for Life](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Self%20Help%20Books/12-Rules-for-Life.pdf) |
| 2 | [Atomic Habits](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Self%20Help%20Books/Atomic%20Habits.pdf) |
| 3 | [Build, Don't Talk](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Self%20Help%20Books/Build_Dont_Talk.pdf) |
| 4 | [Do Epic Shit](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Self%20Help%20Books/DoEpicShit.pdf) |
| 5 | [Don't Believe Everything You Think](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Self%20Help%20Books/Dont%20Believe%20Everything%20You%20Think.pdf) |
| 6 | [How to Win Friends & Influence People](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Self%20Help%20Books/How%20to%20win%20in%20friends.pdf) |
| 7 | [Ikigai](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Self%20Help%20Books/Ikigai.pdf) |
| 8 | [Meditations — Marcus Aurelius](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Self%20Help%20Books/Marcus-Aurelius-Meditations.pdf) |
| 9 | [Think Straight](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Self%20Help%20Books/Think_Straight.pdf) |
| 10 | [Can't Hurt Me](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Self%20Help%20Books/cant%20hurt%20me.pdf) |
| 11 | [Do It Today](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Self%20Help%20Books/do%20it%20today%20.pdf) |
| 12 | [Eat That Frog](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Self%20Help%20Books/eat%20the%20frog.pdf) |

---

## Bug Bounty Material

### Methodology

- Always try to chain vulnerabilities together to increase severity
- Finding a vulnerability is half the battle — writing a clear, compelling report is the other half
- Use a proxy (Burp Suite) and monitor all resources loaded when visiting a target

---

### Vulnerabilities

#### 1. XSS (Cross-Site Scripting)
- Find parameters, endpoints, and input fields
- Try different payloads based on the WAF in place
- `javascript:` and `<img>` payloads are most common

#### 2. CSRF (Cross-Site Request Forgery)
- Allows an attacker to perform actions on behalf of a victim
- Common targets: delete account, change email/password, add roles, modify profile info
- **Bypass techniques:**
  - Delete the token parameter entirely
  - Send a blank token value
  - Switch request from POST to GET
  - Change body encoding
  - Replace token with a random value
  - Remove the `Referer` header or use `<meta name="referrer" content="no-referrer">`
  - Use another user's token
  - Modify one character in the token

#### 3. IDOR (Insecure Direct Object Reference)
- Exploited by manipulating object references (IDs) in requests to access unauthorized data
- Always requires two accounts for ID-based testing
- Copy a victim's resource ID to your attacker account — if the response is 200, IDOR confirmed
- **ID types to look for:**
  - Decimal (< 8 digits)
  - Decimal (8+ digits)
  - Name / email
  - UUID
  - Hex (8+ digits)
  - Bruteforceable / non-bruteforceable values
  - Hash

#### 4. SSRF (Server-Side Request Forgery)
- Forces the server to make HTTP requests to unintended internal or external locations

#### 5. Open Redirect
- Commonly found on login/logout flows that redirect to a URL parameter
- Monitor redirect behavior in Burp Suite
- [Example file](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Bug%20Bounty/Open-Redirect-Example.txt)

#### 6. Account Takeover
- Most common entry point: password reset functionality
- **Methods:**
  - OAuth misconfiguration
  - JWT verification bypass
  - No rate limit on OTP verification
  - OTP bypass via response manipulation
  - IDOR on account endpoints

#### 7. Information Disclosure
- Often triggered by IDOR or unsecured endpoints
- Check response bodies and source code for hardcoded values, tokens, or internal paths

#### 8. File Upload Vulnerability
- Commonly found in support chat or profile picture upload features
- Upload a normal file and intercept — swap the content for malicious data via Burp Suite
- Changing the MIME type via DevTools (e.g., image → text) can sometimes trigger XSS if backend validation is weak

#### 9. HTTP Parameter Pollution
- Inject duplicate parameters to confuse backend validation
- Example: `?uid=victim&uid=attacker` — some backends process the last value, others the first

---

### Bug Bounty Tools

| # | Category | Tool | Link |
|---|----------|------|------|
| 1 | **DNS Discovery** | Sublist3r | [github.com/aboul3la/Sublist3r](https://github.com/aboul3la/Sublist3r) |
| | | enumall | [github.com/jhaddix/domain](https://github.com/jhaddix/domain/) |
| | | massdns | [github.com/blechschmidt/massdns](https://github.com/blechschmidt/massdns) |
| | | altdns | [github.com/infosec-au/altdns](https://github.com/infosec-au/altdns) |
| | | dns-parallel-prober | [github.com/lorenzog/dns-parallel-prober](https://github.com/lorenzog/dns-parallel-prober) |
| | | dnscan | [github.com/rbsec/dnscan](https://github.com/rbsec/dnscan) |
| 2 | **Port Scan** | nmap | [nmap.org](https://nmap.org) |
| | | masscan | [github.com/robertdavidgraham/masscan](https://github.com/robertdavidgraham/masscan) |
| | | RustScan | [github.com/RustScan/RustScan](https://github.com/RustScan/RustScan) |
| 3 | **Screenshots** | EyeWitness | [github.com/ChrisTruncer/EyeWitness](https://github.com/ChrisTruncer/EyeWitness) |
| | | httpscreenshot | [github.com/breenmachine/httpscreenshot](https://github.com/breenmachine/httpscreenshot/) |
| 4 | **Web Discovery** | DirBuster | [sourceforge.net/projects/dirbuster](https://sourceforge.net/projects/dirbuster/) |
| | | gobuster | [github.com/OJ/gobuster](https://github.com/OJ/gobuster) |
| | | wfuzz | [github.com/xmendez/wfuzz](https://github.com/xmendez/wfuzz/) |
| | | FFUF | [github.com/ffuf/ffuf](https://github.com/ffuf/ffuf) |
| | | DirSearch | [github.com/maurosoria/dirsearch](https://github.com/maurosoria/dirsearch) |
| | | hydra | [github.com/vanhauser-thc/thc-hydra](https://github.com/vanhauser-thc/thc-hydra) |
| | | truffleHog | [github.com/dxa4481/truffleHog](https://github.com/dxa4481/truffleHog) |
| 5 | **Google Dorks** | pentest-tools | [pentest-tools.com](https://pentest-tools.com/information-gathering/google-hacking) |
| | | taksec | [taksec.github.io/google-dorks-bug-bounty](https://taksec.github.io/google-dorks-bug-bounty/) |
| | | faisalahmed | [dorks.faisalahmed.me](https://dorks.faisalahmed.me/) |
| | | nitinyadav00 | [nitinyadav00.github.io/Bug-Bounty-Search-Engine](https://nitinyadav00.github.io/Bug-Bounty-Search-Engine/) |
| 6 | **Params** | parameth | [github.com/mak-/parameth](https://github.com/mak-/parameth) |
| 7 | **Wayback** | Wayback Machine | [web.archive.org](https://web.archive.org) |
| | | waybackurls | [github.com/tomnomnom/waybackurls](https://github.com/tomnomnom/waybackurls) |
| | | gau | [github.com/lc/gau](https://github.com/lc/gau) |
| 8 | **Tech Detection** | Wappalyzer | [wappalyzer.com](https://wappalyzer.com/) |
| | | wappalyzer-cli | [github.com/gokulapap/wappalyzer-cli](https://github.com/gokulapap/wappalyzer-cli) |
| 9 | **CMS** | WPScan | [wpscan.org](https://wpscan.org/) |
| | | CMSMap | [github.com/Dionach/CMSmap](https://github.com/Dionach/CMSmap) |
| | | joomscan | [github.com/rezasp/joomscan](https://github.com/rezasp/joomscan) |
| 10 | **JWT** | JWT Toolkit | [github.com/ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool) |
| 11 | **WAF** | wafw00f | [github.com/EnableSecurity/wafw00f](https://github.com/EnableSecurity/wafw00f) |
| 12 | **GraphQL** | GraphQLmap | [github.com/swisskyrepo/GraphQLmap](https://github.com/swisskyrepo/GraphQLmap) |
| | | InQL v5.0 | [github.com/doyensec/inql](https://github.com/doyensec/inql) |
| | | clairvoyancex | [github.com/y0k4i-1337/clairvoyancex](https://github.com/y0k4i-1337/clairvoyancex) |
| | | CrackQL | [github.com/nicholasaleks/CrackQL](https://github.com/nicholasaleks/CrackQL) |
| | | graphql-voyager | [graphql-kit.com/graphql-voyager](https://graphql-kit.com/graphql-voyager/) |

---

### Vulnerability Report Templates

| Template | Link |
|----------|------|
| No Rate Limit | [View Report](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/blob/main/Bug%20Bounty/Vulnerability%20Report%20format/No%20Rate%20Limit%20Vulnerability.docx) |

---

### Bug Bounty Platforms

| # | Platform | Link |
|---|----------|------|
| 1 | HackerOne | [hackerone.com](https://hackerone.com/) |
| 2 | Bugcrowd | [bugcrowd.com](https://www.bugcrowd.com/) |
| 3 | Open Bug Bounty | [openbugbounty.org](https://www.openbugbounty.org/) |
| 4 | Intigriti | [intigriti.com](https://www.intigriti.com/) |
| 5 | Detectify | [detectify.com](https://detectify.com/) |
| 6 | Synack | [synack.com](https://www.synack.com/) |
| 7 | Cobalt | [cobalt.io](https://cobalt.io/) |
| 8 | Zerocopter | [zerocopter.com](https://www.zerocopter.com/) |
| 9 | YesWeHack | [yeswehack.com](https://www.yeswehack.com/) |
| 10 | HackenProof | [hackenproof.com](https://hackenproof.com/) |
| 11 | Vulnerability Lab | [vulnerability-lab.com](https://www.vulnerability-lab.com/) |
| 12 | AntiHack | [antihack.me](https://antihack.me/) |
| 13 | FireBounty | [firebounty.com](https://firebounty.com/) |
| 14 | BugBounty.jp | [bugbounty.jp](https://bugbounty.jp/) |
| 15 | CyberArmy ID | [cyberarmy.id](https://www.cyberarmy.id/) |
| 16 | Safe Hats | [safehats.com](https://safehats.com/) |
| 17 | Red Storm | [redstorm.io](https://redstorm.io/) |
| 18 | Yogosha | [yogosha.com](https://www.yogosha.com/) |
| 19 | Bugbase | [bugbase.io](https://bugbase.io/) |

---

## People to Follow

- [Hackers on Twitter / X](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/tree/main/Hackers%20To%20Follow)
- [Hackers on Medium](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/tree/main/Hackers%20To%20Follow)
- [Hackers on YouTube](https://github.com/cookiesn1ffer/My-CyberSecurity-Store/tree/main/Hackers%20To%20Follow)

---

## Learning Resources

### Roadmap

All resources, CTF platforms, programming guides, and YouTube channels related to cybersecurity are documented in the [Roadmap](./Roadmap) folder.

---

### Learn Linux

1. **Command Line**
   - [The Cyber Mentor](https://www.youtube.com/watch?v=U1w4T03B30I&list=LL&index=386)
   - [freeCodeCamp](https://www.youtube.com/watch?v=ZtqBQ68cfJc&list=LL&index=404)
   - [HackerSploit](https://www.youtube.com/watch?v=rZsJieGi8os&list=LL&index=406)

2. **File System**
   - [NeuralNine](https://www.youtube.com/watch?v=BUnb1PKKMBA)
   - [Edureka](https://www.youtube.com/watch?v=ePN5igV9ZpY&list=LL&index=235)
   - [NetworkChuck](https://www.youtube.com/watch?v=A3G-3hp88mo&list=LL&index=399)

3. **Reference Sites**
   - [Linux Journey](https://linuxjourney.com/)
   - [Explain Shell](https://explainshell.com/)

---

### Learn Programming Languages

- **C++** — [GeeksForGeeks Examples](https://www.geeksforgeeks.org/c-programming-examples/) | [Top 50 Array Qs](https://www.geeksforgeeks.org/top-50-array-coding-problems-for-interviews/) | [Top 50 String Qs](https://www.geeksforgeeks.org/top-50-string-coding-problems-for-interviews/)
- **Java** — [GeeksForGeeks Examples](https://www.geeksforgeeks.org/java-programming-examples/)
- **Python** — [GeeksForGeeks Examples](https://www.geeksforgeeks.org/python-programming-examples/) | [Tutorial](https://www.geeksforgeeks.org/python-programming-language/learn-python-tutorial/) | [Projects](https://www.geeksforgeeks.org/python-projects-beginner-to-advanced/)
- **HTML/CSS** — [LoveBabbar](https://www.youtube.com/watch?v=k7ELO356Npo) | [CodeWithHarry](https://www.youtube.com/watch?v=BsDoLVMnmZs) | [SuperSimpleDev](https://www.youtube.com/watch?v=G3e-cpL7ofc) | [BroCode](https://www.youtube.com/watch?v=HGTJBPNC-Gw)
- **SQL** — [BroCode](https://www.youtube.com/watch?v=5OdVJbNCSso) | [AapnaCollege](https://www.youtube.com/watch?v=hlGoQC332VM)

---

### Languages Required in CyberSec

| Category | Languages |
|----------|-----------|
| Web Development | HTML, CSS, JavaScript, PHP, MySQL, TypeScript |
| General Programming | C, C++, Java, Python, Rust, Go, C# |
| Scripting | Bash, PowerShell, Ruby, Perl, Lua, Python, VBScript |
| Config / Markup | YAML, JSON, XML, Markdown, TOML |

---

### Top Platforms to Learn Any Programming Language

1. [JavaTpoint](https://www.javatpoint.com/)
2. [W3Schools](https://www.w3schools.com/)
3. [GeeksforGeeks](https://www.geeksforgeeks.org/)
4. [Tutorialspoint](https://www.tutorialspoint.com/)
5. [HackerRank](https://www.hackerrank.com/)
6. [Programiz](https://www.programiz.com/)

---

### Practice & CTF Platforms

| Platform | Focus |
|----------|-------|
| [TryHackMe](https://tryhackme.com/) | Beginner-friendly, guided rooms |
| [HackTheBox Labs](https://app.hackthebox.com/home) | Intermediate/advanced machines |
| [HTB Academy](https://academy.hackthebox.com/) | Structured learning paths |
| [PortSwigger Web Academy](https://portswigger.net/) | Web security labs |
| [PentesterLab](https://www.pentesterlab.com/) | Web & code review challenges |
| [PicoCTF](https://picoctf.org/) | CTF competitions |
| [OverTheWire](https://overthewire.org/wargames/) | Linux wargames |
| [VulnHub](https://www.vulnhub.com/) | Downloadable vulnerable VMs |
| [Exploit Education](https://exploit.education/) | Binary exploitation |
| [RootMe](https://www.root-me.org/) | Multi-category challenges |
| [HackingHub](https://www.hackinghub.io/) | Web app hacking |
| [Pwned Labs](https://pwnedlabs.io/) | Cloud & AD labs |
| [HBH.sh](https://hbh.sh/home) | Hacking challenges |
| [API Security University](https://www.apisecuniversity.com/) | API security |
| [CompTIA Security+ Labs](https://www.101labs.net/comptia-security/) | Cert prep labs |
| [Trailhead (Salesforce)](https://trailhead.salesforce.com/en/career-path/cybersecurity/) | Cloud security path |
| [awesome-vulnerable-apps](https://github.com/vavkamil/awesome-vulnerable-apps) | Curated vuln app list |
| [awesome-hacker-search-engines](https://github.com/edoardottt/awesome-hacker-search-engines) | OSINT & recon tools |
| [THM Free Labs List](https://github.com/Raunaksplanet/THM-CTF-Time/tree/main) | TryHackMe free rooms |

---

### Certifications

| Vendor | Certifications |
|--------|---------------|
| CompTIA | A+, Network+, Security+, Linux+, PenTest+, CySA+, CASP+, ITF+ |
| EC-Council | CEH |
| INE Security | eJPT, eWPTX |

---

### Learn BurpSuite

- [Bitten Tech](https://www.youtube.com/playlist?list=PLkW9FMxqUvybgx3pI9x9HyU-_HcJJFWQY)
- [Ethical Sharmaji](https://www.youtube.com/watch?v=mK3Hr6ktgNg&t=4118s)
- [hackbin](https://www.youtube.com/watch?v=eKPpGLn9G3w&t=185s)
- [David Bombal](https://www.youtube.com/watch?v=IWWYNDiwYOA)
- [PortSwigger Playlist 1](https://www.youtube.com/playlist?list=PLoX0sUafNGbEXtfr-f4n0g4AqzU-CDvcQ)
- [PortSwigger Playlist 2](https://www.youtube.com/playlist?list=PLSbrmTUy4daN1ep7pkBZw4PRRmx7F0EaS)
- [Cyberwings Security](https://www.youtube.com/playlist?list=PLa2xctTiNSCjVzFfxTn_UKkd-sS34EQaF)
- [Technical MotaBhai](https://www.youtube.com/playlist?list=PLBCWFgREB971jxEXKbiAZSNQZqIxH9L47)

---

### Common CyberSec Tools

| Category | Tools |
|----------|-------|
| Exploitation | Metasploit, SQLMap, Aircrack-ng |
| Password Cracking | John the Ripper, Hashcat, Hydra, Crunch |
| Recon & OSINT | Maltego, Shodan, Subfinder, Sublist3r |
| Web Testing | Burp Suite, OWASP ZAP, Nikto, FFUF, FeroxBuster, DirSearch |
| Network | Nmap, Masscan, RustScan, Netcat, Wireshark, Snort |
| Scanning | Katana, HTTPX, wafw00f |
| Steganography | Steghide, Binwalk |
| Identification | Hashid, Wappalyzer |
| File Search | which, whereis, find, locate |

---

### Other Topics

- [Reverse Shell vs Bind Shell](https://medium.com/bugbountywriteup/reverse-shell-vs-bind-shell-d5a1e80b6a6c)
- [Cybersecurity Roadmap by TCM Security (2023)](https://tcm-sec.com/so-you-want-to-be-a-hacker-2023-edition/)
- [MySQL & SQL — AapnaCollege](https://www.youtube.com/watch?v=hlGoQC332VM&list=LL&index=9&t=2s)
- **The Cyber Expert (TCE) Playlists:**
  - [Network Pentesting](https://www.youtube.com/playlist?list=PL-DxAN1jsRa-zHjDOfbpi6OAVwpCkyRYn)
  - [Reverse Engineering](https://www.youtube.com/playlist?list=PL-DxAN1jsRa9151ezNuCbh7UkGS0bMPdw)
  - [Binary Exploitation](https://www.youtube.com/playlist?list=PL-DxAN1jsRa9151ezNuCbh7UkGS0bMPdw)
