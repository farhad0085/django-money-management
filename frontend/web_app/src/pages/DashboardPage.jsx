import React from 'react'
import { useSelector, useDispatch } from 'react-redux'

const DashboardPage = () => {
     
    const auth = useSelector(state => state.auth)

    return (
        <h1>Dashboard Page</h1>
    )

}


export default DashboardPage