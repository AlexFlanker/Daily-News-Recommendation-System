import React from 'react';
import './About.css';
import logo from '../App/logo.png';
class About extends React.Component {
    render() {
        return (
            <div>
                <img className = 'logo' src={logo} alt='logo' />
                <center>
                <br />
                <br />
                <b><font size = "5">This website is a news website which can always recommend latest news to users based on their preferences and view histroy. </font></b><br />
                Contact Info: <b>Email: ts755@cornell.edu Tele: 347-825-937</b><br />
                All rights reserved<br /></ center>
            </div>
        );
    }
}

export default About;