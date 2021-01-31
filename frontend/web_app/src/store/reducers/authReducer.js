import * as Types from "../actions/actionTypes";

const initialState = {
  isAuthenticated: !!localStorage.getItem("userToken"),
  logoutErrors: {},
  loginErrorMessage: "",
  loading: false,
  user: {},
};

function authReducer(state = initialState, action) {
  switch (action.type) {
    case Types.AUTH_LOADING: {
      return {
        ...state,
        loading: action.payload,
      };
    }
    case Types.USER_LOGGED_OUT: {
      return {
        ...state,
        isAuthenticated: false,
      };
    }
    case Types.USER_LOGOUT_ERROR: {
      return {
        ...state,
        logoutErrors: action.payload,
      };
    }
    
    default: return state;
  }
}

export default authReducer;
