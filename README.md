# Smart Exam Scheduler

This project automates the creation of a university/college exam schedule based on student course enrollment data. It aims to minimize conflicts by ensuring that students enrolled in multiple courses do not have exams scheduled at the same time. It also considers room capacities when assigning exams.

## How it Works

1.  **Data Ingestion:** Reads student course enrollment data from an Excel file (`studentcourses.xlsx`). This data includes student ID, course name, etc.
2.  **Conflict Graph Creation:**
    *   A graph is constructed where each course is a node.
    *   An edge is created between two courses if at least one student is enrolled in both.
    *   The weight of the edge represents the number of students co-enrolled in both connected courses, indicating the severity of the conflict.
3.  **Exam Slot Assignment (Graph Coloring):**
    *   The [Greedy Graph Coloring](https://en.wikipedia.org/wiki/Greedy_coloring) algorithm (specifically using the "largest_first" strategy from NetworkX) is applied to the conflict graph.
    *   Each color assigned by the algorithm represents a unique exam time slot. Adjacent nodes (conflicting courses) receive different colors, ensuring they are scheduled at different times.
    *   The project also benchmarks different coloring strategies (`smallest_last`, `random_sequential`, `independent_set`) for time and number of colors used.
4.  **Room Assignment:**
    *   Based on predefined room capacities and the number of students enrolled in each course, courses are assigned to available rooms for their scheduled time slot.
5.  **Schedule Generation:**
    *   An Excel file (`جدول_الامتحانات_منسق.xlsx`) is generated, presenting the final exam schedule organized by day and period (e.g., 4 periods per day). Each entry includes the course name, number of students, and the assigned room.
6.  **Visualization:**
    *   Includes visualizations of the course conflict graph (for the top 20 most connected courses) and a bar chart of the top 100 courses by student enrollment.
7.  **Arabic Support:** The project includes functionality to correctly display and handle Arabic text for course names in visualizations and the output Excel file.

## Technologies Used

*   **Python 3**
*   **Jupyter Notebook**
*   **Pandas:** For data loading, manipulation, and analysis.
*   **NumPy:** For numerical operations, often used with Pandas.
*   **Matplotlib:** For creating static, animated, and interactive visualizations.
*   **NetworkX:** For graph creation, manipulation, analysis, and graph coloring algorithms.
*   **Openpyxl:** For reading and writing Excel files (`.xlsx`).
*   **arabic-reshaper & python-bidi:** For proper rendering and display of Arabic text.
*   **time:** For benchmarking algorithm performance.

## Input

*   `studentcourses.xlsx`: An Excel file containing student enrollment data with columns like 'رقم الطالب' (Student ID), 'اسم المقرر' (Course Name), etc.

## Output

*   `جدول_الامتحانات_منسق.xlsx`: An Excel file containing the generated, formatted exam schedule.
*   Visualizations (bar charts and graph plots) displayed within the notebook.


This README provides a good overview of what your project does, the main steps involved, and the technologies it utilizes, as requested.
