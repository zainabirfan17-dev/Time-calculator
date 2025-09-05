# 🕒 TIME CALCULATOR

[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Made by Zainab](https://img.shields.io/badge/made%20by-Zainab%20Irfan-pink.svg)](https://github.com/zainabirfan17-dev)

A Python project that calculates the new time after adding a given duration to a starting time.  
It supports **12-hour format (AM/PM)**, handles **day rollovers**, and can also compute the **day of the week** if provided.

---

## ✨ Features
- Add hours and minutes to a starting time  
- Correctly handle **AM/PM conversions**  
- Track how many days later the new time is  
- Optionally calculate the **new day of the week**  
- Clean, well-documented, and open-source  

---

## 📂 Installation
Clone this repository to your local machine:

```bash
git clone https://github.com/zainabirfan17-dev/TIME-CALCULATOR.git
cd TIME-CALCULATOR
```

## 🚀 Usage

Run the script with Python:
```bash
python time_calculator.py
```


Or import it in another Python script:


```bash
from time_calculator import add_time

print(add_time('3:00 PM', '3:10'))
# Output: 6:10 PM
```

## More examples:
```bash
>>> add_time('11:30 AM', '2:32', 'Monday')
'2:02 PM, Monday'

>>> add_time('10:10 PM', '3:30')
'1:40 AM (next day)'

>>> add_time('11:43 PM', '24:20', 'tueSday')
'12:03 AM, Thursday (2 days later)'
```

## 🎥 Explanation Video

For a detailed walkthrough of this problem, check out this video:
[YouTube – Time Calculator Explanation](https://youtu.be/zjYpfpFS-p8)


## 📜 License

This project is licensed under the MIT License
.

## 👩‍💻 Author

Zainab Irfan
[GitHub Profile](https://github.com/zainabirfan17-dev) 

