import React, {useState} from "react";
import './ScoreScreen.css';
import Table from "react-bootstrap/Table";

import axios from "axios";


function ScoreScreen() {

    const [allUsers, setAllUsers] = useState([]);
    const [user, setUser] = useState({
        'username': '',
        'score': ''
    });


    function iterateUsers(e) {
        axios.get("/player/list").then(res => {

            }
        );
        return (<tr><td>Test</td></tr>)
    }

        return (
            <div class="App-header">
                <Table class="Score">
                    <thead>
                    <th>
                        USERNAME
                    </th>
                    </thead>
                    <th>
                        SCORE
                    </th>
                    <tbody>
                    {allUsers.map((q, s) => (
                        <div index={s} key={s}>
                            <tr>
                                <td>q.username</td>
                                <td>q.score</td>
                            </tr>
                        </div>
                    ))}
                    </tbody>
                </Table>
            </div>
        )
    }

    export default ScoreScreen;