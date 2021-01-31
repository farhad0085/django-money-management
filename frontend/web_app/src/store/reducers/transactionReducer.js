import * as Types from '../actions/actionTypes'

const initialState = {
    loading: false,
    transactionCreatedData: {},
    transactionCreateErrors: {},
    transactions: []
}

function transactionReducer(state = initialState, action) {
    switch (action.type) {
        case Types.TRANSACTION_CREATED: {
            return {
                ...state,
                transactionCreatedData: action.payload
            }
        }
        case Types.TRANSACTION_CREATE_ERROR: {
            return {
                ...state,
                transactionCreateErrors: action.payload
            }
        }
        case Types.TRANSACTION_LOADED: {
            return {
                ...state,
                transactions: action.payload
            }
        }
        default: return state
    }
}

export default transactionReducer