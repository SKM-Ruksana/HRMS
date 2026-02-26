import { useState } from "react";
import API from "../API/API";

function EmployeeForm() {
  const [form, setForm] = useState({
    employeeId: "",
    fullName: "",
    email: "",
    department: "",
  });

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await API.post("/employees", form);

      alert("Employee added successfully ");

      setForm({
        employeeId: "",
        fullName: "",
        email: "",
        department: "",
      });

    } catch (err) {
      const errorData = err.response?.data?.detail;

      // If FastAPI sends validation errors (array)
      if (Array.isArray(errorData)) {
        const messages = errorData.map((e) => e.msg).join(", ");
        alert(messages);
      }
      // If FastAPI sends custom error (string)
      else if (typeof errorData === "string") {
        alert(errorData);
      }
      // Fallback
      else {
        alert("Something went wrong while adding employee");
      }
    }
  };

  return (
    <div>
      <h2>Add Employee</h2>

      <form onSubmit={handleSubmit}>
        <input
          placeholder="Employee ID"
          value={form.employeeId}
          onChange={(e) =>
            setForm({ ...form, employeeId: e.target.value })
          }
          required
        />

        <input
          placeholder="Full Name"
          value={form.fullName}
          onChange={(e) =>
            setForm({ ...form, fullName: e.target.value })
          }
          required
        />

        <input
          placeholder="Email"
          type="email"
          value={form.email}
          onChange={(e) =>
            setForm({ ...form, email: e.target.value })
          }
          required
        />

        <input
          placeholder="Department"
          value={form.department}
          onChange={(e) =>
            setForm({ ...form, department: e.target.value })
          }
          required
        />

        <button type="submit">Add Employee</button>
      </form>
    </div>
  );
}

export default EmployeeForm;