# 🔥 GitHub Streak Box

A clean and customizable GitHub contribution tracker that visually displays your:

- ✅ Current Streak
- ✅ Longest Streak (with start and end dates)
- ✅ Total Contributions

This project helps you monitor your GitHub activity in a stylish format and is fully deployable on the web. Easily link it to your GitHub profile README and keep your streak updated daily!

---

## 🎯 Features

- 🔥 Displays your current contribution streak
- 📅 Shows the longest streak with accurate start–end dates
- 📈 Total contributions counter
- 🌈 Responsive and minimal UI
- 🛠 Manual JSON-based updating system
- 🌐 Live deployable via Netlify (or any static host)
- 🧩 Easily embeddable in your GitHub README

---

## 🧠 How It Works

- A Python script (`app.py`) uses GitHub’s GraphQL API to fetch your contribution data.
- It extracts:
  - Contributions from the past 7 days
  - Longest streak duration with date range
  - Current active streak
- The data is saved into a JSON file (`data.json`)
- An HTML/CSS page (`index.html`) reads the JSON and displays it in a user-friendly format
- The site is hosted using Netlify and linked to your GitHub for easy updates

---

## ⚙️ Tech Stack Used

- **Python** – Backend logic and GitHub API handling
- **GraphQL API** – For fetching GitHub contributions
- **HTML + CSS** – For UI layout and styling
- **JavaScript** – For reading and displaying JSON data
- **JSON** – Stores contribution data
- **Netlify** – For deployment and live hosting

---

## 📂 Folder Structure

GHB_Streak_Box/
│
├── app.py # Main Python script to fetch contribution data
├── streak_utils.py # Helper functions for streak calculation
├── web/
│ ├── index.html # Main webpage displaying streak data
│ ├── style.css # Styling for the webpage
│ └── data.json # Stores contribution data to be displayed

🌐 Live Preview
🔗 See it live here
👉 https://streak-box-denny.netlify.app


