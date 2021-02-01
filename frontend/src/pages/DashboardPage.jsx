import React from 'react'
import { Link } from 'react-router-dom'
import LayoutContainer from '../components/layouts/LayoutContainer';

const DashboardPage = ({ history }) => {

    return (
        <LayoutContainer>
            <h1>Dashboard Page</h1>
            <div>
                <Link to="/transactions">Transaction</Link>
                <Link to="/notes">Short Note</Link>
            </div>
        </LayoutContainer>
    )

}


export default DashboardPage