import React, { useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import LayoutContainer from '../../components/layouts/LayoutContainer'
import { createTransaction } from '../../store/actions/transactionActions'


const CreateTransaction = ({ history }) => {

    const dispatch = useDispatch()
    const transaction = useSelector(state => state.transaction)

    const [amount, setAmount] = useState(0)
    const [title, setTitle] = useState("")
    const [body, setBody] = useState("")
    const [tags, setTags] = useState("")
    const [type, setType] = useState(1)


    const submitHandler = event => {
        event.preventDefault()
        const data = { title, body, amount, tags, transaction_type: type }
        dispatch(createTransaction(data, history))
    }

    return (
        <LayoutContainer>
            <h1>Create Transaction</h1>
            <form onSubmit={submitHandler}>
                <div>
                    <input
                        type="text"
                        value={title}
                        placeholder="Title"
                        onChange={e => setTitle(e.target.value)}
                    />
                </div>
                <div>
                    <input
                        type="number"
                        value={amount}
                        placeholder="Amount"
                        onChange={e => setAmount(e.target.value)}
                    />
                </div>
                <div>
                    <textarea
                        value={body}
                        placeholder="Short description"
                        onChange={e => setBody(e.target.value)}
                    />
                </div>
                <div>
                    <select
                        value={type}
                        onChange={e => setType(e.target.value)}
                    >
                        <option value={0}>Earn</option>
                        <option value={1}>Spend</option>
                    </select>
                </div>
                <div>
                    <input
                        type="text"
                        value={tags}
                        placeholder="Tags (Comma seperated)"
                        onChange={e => setTags(e.target.value)}
                    />
                </div>

                <button type="submit" disabled={transaction.loading}>
                    {transaction.loading ? "Saving..." : "Save"}
                </button>
            </form>
        </LayoutContainer>
    )

}


export default CreateTransaction