import React from "react";
import { Link } from "react-router-dom";
import LayoutContainer from "../components/layouts/LayoutContainer";
import { useSelector } from 'react-redux'


const HomePage = () => {

    const auth = useSelector(state => state.auth)

    return (
        <LayoutContainer>
            <h1>Home page</h1>
            {auth.isAuthenticated ? (
                <Link to="/dashboard">Go to dashboard</Link>
            ) : (
                <Link to="/login">Login</Link>
            )}
        </LayoutContainer>
    );
};

export default HomePage;
