import logo from "./titleLogo.png";
import React, {useState} from "react";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import './Home.css';

import axios from "axios";

function Home(props) {

    async function handleSubmit(e) {
        e.preventDefault();
        let tempName = e.target.elements.name.value;

        axios.post("localhost:5000/createplayer", {"name": tempName}).then((res) => {
            localStorage.setItem("playerID", JSON.stringify(res.data));
        });

        props.history.push('/Play/');
    }

    return (
        <div className="App-header">
            <header>
                <img src={logo} className="App-logo" alt="logo"/>
            </header>
            <Form className="start-game" onSubmit={handleSubmit}>
                <Form.Group controlId="name">
                    <Form.Text>
                        <p>Enter Username:</p>
                    </Form.Text>
                    <Form.Control placeholder="Enter your name"></Form.Control>
                </Form.Group>
                <Button type='submit'>Play</Button>
            </Form>
        </div>
    )
}


export default Home