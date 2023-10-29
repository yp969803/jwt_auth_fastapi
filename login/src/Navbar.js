import React, { Component } from "react";
import { Link } from "react-router-dom";
import logoo from './logo4.jpeg';
class Navbar extends Component {
  render() {
    return (
      <>
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
          <div class="container-fluid">
            <img className="imgnav" src={logoo} alt="Briefify.AI"/>
            {/* <a class="navbar-brand" href="#">
              Briefify.ai
            </a> */}
            <button
              class="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarSupportedContent"
              aria-controls="navbarSupportedContent"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item nav-link active">Home</li>
                <li class="nav-item nav-link active">About Us</li>
                <li class="nav-item nav-link active">Disabled</li>
              </ul>
              <button class="btn btn-outline-info">
                <Link to="/login">Login</Link>
              </button>
              <button class="btn btn-outline-info">
                <Link to="/register">Register</Link>
              </button>
            </div>
          </div>
        </nav>
      </>
    );
  }
}

export default Navbar;
