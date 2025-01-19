# housing-yasmine-gaoui
the objectif is to create houses and fetching them.


# Python, Flask, and PostgreSQL: API Application  

## **Project Description**  

This project showcases how to create a simple API using Flask to interact with a PostgreSQL database. It enables managing house-related data through a `houses` table, using the psycopg2 library to handle database operations.  

---

## **Technologies Used**  

- **Programming Language**: Python  
- **Framework**: Flask  
- **Database**: PostgreSQL  
- **Library**: psycopg2  

---

## **Prerequisites**  

Before starting, make sure you have:  

1. **Python 3.x** installed with a virtual environment tool.  
2. **PostgreSQL**, running on your local machine or a server.  
3. **Git**, to clone the repository.  

---

## **Installation and Setup**  

### **1. Clone the Repository**  

```bash  
git clone https://github.com/yourusername/project-houses-api.git  
cd project-houses-api  
```  

### **2. Prepare the Python Environment**  

- Activate a virtual environment:  
  ```bash  
  python -m venv venv  
  source venv/bin/activate  # On Windows: venv\Scripts\activate  
  ```  

- Install required dependencies:  
  ```bash  
  pip install -r requirements.txt  
  ```  

### **3. Configure PostgreSQL**  

- Update the PostgreSQL credentials in the `app.py` file:  
  ```python  
  conn = psycopg.connect(database="postgres", user="postgres", password="your_password", host="127.0.0.1", port="5432")  
  ```  

- Ensure the PostgreSQL user has permissions to create databases and tables.  

---

## **Running the Application**  

1. Make sure your PostgreSQL server is up and running.  
2. Start the Flask application:  
   ```bash  
   python app.py  
   ```  
3. Access the API at [http://127.0.0.1:5000](http://127.0.0.1:5000).  

---

## **API Endpoints**  

### **1. GET `/houses`**  

- **Description**: Retrieves all house records from the database.  
- **Sample Response**:  
  ```json  
  [  
    {  
      "house_id": 1,  
      "longitude": -122.23,  
      "latitude": 37.88,  
      "housing_median_age": 41,  
      "total_rooms": 880,  
      "total_bedrooms": 129,  
      "population": 322,  
      "households": 126,  
      "median_income": 8.3252,  
      "median_house_value": 452600,  
      "ocean_proximity": "NEAR BAY"  
    }  
  ]  
  ```  

### **2. POST `/houses`**  

- **Description**: Adds a new house record to the database.  
- **Sample Request Body**:  
  ```json  
  {  
    "house_id": 2,  
    "longitude": -122.22,  
    "latitude": 37.86,  
    "housing_median_age": 21,  
    "total_rooms": 7099,  
    "total_bedrooms": 1106,  
    "population": 2401,  
    "households": 1138,  
    "median_income": 8.3014,  
    "median_house_value": 358500,  
    "ocean_proximity": "NEAR BAY"  
  }  
  ```  
- **Sample Response**:  
  ```json  
  {  
    "message": "House added successfully!"  
  }  
  ```  

---

## **Testing the API**  

### **GET Request Example**  

```bash  
curl http://127.0.0.1:5000/houses  
```  

### **POST Request Example**  

```bash  
curl -X POST http://127.0.0.1:5000/houses \  
-H "Content-Type: application/json" \  
-d '{  
  "house_id": 3,  
  "longitude": -122.24,  
  "latitude": 37.85,  
  "housing_median_age": 25,  
  "total_rooms": 1467,  
  "total_bedrooms": 190,  
  "population": 496,  
  "households": 177,  
  "median_income": 7.2574,  
  "median_house_value": 352100,  
  "ocean_proximity": "INLAND"  
}'  
```  

---

## **Troubleshooting**  

- **Connection Issues**: Ensure PostgreSQL is running and the credentials are correct.  
- **Missing Dependencies**: Run `pip install -r requirements.txt` again.  
- **Table or Database Not Found**: The app automatically creates the `houses` table and database if they don’t exist.  

---

## **License**  

This project is licensed under the MIT License. You are free to use, modify, and distribute it while respecting the terms of the license.  

---  

This README is tailored for clarity and usability while being structured differently to maintain originality.
