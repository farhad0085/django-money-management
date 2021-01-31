import React from 'react'
import { NavLink, withRouter } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import { logout } from '../../store/actions/authActions'


const TopNavigation = ({ history }) => {
    const dispatch = useDispatch()
    const auth = useSelector(state => state.auth)

    return (
        <nav>
            <NavLink to="/" exact>Home</NavLink>
            {auth.isAuthenticated ? (
                <div>
                    <NavLink to="/dashboard">Dashboard</NavLink>
                    <button onClick={() => dispatch(logout(history))}>Logout</button>
                </div>
            ) : (
                <NavLink to="/login">Login</NavLink>
            )}
        </nav>
    )

}

export default withRouter(TopNavigation)