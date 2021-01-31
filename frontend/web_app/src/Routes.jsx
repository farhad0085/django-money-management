import React from "react";
import { Route, Redirect, Switch } from "react-router-dom";
import { useSelector } from "react-redux";
import NotFound from "./pages/NotFound";
import HomePage from "./pages/HomePage";
import DashboardPage from "./pages/DashboardPage";
import LoginPage from "./pages/auth/LoginPage";


const Routes = () => {
    return (
        <Switch>
            <Route path="/" exact component={HomePage} />
            <PrivateRoute path="/dashboard" component={DashboardPage} />

            {/* auth routes */}
            <GuestRoute path="/login" component={LoginPage} />

            <Route component={NotFound} />
        </Switch>
    );
};

export default Routes;

export const GuestRoute = ({ component: Component, ...rest }) => {
    const auth = useSelector((state) => state.auth);

    return (
        <Route
            {...rest}
            render={(props) => (
                <>
                    {!auth.isAuthenticated ? (
                        <Component {...props} />
                    ) : (
                            <Redirect
                                to={{
                                    pathname: "/",
                                    state: { from: props.location },
                                }}
                            />
                        )}
                </>
            )}
        />
    );
};

export const PrivateRoute = ({ component: Component, ...rest }) => {
    const auth = useSelector((state) => state.auth);

    return (
        <Route
            {...rest}
            render={(props) => (
                <>
                    {auth.isAuthenticated ? (
                        <Component {...props} />
                    ) : (
                            <Redirect
                                to={{
                                    pathname: "/login",
                                    state: { from: props.location },
                                }}
                            />
                        )}
                </>
            )}
        />
    );
};
