import React from 'react'

const NotFound = ({ history }) => {

    return (
        <div>
            <h1>Page not found</h1>
            <button onClick={() => history.push("/")}>Go Home</button>
        </div>
    )

}


export default NotFound