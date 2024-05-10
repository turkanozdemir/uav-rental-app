import axios from "axios";

const BASE_URL = "http://localhost:8000/uavs/";

class UAVService {
  static async createUAV(uavData) {
    try {
      const response = await axios.post(`${BASE_URL}`, uavData, {
        headers: {
          "Content-Type": "application/json",
        },
      });
      return response.data;
    } catch (error) {
      console.error("Error while creating UAV:", error);
      throw error;
    }
  }

  static async listUAVs() {
    try {
      const response = await axios.get(`${BASE_URL}`);
      return response.data;
    } catch (error) {
      console.error("Error while fetching UAV list:", error);
      throw error;
    }
  }

  static async getUAV(serialNumber) {
    try {
      const response = await axios.get(
        `${BASE_URL}${serialNumber}/`
      );
      return response.data;
    } catch (error) {
      console.error(
        `Error while fetching UAV with serial number ${serialNumber}:`,
        error
      );
      throw error;
    }
  }

  static async updateUAV(serialNumber, updatedUAVData) {
    try {
      const response = await axios.put(
        `${BASE_URL}${serialNumber}/`,
        updatedUAVData,
        {
          headers: {
            "Content-Type": "application/json",
            // Gerekirse diğer header bilgilerini de buraya ekleyebilirsiniz
          },
        }
      );
      return response.data;
    } catch (error) {
      console.error(
        `Error while updating UAV with serial number ${serialNumber}:`,
        error
      );
      throw error;
    }
  }

  static async deleteUAV(serialNumber) {
    try {
      const response = await axios.delete(
        `${BASE_URL}${serialNumber}/`
      );
      return response.data;
    } catch (error) {
      console.error(
        `Error while deleting UAV with serial number ${serialNumber}:`,
        error
      );
      throw error;
    }
  }
}

export default UAVService;
