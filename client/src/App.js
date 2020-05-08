import React, { Fragment } from "react";
import "./App.css";
import { Container } from "semantic-ui-react";
import Navbar from "./components/Navbar";
import ResultList from "./components/ResultList";

function App() {
  return (
     <Fragment>
       <Navbar />
       <Container className="container">
         <ResultList />
       </Container>
     </Fragment>
  );
}

export default App;
