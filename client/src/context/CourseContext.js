import React, { createContext, useEffect, useState } from 'react';

export const CourseContext = createContext();

export default function CourseProvider({ children }) {
    const [courses, setCourses] = useState([]);
    const [selectedCourse, setSelectedCourse] = useState(null);
    const [onChange , setOnChange] = useState(false)


    useEffect(() => {
        console.log('Fetching courses...');
        fetch('/courses')
            .then((response) => response.json())
            .then((data) => {
                console.log('Fetched courses:', data);
                setCourses(data);
            })
            .catch((error) => console.error('Error fetching courses:', error));
    }, [onChange]);

    const fetchCourseById = (id) => {
        console.log(`Fetching course with ID ${id}...`);
        fetch(`/courses/${id}`)
            .then((response) => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then((data) => {
                console.log(`Fetched course with ID ${id}:`, data);
                setSelectedCourse(data);
            })
            .catch((error) => console.error(`Error fetching course with ID ${id}:`, error));
    };
    const contextData = {
        courses,
        selectedCourse,
        fetchCourseById,
        onChange,
        setOnChange,
    }

    return (
        <CourseContext.Provider value={contextData}>
            {children}
        </CourseContext.Provider>
    );
}
