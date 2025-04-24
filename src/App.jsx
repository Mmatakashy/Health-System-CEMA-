import { ChakraProvider } from "@chakra-ui/react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";

function App() {
  return (
    <ChakraProvider>
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          {/* Add more routes here as you build: */}
          {/* <Route path="/clients" element={<ClientsPage />} /> */}
        </Routes>
      </Router>
    </ChakraProvider>
  );
}

export default App;
