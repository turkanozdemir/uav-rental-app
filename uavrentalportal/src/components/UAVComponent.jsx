import React, { useState, useEffect } from "react";
import {
  Button,
  Paper,
  Typography,
  FormControl,
  createTheme,
  ThemeProvider,
  TextField,
} from "@mui/material";
import UAVService from "../services/UAVSercie";


const UAVComponent = () => {
  const [uavData, setUavData] = useState({
    email: sessionStorage.getItem("email"),
    serial_number: "",
    brand: "",
    model: "",
    year: 2024,
    weight: 10.5,
    max_range: 1000.0,
    max_speed: 50.0,
    max_flight_time: 120,
    max_payload_capacity: 5.0,
    daily_rental_fee: 200.0,
    availability: true,
    category: ["commercial", "civil"],
    sensors: ["gps", "thermal_camera"],
    functionality: ["autonomous_flight", "mapping_and_processing"],
    durability_and_design: ["weather_resistant", "modular_design"],
    communication_system: ["wifi", "rf"],
    security: ["collision_detection", "emergency_landing"],
    propulsion_system: ["electric_motor"],
  });
  const { email, ...formDataWithoutEmail } = uavData;

  const handleChange = (event) => {
    const { name, value } = event.target;
    setUavData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      console.log(uavData);

      const response = await UAVService.createUAV({
        uavData,
      });
      console.log("UAV added successfully:", response);
    } catch (error) {
      console.error("Error while logging in:", error);
      console.log("UAV can not be added!!!");
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
            Create UAV
          </Typography>
          <form onSubmit={handleSubmit}>
            <FormControl fullWidth style={{ marginBottom: "10px" }}>
              {Object.entries(formDataWithoutEmail).map(([key, value]) => (
                <TextField
                  key={key}
                  label={key.replace(/_/g, " ").toUpperCase()}
                  name={key}
                  value={value}
                  onChange={handleChange}
                  fullWidth
                  variant="outlined"
                  margin="normal"
                />
              ))}
              <Button
                variant="contained"
                color="primary"
                type="submit"
                style={{ marginTop: "10px" }}
              >
                Create UAV
              </Button>
            </FormControl>
          </form>
        </Paper>
      </div>
    </ThemeProvider>
  );
};

export default UAVComponent;
