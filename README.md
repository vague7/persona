# Reddit User Persona Builder 📝

This Python script takes a Reddit user’s profile URL as input, fetches their posts and comments using Reddit’s API, and uses Google Gemini LLM to build a **detailed user persona** (motivations, personality traits, behaviors, goals, frustrations) with citations from Reddit activity.

The final persona is saved to a text file.

---

## 🚀 Features

* Fetch Reddit user activity (posts + comments)
* Summarize and analyze using **Google Gemini API**
* Outputs a clean **user persona** with source links
* Easy setup with `.env` file for environment variables

---

## 🛠️ Requirements

* Python **3.8+**
* [Reddit API credentials](https://old.reddit.com/prefs/apps)
* Google Gemini API key ([Get API key here](https://ai.google.dev/gemini-api/docs/quickstart))
* pip package dependencies

---

## 💻 Setup Guide

### 1️⃣ Clone this Repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

---

### 2️⃣ Create and Activate a Virtual Environment

#### Linux/MacOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have `requirements.txt`, install manually:

```bash
pip install praw google-generativeai python-dotenv
```

---

### 4️⃣ Get API Keys

#### 🔑 Reddit API Credentials

1. Log in to Reddit and go to: [https://old.reddit.com/prefs/apps](https://old.reddit.com/prefs/apps)
2. Click **“Create app”** > Choose **script**
3. Set:

   * Name: *Reddit Persona Builder*
   * Redirect URI: `http://localhost`
4. After creation:

   * Copy `client_id` (14-char string)
   * Copy `client_secret` (27-char string)
5. Save these for later.

---

#### 🔑 Google Gemini API Key

1. Go to [https://ai.google.dev/](https://ai.google.dev/)
2. Click **Get API Key** and create one for your project
3. Copy the API key for later.

---

### 5️⃣ Set Environment Variables

Create a file named **`.env`** in the project root:

```bash
touch .env
```

Add the following (replace values with your own):

```
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=mybot:personabot:v0.1 (by u/yourusername)
GEMINI_API_KEY=your_google_gemini_api_key
```

---

## ▶️ Running the Script

```bash
python reddit_persona_builder.py
```

When prompted, enter a Reddit profile URL:

```
https://www.reddit.com/user/kojied/
```

The script will:
✅ Fetch the user’s posts & comments
✅ Analyze and summarize using Gemini
✅ Save the persona in a text file:

```
kojied_persona.txt
```




