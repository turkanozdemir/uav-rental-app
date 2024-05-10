import axios from 'axios';

const BASE_URL = 'http://localhost:8000/users/';

class UserService {
    static async registerUser(userData) {
        try {
            const response = await axios.post(`${BASE_URL}register/`, userData, {
                headers: {
                    'Content-Type': 'application/json',
                }
            });
            return response.data;
        } catch (error) {
            console.error('Error while registering user:', error);
            throw error;
        }
    }

    static async loginUser(userData) {
        try {
            const response = await axios.post(`${BASE_URL}login/`, userData, {
                headers: {
                    'Content-Type': 'application/json',
                }
            });
            return response.data;
        } catch (error) {
            console.error('Error while logging in user:', error);
            throw error;
        }
    }

    static async logoutUser() {
        try {
            const response = await axios.post(`${BASE_URL}logout/`);
            return response.data;
        } catch (error) {
            console.error('Error while logging out user:', error);
            throw error;
        }
    }

    static async getUserProfile() {
        try {
            const response = await axios.get(`${BASE_URL}profile/`);
            return response.data;
        } catch (error) {
            console.error('Error while fetching user profile:', error);
            throw error;
        }
    }

    static async getBrandUsers() {
        try {
            const response = await axios.get(`${BASE_URL}brand-users/`);
            return response.data;
        } catch (error) {
            console.error('Error while fetching brand users:', error);
            throw error;
        }
    }

    static async getCustomUsers() {
        try {
            const response = await axios.get(`${BASE_URL}custom-users/`);
            return response.data;
        } catch (error) {
            console.error('Error while fetching custom users:', error);
            throw error;
        }
    }
}

export default UserService;
