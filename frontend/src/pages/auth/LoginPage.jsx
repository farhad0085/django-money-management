import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { login } from "../../store/actions/authActions";


const SignIn = ({ history }) => {
    const auth = useSelector((state) => state.auth);
    const dispatch = useDispatch();

    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")

    const submitHandler = (event) => {
        event.preventDefault()
        dispatch(login({ username, password }, history));
    };

    return (
        <div>
            <div>
                <h2>
                    Login to you dashboard
                </h2>
            </div>
            <div>
                <form onSubmit={submitHandler}>
                    <div>
                        <input
                            type="text"
                            name="username"
                            value={username}
                            onChange={e => setUsername(e.target.value)}
                        />
                    </div>
                    <div>
                        <input
                            type="password"
                            name="password"
                            value={password}
                            onChange={e => setPassword(e.target.value)}
                        />
                    </div>
                    <button type="submit" disabled={auth.loading}>
                        {auth.loading ? "Logging in..." : "Login"}
                    </button>
                </form>
            </div>
        </div>
    );
};

export default SignIn;
