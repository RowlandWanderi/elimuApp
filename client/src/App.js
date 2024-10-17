import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login"
import Profile from "./pages/Profile"
import Register from "./pages/Register"
import SingleCourse from "./pages/SingleCourse"
import Layout from "./layout/Layout"
import NoPage from "./pages/NoPage";
import UserProvider from "./context/UserContext"
import EnrollmentProvider from "./context/EnrollmentContext"
import CourseProvider from "./context/CourseContext";

function App() {
  return (
    <BrowserRouter>
    <UserProvider>
      <EnrollmentProvider>
           <CourseProvider>
            <Routes>
              <Route path="/" element={<Layout />}>
                <Route index element={<Home />} />
                <Route path="/login" element ={<Login />} />
                <Route path="/profile" element ={<Profile />} />
                <Route path="/register" element ={<Register />} />
                <Route path="/courses/:id" element ={<SingleCourse />} />
                <Route path="*" element={<NoPage />} />
              </Route>
            </Routes>
            </CourseProvider>
      </EnrollmentProvider>
    </UserProvider>
    </BrowserRouter>
  );
}

export default App;
