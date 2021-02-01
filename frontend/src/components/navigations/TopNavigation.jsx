import React from 'react'
import { NavLink, withRouter } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import { logout } from '../../store/actions/authActions'
import styles from './styles.module.css'


const TopNavigation = ({ history }) => {
    const dispatch = useDispatch()
    const auth = useSelector(state => state.auth)

    return (
        <nav className={styles.navBar}>
            <NavLink className={styles.navLink} to="/" exact>Home</NavLink>
            {auth.isAuthenticated ? (
                <>
                    <NavLink className={styles.navLink} to="/dashboard">Dashboard</NavLink>
                    <button className={styles.logoutButton} onClick={() => dispatch(logout(history))}>Logout</button>
                </>
            ) : (
                <NavLink className={styles.navLink} to="/login">Login</NavLink>
            )}
        </nav>
    )

}

export default withRouter(TopNavigation)