import * as Types from "./actionTypes";
import axios from "../../utils/axios";
import { getHeaders, getTagsList } from '../../utils';



export const createTransaction = (transactionData) =>(dispatch) => {
    
    // first create tags
    const tagsRawData = transactionData.tags
    const tags = getTagsList(tagsRawData)

    axios.post("/tags/", tags, { headers: getHeaders()})
    .then(res => {
        transactionData.tags = [...res.data.map(tag => tag.id)]
        
        // now create transaction with those tags
        axios.post("/transactions/", transactionData, { headers: getHeaders()})
            .then(res => {
                console.log(res.data);
            })
            .catch(error => {
                console.log(error.response);
                dispatch({type: Types.TRANSACTION_CREATE_ERROR, payload: error.response.data})
            })
    })
    .catch(error => {
        console.log(error);
        dispatch({type: Types.TRANSACTION_CREATE_ERROR, payload: error.response.data})
    })

    
}