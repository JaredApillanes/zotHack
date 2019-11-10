import logo from "./league-of-legends-logo.png";
import React from "react";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";

function Home(e) {
    return (
        <div className="App-header">
            <header>
            <img src={logo} className="App-logo" alt="logo" />
            </header>
          <Form.Group controlId="name">
              <Form.Text>
                  Enter Username:
              </Form.Text>
                <p></p> <Form.Control placeholder="Enter your name"></Form.Control>
          </Form.Group>
            <Button variant = 'secondary'>Test</Button>
        </div>
    )
}

export default Home