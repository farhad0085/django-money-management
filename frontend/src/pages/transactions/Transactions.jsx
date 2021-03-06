import React, { useEffect } from 'react'
import { Link } from 'react-router-dom'
import LayoutContainer from '../../components/layouts/LayoutContainer'
import { useSelector, useDispatch } from 'react-redux'
import { getAllTransactions } from '../../store/actions/transactionActions'
import styles from './styles.module.css'
import Transaction from './Transaction'


const Transactions = () => {

    const dispatch = useDispatch()
    const transaction = useSelector(state => state.transaction)

    useEffect(() => {
        dispatch(getAllTransactions())
        // eslint-disable-next-line
    }, [])

    return (
        <LayoutContainer>
            <div className={styles.transactionContainer}>
                <Link className={styles.createTransactionLink} to="/transactions/create">Create Transaction</Link>
                <ul className={styles.transactionList}>
                    {transaction.transactions.map(transaction => <Transaction key={transaction.id} transaction={transaction} />)}
                </ul>
            </div>
        </LayoutContainer>
    )

}


export default Transactions