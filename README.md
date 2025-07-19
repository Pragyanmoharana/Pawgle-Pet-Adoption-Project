# 🐾 Pawgle - Pet Adoption Platform

**Pawgle** is a Django-based pet adoption platform that connects pet lovers with pets in need of a home. Users can browse pets, donate a pet for adoption, request to adopt a pet, and share their experiences through feedback. The platform includes admin management for approving pets and adoption requests, along with in-app status tracking and notification features.

---

## 🌟 Features

- 🐶 **Adopt a Pet:** Browse and filter pets by species and gender.
- ✍️ **Donate a Pet:** Fill a simple form to request pet donation.
- ✅ **Admin Approval:** Admin reviews and approves donated pets and adoption requests.
- 📬 **Adoption Request Tracking:** Users can track the status of their adoption requests.
- 🔒 **User Auth:** Register, Login, and Logout securely.
- 🔔 **In-App Notifications:** See live updates for donations and adoptions.
- 📞 **Contact Us Page:** Contact for rescue and services.

---

## 🛠️ Tech Stack

| Frontend   | Backend  | Database | Other Tools |
|------------|----------|----------|-------------|
| HTML, CSS, Bootstrap, JavaScript | Django (Python) | SQLite | Django Admin, Static Files |

---

## 🚀 Getting Started

## 📦 Prerequisites

- Python 3.x
- Django
- pip
- Virtualenv (optional but recommended)

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Pragyanmoharana/Pawgle-Pet-Adoption-Project.git
   cd Pawgle-Pet-Adoption-Project

2. Create and activate a virtual environment:

python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate   

3. Install dependencies:
pip install -r requirements.txt

4. Apply migrations:
python manage.py migrate

5. Run the development server:
python manage.py runserver

6. Open your browser and visit:
http://127.0.0.1:8000/home
