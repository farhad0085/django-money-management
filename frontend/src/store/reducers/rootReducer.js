import { combineReducers } from 'redux'
import authReducer from './authReducer'
import transactionReducer from './transactionReducer'
import tagsReducer from './tagsReducer'

const rootReducer = combineReducers({
    auth: authReducer,
    transaction: transactionReducer,
    tags: tagsReducer
})

export default rootReducer