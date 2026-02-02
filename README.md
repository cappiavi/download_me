![Alt](https://repobeats.axiom.co/api/embed/d162b37147fde7ecaabb9f3a19fe888938a3b17a.svg "Repobeats analytics image")

# DOWNLOAD ME

## Project Overview

**DOWNLOAD ME** is a Python-based command-line media downloader built on top of `yt-dlp`.  
It is designed to download videos and other media content from a wide range of websites by using **authenticated browser sessions** instead of public access links.

The project works by importing locally exported browser cookies, allowing the program to behave as if it were the logged-in user. This enables access to restricted, private, or account-based content that would otherwise be inaccessible.

The downloader supports **multi-threaded download sessions**, giving the user direct control over download speed, CPU usage, and network load. Higher thread counts increase performance but also increase the risk of triggering platform security mechanisms.

All cookies and session data remain **entirely local** to the user’s machine. No credentials, cookies, or personal data are uploaded, shared, or transmitted to any external service.

---

## Cookie File Naming Convention (CRITICAL REQUIREMENT)

For the program to correctly authenticate and access protected content, cookie files **must follow a strict naming convention**.  
The program does not infer or guess which cookies belong to which website. It relies entirely on the **filename** to determine which cookie file to load.

Incorrect naming will result in:
- Authentication failure
- Download errors
- Inability to access restricted content

---

### Required File Naming Format

```

<website_name>.txt

```

Where:
- `<website_name>` is the name of the website where the cookies were extracted
- The file extension **must be `.txt`**
- The filename should be simple, lowercase, and free of spaces or special characters

---

### Correct Naming Examples

| Website Source | Correct Filename |
|---------------|------------------|
| Facebook      | `facebook.txt`  |
| YouTube       | `youtube.txt`   |
| Twitter / X   | `twitter.txt`   |
| Instagram     | `instagram.txt` |
| TikTok        | `tiktok.txt`    |
| Reddit        | `reddit.txt`    |

---

### Incorrect Naming Examples

- `facebook_cookies.txt`
- `cookies.txt`
- `FB.txt`
- `my_facebook_account.txt`
- `youtube(1).txt`

These filenames may prevent the program from correctly identifying the intended authentication session.

---

## Step-by-Step: Preparing the Cookie File

1. Open a supported browser (Brave or Chrome recommended)
2. Navigate to the target website
3. Log in to your account if required
4. Play the target video for **2–3 seconds** to activate the session
5. Click the **Extensions (Puzzle Piece)** icon
6. Select **Get cookies.txt LOCALLY**
7. Click **Export**
8. A cookies file will be downloaded to your system
9. Rename the file to match the website name  
   Example:
```

facebook.txt

````
10. Move the renamed file into the following directory:
 ```
 DOWNLOAD ME/cookies/
 ```

Once placed correctly, the program will automatically detect the cookie file during execution.

---

## How the Program Uses Cookie Files

- The program scans the `/cookies/` directory at runtime
- Cookie files are selected based on filename
- The selected cookies are passed directly to `yt-dlp`
- Cookie data never leaves the local machine
- No cookies are stored remotely or transmitted to third parties

---

## Code Usage, Modification, and Redistribution

This project is intentionally structured to allow learning, modification, and extension.

### Permissions

- Users are free to:
- Study the source code
- Modify existing logic
- Extend features and functionality
- Optimize or refactor performance

### Requirements

- Any redistribution or derivative work **must include proper credit to the original author**
- Author attribution must be:
- Clearly visible
- Preserved in source files and documentation
- Not removed or altered

Failure to credit the original author is considered misuse of the project.

---

## Responsibility and Liability Statement

- The author explicitly states that they are **not responsible** for:
- Temporary or permanent IP bans
- Account suspensions or platform restrictions
- Hardware or software damage
- Data loss
- Legal consequences arising from misuse

- This project is provided **as-is**, without warranty of any kind
- All actions performed using this project are **entirely the responsibility of the user**
