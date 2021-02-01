import React from "react";
import { Link } from "react-router-dom";
import LayoutContainer from "../components/layouts/LayoutContainer";
import { useSelector } from 'react-redux'
import styles from './home.module.css'

const HomePage = () => {

    const auth = useSelector(state => state.auth)

    return (
        <LayoutContainer>
            <h1 className={styles.title}>Home page</h1>
            {auth.isAuthenticated ? (
                <Link to="/dashboard">Go to dashboard</Link>
            ) : (
                <Link to="/login">Login</Link>
            )}
        </LayoutContainer>
    );
};

export default HomePage;
