# Desktop Assistant

A small Windows desktop app that creates files and folders on your Desktop and lets you chat with a chatbot powered by Google Gemini. Built with Python and CustomTkinter.

[Download the latest release](https://github.com/hannandeveloper/desktop-assistant/releases/download/v1.0.0/DesktopAssistantv1.zip) · [Report an issue](https://github.com/hannandeveloper/desktop-assistant/issues) · [Author on GitHub](https://github.com/hannandeveloper)

---

## Features

| Feature | What it does |
|---|---|
| **Create a file** | Enter a file name and Desktop Assistant creates the file on your Desktop. |
| **Create a folder** | Enter a name and press the button. The folder appears on your Desktop and the status line confirms it. |
| **Create a folder with several files** | Make a folder and fill it with multiple files in one step. |
| **Talk to the chatbot** | Ask questions in the AI Chat tab. Replies appear as they are written. It uses your own Google Gemini API key. |

The file and folder tools work without an API key. Only the AI Chat tab needs one.

## Install

1. Open the [latest release](https://github.com/hannandeveloper/desktop-assistant/releases/latest) and download the file.
2. If you downloaded a zip, **extract it**. Run `DesktopAssistantv1.exe` from inside the extracted folder. The app needs the files next to it, so do not move the exe on its own.
3. Windows may show a SmartScreen warning because the app is not code-signed. Choose **More info**, then **Run anyway**.

## Get your API key

The AI Chat tab needs your own Gemini API key. Creating one takes about two minutes, and Google sets the usage limits for your key.

1. Open Google AI Studio's API keys page: <https://aistudio.google.com/api-keys>
2. Sign in with your Google account.
3. Choose **Create API key** and copy the key. If it asks for a project, pick one or create a new one.
4. In the same folder as `DesktopAssistant.exe`, create a file named `.env`.
   In Notepad, choose **Save as**, set **Save as type** to **All files**, and type `.env` as the file name. Otherwise Windows saves it as `.env.txt` and the app will not find it.
5. Add this line, replacing the placeholder with your key. Use no quotes and no spaces around the equals sign:

   ``` bash
   gen_api=PASTE_YOUR_KEY_HERE
   ```

6. Save the file, start Desktop Assistant, open the **AI Chat** tab and send a message.

> **Keep your key private.** Do not post it, send your `.env` file to anyone, or upload it to GitHub. If it leaks, delete the key in AI Studio and create a new one.

## Run from source

You need Python 3.10 or newer.

``` bash
git clone https://github.com/hannandeveloper/desktop-assistant.git
cd YOUR-REPO
python -m pip install customtkinter google-genai python-dotenv
```

Create a `.env` file in the project folder with `gen_api=YOUR_KEY`, then run:

``` bash
python gui.py
```

### Project structure

```
gui.py        Window, tabs and widgets (CustomTkinter)
filetask.py   File and folder functions
chatbot.py    Gemini chat logic
.env          Your API key (never commit this file)
```

## Build the exe

``` bash
python -m pip install pyinstaller
python -m PyInstaller --noconfirm --onedir --windowed --name DesktopAssistant --collect-all customtkinter --collect-submodules google.genai gui.py
```

The app is created in `dist\DesktopAssistant`. Do not copy your own `.env` into a build you plan to share.

## Contributing

**All contributions are welcome.** Report a bug, suggest a feature, improve the documentation or send a pull request.

1. Fork the repository and create a branch for your change.
2. Make your change and test it by running `python gui.py`.
3. Open a pull request that explains what you changed and why.

For a large change, please [open an issue](https://github.com/hannandeveloper/desktop-assistant/issues) first so we can talk it through.

Add `.env` to your `.gitignore` so your API key never ends up in a commit.


