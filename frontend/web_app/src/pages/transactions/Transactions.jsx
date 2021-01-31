import React from 'react'
import { Link } from 'react-router-dom'
import LayoutContainer from '../../components/layouts/LayoutContainer'

const Transactions = () => {

    return (
        <LayoutContainer>
            <Link to="/transactions/create">Create Transaction</Link>
        </LayoutContainer>
    )

}


export default Transactions