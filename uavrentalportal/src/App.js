import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import BrandUserLogin from "./components/UserLoginComponent"; // Ensure correct import path
import UAVComponent from "./components/UAVComponent";

function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/brand-user/login" element={<BrandUserLogin />} />
          <Route path="/uav-create" element={<UAVComponent />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
