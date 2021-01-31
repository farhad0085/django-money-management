import { getHeaders } from "../../utils";
import axios from "../../utils/axios";
import * as Types from "./actionTypes";

export const login = (loginCreds, history) => (dispatch) => {
  dispatch({ type: Types.AUTH_LOADING, payload: true });
  dispatch({ type: Types.USER_LOGIN_ERROR, payload: {} });
  axios
    .post("/auth/login/", loginCreds)
    .then((res) => {
      localStorage.setItem("userToken", res.data.key);
      dispatch({ type: Types.USER_LOGGED_IN });
      history.push("/dashboard");
      dispatch(loadUserInfo());
    })
    .catch((error) => {
      console.log(error.response);
      dispatch({
        type: Types.USER_LOGIN_ERROR,
        payload: error.response ? error.response.data : {},
      });
      dispatch({ type: Types.AUTH_LOADING, payload: false });
    });
};

export const register = (registerData, history) => (dispatch) => {
  dispatch({ type: Types.AUTH_LOADING, payload: true });
  dispatch({ type: Types.USER_REGISTER_ERROR, payload: {} });
  axios
    .post("/auth/register/", registerData)
    .then((res) => {
      // console.log(res.data);
      localStorage.setItem("userToken", res.data.key);
      dispatch({ type: Types.AUTH_LOADING, payload: false });
      dispatch({ type: Types.USER_REGISTERED });
      history.push("/");
      dispatch(loadUserInfo()); // after registration complete get user info
    })
    .catch((error) => {
      // console.log(error.response);
      dispatch({
        type: Types.USER_REGISTER_ERROR,
        payload: error.response ? error.response.data : {},
      });
      dispatch({ type: Types.AUTH_LOADING, payload: false });
    });
};

export const logout = (history) => (dispatch) => {
  dispatch({ type: Types.AUTH_LOADING, payload: true });

  axios
    .post("/auth/logout/", {}, { headers: getHeaders() })
    .then((res) => {
      localStorage.removeItem("userToken");
      dispatch({ type: Types.USER_LOGGED_OUT });
      dispatch({ type: Types.AUTH_LOADING, payload: false });
      history.push("/");
    })
    .catch((error) => {
      console.log(error.response);
      dispatch({
        type: Types.USER_LOGOUT_ERROR,
        payload: error.response ? error.response.data : {},
      });
      dispatch({ type: Types.AUTH_LOADING, payload: false });
    });
};

export const loadUserInfo = () => (dispatch) => {
  dispatch({ type: Types.AUTH_LOADING, payload: true });

  axios
    .get("/auth/user/me/", { headers: getHeaders() })
    .then((res) => {
      dispatch({ type: Types.AUTH_LOADING, payload: false });
    })
    .catch((error) => {
      console.log(error.response);
      localStorage.removeItem("userToken");
      dispatch({ type: Types.USER_LOGGED_OUT });
      dispatch({ type: Types.AUTH_LOADING, payload: false });
    });
};
