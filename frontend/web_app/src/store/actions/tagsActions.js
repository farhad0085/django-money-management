import * as Types from "./actionTypes";
import axios from "../../utils/axios";
import { getHeaders, getTagsList } from '../../utils';


export const createTags = (tagsRawData) => dispatch => {
    const tags = getTagsList(tagsRawData)

    axios.post("/tags/", tags, { headers: getHeaders()})
    .then(res => {
        console.log(res.data);
    })
    .catch(error => {
        console.log(error.response);
        dispatch({type: Types.TRANSACTION_CREATE_ERROR, payload: error.response.data})
    })
}