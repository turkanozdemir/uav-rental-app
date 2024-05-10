import React, { useState } from "react";
import UserService from "../services/UsersService";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import {
  Button,
  Paper,
  Typography,
  FormControl,
  createTheme,
  ThemeProvider,
  TextField,
} from "@mui/material";

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

const UserLoginComponent = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [userType, setUserType] = useState("custom"); // Default user type is "custom"
  const navigate = useNavigate();

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleUserTypeChange = (userTypeValue) => {
    setUserType(userTypeValue);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await UserService.loginUser({
        user_type: userType,
        email: email,
        password: password,
      });
      console.log("Login successful:", response);
      sessionStorage.setItem('userType', userType);
      sessionStorage.setItem('email', email);

      if (userType === "brand") navigate("/uav-create");
    } catch (error) {
      console.error("Error while logging in:", error);
      setError("* Invalid credentials. Please try again.");
    }
  };

  const theme = createTheme({
    palette: {
      primary: {
        main: "#1976d2",
      },
      secondary: {
        main: "#f50057",
      },
    },
  });

  return (
    <ThemeProvider theme={theme}>
      <div
        style={{
          minHeight: "100vh",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          backgroundImage: `url(background.jpg)`,
          backgroundSize: "cover",
        }}
      >
        <Paper
          style={{
            padding: "20px",
            maxWidth: "400px",
            width: "100%",
            backgroundColor: "rgba(255, 255, 255, 0.8)",
          }}
        >
          <Typography variant="h4" align="center" gutterBottom>
            {userType === "brand" ? "Brand User Login" : "Custom User Login"}
          </Typography>
          <div style={{ marginBottom: "10px" }}>
            <Button
              variant={userType === "brand" ? "contained" : "outlined"}
              color="primary"
              style={{ marginRight: "10px" }}
              onClick={() => handleUserTypeChange("brand")}
            >
              Brand User Login
            </Button>
            <Button
              variant={userType === "custom" ? "contained" : "outlined"}
              color="primary"
              onClick={() => handleUserTypeChange("custom")}
            >
              Custom User Login
            </Button>
          </div>
          <form onSubmit={handleSubmit}>
            <FormControl fullWidth style={{ marginBottom: "10px" }}>
              <TextField
                label="E-mail"
                value={email}
                onChange={handleEmailChange}
                fullWidth
                variant="outlined"
                margin="normal"
              />
              <TextField
                label="Password"
                variant="outlined"
                fullWidth
                margin="normal"
                type="password"
                  value={password}
                  onChange={handlePasswordChange}
                />
                {error && (
                  <Typography variant="body2" color={"red"}>
                    {error}
                </Typography>
              )}
              <Button
                variant="contained"
                color="primary"
                type="submit"
                style={{ marginTop: "10px" }}
              >
                Login
              </Button>
            </FormControl>
          </form>
        </Paper>
      </div>
    </ThemeProvider>
  );
};

export default UserLoginComponent;
