import { useState } from "react";
import EmployeeForm from "./components/employeeform";
import EmployeeList from "./components/employeelist";
import AttendanceForm from "./components/attendenceform";
import AttendanceList from "./components/attendencelist";
 
function App() {
  const [selectedEmployee, setSelectedEmployee] = useState(null);
 
  return (
<div className="container">
<h1>HRMS Lite Dashboard</h1>
 
      <div className="card">
<EmployeeForm />
</div>
 
      <div className="card">
<EmployeeList onSelectEmployee={setSelectedEmployee} />
</div>
 
      <div className="card">
<AttendanceForm />
</div>
 
      <div className="card">
<AttendanceList employeeId={selectedEmployee} />
</div>
</div>
  );
}
 
export default App;