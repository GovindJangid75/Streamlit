# 📊 Streamlit Learning & Dashboard Projects

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A comprehensive, hands-on repository documenting a structured learning journey through **Streamlit** — Python's most popular framework for building interactive data web applications. This repo includes chapter-by-chapter exercises, a real-world dataset, an assignment, and a complete demo dashboard — all progressing from basic concepts to a fully functional interactive data app.

---

## 📌 Table of Contents

- [About This Repository](#-about-this-repository)
- [Repository Structure](#-repository-structure)
- [What You'll Learn](#-what-youll-learn)
- [Chapter Breakdown](#-chapter-breakdown)
- [Demo Dashboard](#-demo-dashboard)
- [Dataset](#-dataset)
- [Assignment](#-assignment)
- [Getting Started](#-getting-started)
- [Running the Apps](#-running-the-apps)
- [Tech Stack](#-tech-stack)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🧠 About This Repository

This repository is a curated set of Streamlit projects built as part of a structured learning course. Streamlit makes it incredibly easy to turn Python scripts into shareable, interactive web applications — no front-end experience required.

Each chapter file focuses on a specific set of Streamlit concepts, building progressively from the basics all the way to building a real data dashboard powered by actual sales data (`chai_sales.csv`). The final deliverable — `demo-dashboard.py` — brings together everything learned across all chapters into one polished, interactive application.

Whether you're a beginner picking up Streamlit for the first time or looking for reference examples, this repo has you covered.

---

## 📁 Repository Structure

```
Streamlit/
│
├── 📄 chapter-1.py          # Streamlit fundamentals: text, headers, markdown, layout
├── 📄 chapter-2.py          # Interactive widgets: sliders, buttons, text inputs, selectboxes
├── 📄 chapter-3.py          # Displaying data: DataFrames, tables, and metrics
├── 📄 chapter-4.py          # Data visualization: charts, line graphs, bar charts
├── 📄 chapter-5.py          # Advanced features: session state, caching, forms
│
├── 📄 Assigment-2.py        # Applied assignment using real data with multiple features
├── 📄 demo-dashboard.py     # Complete interactive dashboard (final project)
│
├── 📊 chai_sales.csv        # Real-world chai sales dataset used across demos
│
├── ⚙️  pyproject.toml       # Project metadata and dependency configuration (uv)
├── 🔒 uv.lock               # Pinned dependency versions for reproducibility
├── 🐍 .python-version       # Python version specification
├── 🚫 .gitignore            # Files excluded from version control
└── 📘 README.md             # You are here!
```

---

## 🎯 What You'll Learn

By exploring this repository, you will gain hands-on experience with:

- ✅ Setting up a Streamlit project from scratch
- ✅ Building interactive UI components (sliders, dropdowns, buttons, forms)
- ✅ Displaying and formatting data with `st.dataframe()`, `st.table()`, and `st.metric()`
- ✅ Creating data visualizations using Streamlit's built-in chart functions
- ✅ Working with CSV datasets using Pandas inside Streamlit
- ✅ Managing state with `st.session_state`
- ✅ Improving performance with `@st.cache_data`
- ✅ Building a complete, multi-section data dashboard
- ✅ Managing Python environments using the `uv` package manager

---

## 📚 Chapter Breakdown

### 📖 Chapter 1 — Streamlit Fundamentals (`chapter-1.py`)

An introduction to the core building blocks of any Streamlit app. This chapter focuses on:

- Writing text using `st.write()`, `st.title()`, `st.header()`, `st.subheader()`
- Formatting content with `st.markdown()` and `st.caption()`
- Structuring page layout and content flow
- Using `st.divider()` and `st.code()` for better readability

**Key Concept:** Understand how Streamlit re-runs a script from top to bottom on every user interaction.

---

### 📖 Chapter 2 — Interactive Widgets (`chapter-2.py`)

Streamlit's power comes from making Python scripts interactive without writing JavaScript. This chapter covers:

- `st.slider()` — for numeric range selections
- `st.text_input()` and `st.text_area()` — for collecting user text
- `st.selectbox()` and `st.multiselect()` — for dropdown menus
- `st.checkbox()` and `st.radio()` — for toggle-style inputs
- `st.button()` — for triggering actions
- `st.number_input()` and `st.date_input()`

**Key Concept:** Every widget returns a value you can use in Python logic — making your app reactive.

---

### 📖 Chapter 3 — Data Display (`chapter-3.py`)

Learn how to present data clearly and professionally. Topics include:

- Loading CSV data with Pandas
- `st.dataframe()` vs `st.table()` — when to use each
- `st.metric()` — KPI-style cards with delta indicators
- `st.json()` — for displaying structured data
- Column layout with `st.columns()`
- `st.expander()` for collapsible content sections

**Key Concept:** Effective data presentation is as important as the analysis itself.

---

### 📖 Chapter 4 — Charts & Visualizations (`chapter-4.py`)

Data is best understood visually. This chapter explores Streamlit's built-in charting capabilities:

- `st.line_chart()` — for trends over time
- `st.bar_chart()` — for categorical comparisons
- `st.area_chart()` — for cumulative data
- `st.scatter_chart()` — for correlations
- `st.map()` — for geographic data plotting
- Integration with **Matplotlib** and **Plotly** for custom charts

**Key Concept:** Choose your chart type based on the story your data tells.

---

### 📖 Chapter 5 — Advanced Features (`chapter-5.py`)

Level up your Streamlit apps with professional-grade features:

- `st.session_state` — persisting variables across reruns
- `@st.cache_data` — caching expensive computations for performance
- `st.form()` — batching widget submissions for better UX
- `st.sidebar` — adding a navigation/control panel
- `st.tabs()` — multi-tab layouts
- `st.spinner()` and `st.progress()` — loading indicators
- `st.toast()`, `st.success()`, `st.error()`, `st.warning()` — user feedback messages

**Key Concept:** Session state and caching are essential for building performant, production-ready apps.

---

## 📊 Demo Dashboard (`demo-dashboard.py`)

The crown jewel of this repository — a **fully interactive sales dashboard** powered by the `chai_sales.csv` dataset. It brings together all concepts from the five chapters into a single polished application.

### Features

- 📈 **Sales Trend Analysis** — Line chart showing sales performance over time
- 🏆 **Top Performing Products** — Bar chart ranking chai varieties by revenue
- 🔢 **KPI Metric Cards** — Total sales, average daily revenue, best-performing day
- 🔍 **Interactive Sidebar Filters** — Filter by date range, product type, or region
- 📋 **Raw Data Viewer** — Expandable section for exploring the underlying dataset
- 📥 **CSV Export** — Download filtered data directly from the app

### How to Run

```bash
streamlit run demo-dashboard.py
```

---

## 📂 Dataset (`chai_sales.csv`)

The `chai_sales.csv` file is a real-world style dataset used across multiple exercises and the demo dashboard. It contains sales records for various chai products.

| Column | Description |
|--------|-------------|
| Date | Date of the sale |
| Product | Type/variant of chai sold |
| Units Sold | Number of units sold |
| Revenue | Total revenue generated |
| Region | Geographic region of the sale |

This dataset powers the data display chapters, chart visualizations, the assignment, and the final demo dashboard.

---

## 📝 Assignment (`Assigment-2.py`)

A practical applied project combining multiple Streamlit concepts into one mini-application. The assignment demonstrates:

- Loading and exploring the chai sales dataset
- Applying interactive filters to refine the data view
- Generating charts based on user-selected parameters
- Presenting key KPIs and summary statistics

This file represents a checkpoint — combining skills from Chapters 1–4 before tackling the full demo dashboard.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.x** (check `.python-version` for the exact version used in this project)
- **uv** package manager (recommended) or **pip**

### Install uv (Recommended)

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Clone the Repository

```bash
git clone https://github.com/GovindJangid75/Streamlit.git
cd Streamlit
```

### Install Dependencies

**Using uv (fast & reproducible):**
```bash
uv sync
```

**Using pip:**
```bash
pip install streamlit pandas matplotlib plotly
```

---

## ▶️ Running the Apps

Once dependencies are installed, launch any file with the `streamlit run` command:

```bash
# Chapter exercises — work through these in order
streamlit run chapter-1.py
streamlit run chapter-2.py
streamlit run chapter-3.py
streamlit run chapter-4.py
streamlit run chapter-5.py

# Assignment
streamlit run Assigment-2.py

# Full Demo Dashboard
streamlit run demo-dashboard.py
```

Each command will open the app automatically in your default browser at `http://localhost:8501`.

> 💡 **Tip:** Start with `demo-dashboard.py` to see the end goal, then work through the chapters to understand how each piece was built.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Streamlit](https://streamlit.io/) | Web app framework for Python |
| [Python 3.x](https://python.org) | Core programming language |
| [Pandas](https://pandas.pydata.org/) | Data loading, manipulation, and analysis |
| [Matplotlib](https://matplotlib.org/) | Static chart creation |
| [Plotly](https://plotly.com/python/) | Interactive, dynamic visualizations |
| [uv](https://github.com/astral-sh/uv) | Fast, modern Python package manager |

---

## 🤝 Contributing

Contributions, improvements, and suggestions are welcome! To contribute:

1. **Fork** the repository
2. **Create** a new branch: `git checkout -b feature/your-feature-name`
3. **Make** your changes and add comments where helpful
4. **Commit**: `git commit -m 'Add: description of your change'`
5. **Push**: `git push origin feature/your-feature-name`
6. **Open** a Pull Request with a clear description of what you changed and why

Please keep code clean, well-commented, and consistent with the existing structure.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙋 Author

**Govind Jangid**
GitHub: [@GovindJangid75](https://github.com/GovindJangid75)

---

> ⭐ If you found this repository useful, consider giving it a star — it helps others discover it too!