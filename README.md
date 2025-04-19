# 🧭 Indoor Pathfinding System (Python + A\*)

Ever felt lost trying to find a room in a huge hospital or college building? This project is a Python-based indoor navigation tool designed to help people find their way—fast and easily.

It uses the A\* pathfinding algorithm to show the shortest route from your current location to your destination, all on a simple interactive grid. And the best part? It even has an accessibility mode that avoids stairs—perfect for wheelchair users or elderly visitors.

---

## 📁 Project Structure

```bash
path_finder/
│
├── .gitignore
├── a_star.py
├── grid.py
├── main.py
├── README.md
│
└── assets/
    ├── demo_gif.gif
    └── demo_video.mp4
```

---

## 💡 What It Does

-   Lets you pick a starting point and destination on a map
-   Finds and shows the shortest route using the A\* algorithm
-   Draws the path visually on a grid using Tkinter

Whether you're navigating a busy hospital or a confusing college campus, this tool can guide you room-to-room with ease.

---

## 🧰 Tech Stack

-   Python 3
-   Tkinter for the GUI
-   A\* search algorithm for pathfinding
-   2D grid maps (customizable)

---

## 📸 Example Use Case

Imagine you’re in a hospital, and you need to go from the main entrance to the X-Ray department. You open this app, click on your location, choose your destination, and boom—your route is drawn instantly.

---

## 🎬 Demo

![Demo of the navigation](assets/demo_gif.gif)

---

## 🚀 Getting Started

1. Clone this repository:

```bash
git clone https://github.com/Koustav2908/path-finder/
cd path-finder
```

2. Run the app:

```bash
python main.py
```

---

## 🛣️ Map Grid Basics

The app uses a grid system to simulate a floor layout:

-   0 = walkable path

-   1 = wall/obstacle

-   2 = stairs

The grid is customizable, so you can design your own floor plan easily.

---

## 🛠️ Future Work

Support for multi-floor navigation (with elevators or stairs)

Mobile app version

Clickable room names (instead of grid coordinates)

Real image floor plans support

---

## 👩‍💻 Built By

Made with 💙 in Python by Koustav Chatterjee, Anisha Kundu, Tista Sarkar, and Ratnadeep Paul.
Project domain: Healthcare & Education
Tech focus: Algorithms, GUI, Accessibility

---
