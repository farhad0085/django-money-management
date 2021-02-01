import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { login } from "../../store/actions/authActions";
import styles from './styles.module.css';
import LayoutContainer from '../../components/layouts/LayoutContainer';

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
        <LayoutContainer>
            <div className={styles.signInContainer}>
                <div className={styles.signInBox}>
                    <div>
                        <h2 className={styles.loginHeader}>
                            Login to you dashboard
                        </h2>
                    </div>
                    <div>
                        <form onSubmit={submitHandler}>
                            <div>
                                <input
                                    className={styles.loginInput}
                                    type="text"
                                    name="username"
                                    value={username}
                                    onChange={e => setUsername(e.target.value)}
                                />
                            </div>
                            <div>
                                <input
                                    className={styles.loginInput}
                                    type="password"
                                    name="password"
                                    value={password}
                                    onChange={e => setPassword(e.target.value)}
                                />
                            </div>
                            <button className={styles.loginButton} type="submit" disabled={auth.loading}>
                                {auth.loading ? "Logging in..." : "Login"}
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </LayoutContainer>
    );
};

export default SignIn;
