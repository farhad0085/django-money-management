import * as Types from "./actionTypes";
import axios from "../../utils/axios";
import { getHeaders, getTagsList } from '../../utils';


export const createTransaction = (transactionData, history) => dispatch => {
    dispatch({type: Types.TRANSACTION_CREATE_ERROR, payload: {}})

    dispatch({ type: Types.TRANSACTION_LOADING, payload: true })
    // first create tags
    const tagsRawData = transactionData.tags
    const tags = getTagsList(tagsRawData)
    transactionData.tags = tags

    // now create transaction with those tags
    axios.post("/transactions/", transactionData, { headers: getHeaders()})
        .then(res => {
            // console.log(res.data);
            history.push("/transactions")
            dispatch({ type: Types.TRANSACTION_LOADING, payload: false })
        })
        .catch(error => {
            // console.log(error.response);
            dispatch({type: Types.TRANSACTION_CREATE_ERROR, payload: error.response.data})
            dispatch({ type: Types.TRANSACTION_LOADING, payload: false })
        })
    
}

export const getAllTransactions = () => dispatch => {
    dispatch({ type: Types.TRANSACTION_LOADING, payload: true })

    axios.get("/transactions/", { headers: getHeaders()})
    .then(res => {
        dispatch({type: Types.TRANSACTION_LOADED, payload: res.data})
        dispatch({ type: Types.TRANSACTION_LOADING, payload: false })
    })
    .catch(error => {
        console.log(error);
        dispatch({type: Types.TRANSACTION_LOAD_ERROR, payload: error.response.data})
        dispatch({ type: Types.TRANSACTION_LOADING, payload: false })
    })
    
}