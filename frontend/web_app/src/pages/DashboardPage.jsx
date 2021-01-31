import React from 'react'
import { useDispatch } from 'react-redux'
import { logout } from '../store/actions/authActions'

const DashboardPage = ({ history }) => {

    const dispatch = useDispatch()

    return (
        <div>
            <button onClick={() => dispatch(logout(history))}>Logout</button>
            <h1>Dashboard Page</h1>
        </div>
    )

}


export default DashboardPage