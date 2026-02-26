HRMS Lite is a simple Human Resource Management System built as a full stack project.
This project helps to manage:
Employees
Attendance
It is created for learning full stack development using FastAPI and React.
Technologies used:
Backend:
FastAPI
SQLAlchemy
my sql
Pydantic
frontend:
React
Vite
Axios
features of this project:
Employee Management
Add new employee
Email validation
Prevent duplicate Employee ID
Prevent duplicate Email
Proper error messages
Attendance Management
Mark employee as Present or Absent
Filter attendance by employee
Prevent duplicate attendance for same date
project structure:
i have created a main folder called hrms project under that there are 3 folders 1.backend 2. frontend and 3. environmental space and in these folders 
we have some files in backend such as models.py,schemas.py,main.py, models.py . to create a database i have used my sql workbench and in frontend we have a file called frontend-react
in that again we have API and Components two folders and few files like employee form , attendence form  , attendence list and employee list 
to run server in the backend i use "uvicorn main:app --reload" and to run sever in the frontend i use npm run dev. and to see the results we will get a link for example in the backend 
i got "http://127.0.0.1:8000" and to see the result i have typed in the browser /docs and in the frontend the link is "http://localhost:5173"
key points which i have done in this project 
connecting frontend with the backend
handling API errors
validating the data
preventing  duplicate records
basic full stack deployment
API & Error Handling Implementation
200 OK – Successful data retrieval
400 Bad Request – Duplicate or invalid input data
404 Not Found – Resource does not exist
422 Unprocessable Entity – Validation failure(Auto in Fast API)

