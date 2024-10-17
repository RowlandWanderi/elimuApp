import { createContext, useState, useEffect } from 'react';
import Swal from 'sweetalert2';
import { useNavigate } from 'react-router-dom';

export const EnrollmentContext = createContext();

export default function EnrollmentProvider({ children }) {
    const [enrolledCourses, setEnrolledCourses] = useState([]);
    const [onChange, setOnChange] = useState(false); 
    const navigate = useNavigate();
    
    // Enroll in a course
    const enrollInCourse = (courseId) => {
        fetch('/enroll', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                Authorization: `Bearer ${sessionStorage.getItem("authToken")}` // Use token from session storage
            },
            body: JSON.stringify({ course_id: courseId }),
        })
            .then(res => res.json())
            .then(response => {
                if (response.success) {
                    Swal.fire({
                        position: 'center',
                        icon: 'success',
                        title: 'Successfully enrolled in the course!',
                        showConfirmButton: false,
                        timer: 1500,
                    });
                    setOnChange(!onChange); // Trigger re-fetch of enrolled courses
                } else {
                    Swal.fire({
                        position: 'center',
                        icon: 'error',
                        title: response.error,
                        showConfirmButton: false,
                        timer: 1500,
                    });
                }
            })
            .catch(error => {
                console.error('Error enrolling in course:', error);
            });
    };

    // Fetch enrolled courses
    const fetchEnrolledCourses = () => {
        fetch('/enrollments', {
            method: 'GET',
            headers: {
                Accept: 'application/json',
                Authorization: `Bearer ${sessionStorage.getItem("authToken")}` // Use token from session storage
            },
        })
            .then(res => res.json())
            .then(response => {
                setEnrolledCourses(response); // Update state with enrolled courses
            })
            .catch(error => {
                console.error('Error fetching enrolled courses:', error);
            });
    };

    // Unenroll from a course
    const unenrollFromCourse = (courseId) => {
        fetch(`/enrollments/${courseId}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                Authorization: `Bearer ${sessionStorage.getItem("authToken")}` // Use token from session storage
            },
        })
            .then(res => res.json())
            .then(response => {
                if (response.success) {
                    Swal.fire({
                        position: 'center',
                        icon: 'success',
                        title: 'Successfully unenrolled from the course!',
                        showConfirmButton: false,
                        timer: 1500,
                    });
                    setOnChange(!onChange); // Trigger re-fetch of enrolled courses
                } else {
                    Swal.fire({
                        position: 'center',
                        icon: 'error',
                        title: response.error,
                        showConfirmButton: false,
                        timer: 1500,
                    });
                }
            })
            .catch(error => {
                console.error('Error unenrolling from course:', error);
            });
    };

    // Effect to fetch enrolled courses when component mounts or onChange state updates
    useEffect(() => {
        fetchEnrolledCourses();
    }, [onChange]);

    const contextData = {
        enrolledCourses,
        enrollInCourse,
        unenrollFromCourse,
    };

    return (
        <EnrollmentContext.Provider value={contextData}>
            {children}
        </EnrollmentContext.Provider>
    );
}
