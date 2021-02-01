import React from 'react'
import styles from './styles.module.css'


const Transaction = ({ transaction }) => {

    const itemClass = transaction.transaction_type ? styles.spend : styles.earn
    const transactionType = transaction.transaction_type ? "Spend" : "Earn"

    return (
        <div className={`${styles.transactionItem} ${itemClass}`}>
            <h2 className={styles.transactionTitle}>
                {transaction.title}
                <span className={styles.amount}>{transactionType} {transaction.amount} {transaction.currency}</span></h2>
            <div className={styles.transactionDescription}>
                <p>{transaction.body}</p>
            </div>
        </div>
    )

}


export default Transaction