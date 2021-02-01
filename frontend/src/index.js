import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter } from "react-router-dom";
import App from "./App";
import store from "./store";
import { Provider } from "react-redux";
import { loadUserInfo } from './store/actions/authActions';

const userToken = localStorage.getItem("userToken");

if (userToken) {
	store.dispatch(loadUserInfo());
}

ReactDOM.render(
	<Provider store={store}>
		<BrowserRouter>
			<App />
		</BrowserRouter>
	</Provider>,
	document.getElementById("root")
);
