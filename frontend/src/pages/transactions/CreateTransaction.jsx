import React, { useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import LayoutContainer from '../../components/layouts/LayoutContainer'
import { createTransaction } from '../../store/actions/transactionActions'
import { createUUID } from '../../utils'
import currencies from '../../utils/currencies'
import styles from './styles.module.css'


const CreateTransaction = ({ history }) => {

    const dispatch = useDispatch()
    const transaction = useSelector(state => state.transaction)
    const auth = useSelector(state => state.auth)

    const [amount, setAmount] = useState()
    const [title, setTitle] = useState("")
    const [body, setBody] = useState("")
    const [tags, setTags] = useState("")
    const [type, setType] = useState("spend")
    const [currency, setCurrency] = useState(auth.user.user_profile.currency)


    const submitHandler = event => {
        event.preventDefault()
        const data = { title, body, amount, tags, transaction_type: type, currency }
        dispatch(createTransaction(data, history))
    }

    return (
        <LayoutContainer>
            <div className={styles.transactionContainer}>
                <h2 className={styles.transactionHeading}>Create Transaction</h2>
                <form onSubmit={submitHandler}>
                    <div className={styles.transactionInputDiv}>
                        <select
                            className={styles.transactionInput}
                            value={type}
                            onChange={e => setType(e.target.value)}
                        >
                            <option value="spend">Spend</option>
                            <option value="earn">Earn</option>
                        </select>
                        {transaction.transactionCreateErrors.transaction_type}
                    </div>
                    <div className={styles.transactionInputDiv}>
                        <input
                            className={styles.transactionInput}
                            type="text"
                            value={title}
                            placeholder="Title"
                            onChange={e => setTitle(e.target.value)}
                        />
                        {transaction.transactionCreateErrors.title}
                    </div>
                    <div className={styles.transactionInputDiv}>
                        <input
                            className={styles.transactionInput}
                            type="number"
                            value={amount}
                            placeholder="Amount"
                            onChange={e => setAmount(e.target.value)}
                        />
                        <select
                            className={styles.transactionInput}
                            value={currency}
                            onChange={e => setCurrency(e.target.value)}
                        >
                            {currencies.map(currency => <option key={createUUID()} value={currency[0]}>{currency[1]}</option>)}
                        </select>
                        {transaction.transactionCreateErrors.amount}
                    </div>
                    <div className={styles.transactionInputDiv}>
                        <textarea
                            className={styles.transactionTextarea}
                            value={body}
                            placeholder="Short description"
                            onChange={e => setBody(e.target.value)}
                        />
                        {transaction.transactionCreateErrors.body}
                    </div>

                    <div className={styles.transactionInputDiv}>
                        <input
                            className={styles.transactionInput}
                            type="text"
                            value={tags}
                            placeholder="Tags (Comma seperated)"
                            onChange={e => setTags(e.target.value)}
                        />
                        {transaction.transactionCreateErrors.tags}
                    </div>

                    <button className={styles.createTransactionButton} type="submit" disabled={transaction.loading}>
                        {transaction.loading ? "Saving..." : "Save"}
                    </button>
                </form>
                {Object.keys(transaction.transactionCreateErrors).length > 0 && "Error saving the transaction."}
            </div>
        </LayoutContainer>
    )

}


export default CreateTransaction