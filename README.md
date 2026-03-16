# 🧠 AI To-Do Reminder Desktop App

A lightweight **AI-powered To-Do reminder application** built with Python that allows users to add tasks using natural language and receive desktop notifications at the scheduled time.

The application runs in the background, stores tasks locally, and reminds you even while you're doing other work.

---

# 🚀 Features

* 📝 **Natural Language Tasks**

  * Example: `Study Machine Learning today at 8pm`
* ⏰ **Scheduled Reminders**

  * Automatically parses time and schedules notifications
* 🔔 **Desktop Notifications**

  * Pop-up reminders appear on your screen
* 💾 **Local Database Storage**

  * Tasks are stored using SQLite
* ⚡ **Lightweight & Efficient**

  * Minimal CPU and battery usage
* 🖥 **GUI Interface**

  * Built using Qt-based Python GUI
* 🔁 **CRUD Operations**

  * Create, Read, Update, Delete tasks
* 📌 **System Tray Support**

  * Runs in the background

---

# 🛠 Tech Stack

| Technology | Purpose                       |
| ---------- | ----------------------------- |
| Python     | Core language                 |
| PySide6    | GUI framework                 |
| SQLite     | Local task storage            |
| Plyer      | Desktop notifications         |
| DateParser | Natural language time parsing |

---

# 📂 Project Structure

```
AI_TO_DO_APP
│
├── main.py            # Main application runner
├── gui.py             # GUI interface
├── database.py        # SQLite database operations
├── notifier.py        # Notification system
├── ai_parser.py       # Natural language time parser
│
├── icon.png           # App icon
├── tasks.db           # SQLite database (auto-generated)
│
├── requirements.txt   # Python dependencies
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI_TO_DO_APP.git
cd AI_TO_DO_APP
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
python main.py
```

The application will:

* Launch the GUI
* Run a background reminder loop
* Show notifications when tasks are due

---

# 📝 Example Task Inputs

You can type tasks like:

```
Study Machine Learning today at 8pm
Finish project tomorrow at 10am
Call John at 6pm
Submit assignment 2026-03-20 14:00
```

The AI parser will extract the time and schedule the reminder.

---

# 🔔 Notifications

When a task time is reached:

* A **desktop pop-up notification** appears
* The reminder runs even while you are working on other applications

---

# 🧩 Future Improvements

* Recurring reminders
* Priority detection using AI
* Voice input for tasks
* Cloud sync across devices
* Mobile companion app

---

# 📦 Build Desktop Executable

You can convert the app into a standalone executable using PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

This will generate a runnable `.exe` file.

---

# 🤝 Contributing

Contributions are welcome.

If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

# 📜 License

This project is open-source and available under the MIT License.

---

# 👨‍💻 Author

Ayushman
AI / Software Developer

---

⭐ If you find this project useful, consider giving it a **star**!


