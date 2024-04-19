import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import { BrowserRouter } from "react-router-dom";
import axios from "axios";

const root = ReactDOM.createRoot(document.getElementById("root"));
axios.defaults.baseURL = "https://coolseaweed.duckdns.org";
// axios.defaults.baseURL = "http://localhost:8080";

root.render(
  <React.StrictMode>
    <BrowserRouter basename={process.env.PUBLIC_URL}>
      {console.log(process.env.PUBLIC_URL)}
      <App />
    </BrowserRouter>
  </React.StrictMode>
);
