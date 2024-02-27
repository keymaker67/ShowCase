import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom"
import PrivateRoute from './utils/PrivateRoute'
import HomePage from './pages/HomePage'
import LoginPage from './pages/LoginPage'
import NoPage from './pages/NoPage'
import Header from './components/Header'

function App() {
  return (
      <div className="App">
          <BrowserRouter>
                  <Header />
              <Routes>
                  <PrivateRoute index element={<HomePage />} />
                  <PrivateRoute element={<HomePage />} path="/home" exact/>
                  <Route element={<LoginPage />} path="/login" />
                  <Route element={<NoPage />} path="*" />
              </Routes>
          </BrowserRouter>
      </div>
  );
}

export default App;
