import React,  { useContext, useState } from 'react'
import { Link } from 'react-router-dom';
import { CourseContext } from '../context/CourseContext';



export default function Home() {

  const { courses } = useContext(CourseContext)

  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState([]);


  // Function to filter courses based on search term
  const handleSearch = () => {
    const results = courses.filter((course) =>
      course.title.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setSearchResults(results);
  };

  return (
    <div>
      <div>
        <h1 className="text-center">WELCOME TO ELIMU APP!</h1>
        <h2 className="text-center">YOUR NUMBER ONE PLATFORM FOR FREE ONLINE COURSES!</h2>
      </div>

      <div className="card text-bg-dark">
        <img src="" className="card-img" alt="Loading Banner" />
      </div>

      <div className='container bg-info me-3'>
        <h2 className=' text-center my-3'>Courses</h2>

        {/* Search bar */}
        <div className='mb-3 container'>
          <input
          className='col-md-6 ms-5 '
            type='text'
            placeholder='Search Course Store...'
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
          <button className='btn btn-success col-md-3 ms-2' onClick={handleSearch}>Search</button>
        </div>

        {searchResults.length > 0 ? (
          // Display search results
          searchResults.map((course) => (
            <div key={course.id} className='row border-bottom p-3 bg-white mt-3'>
              
              <div className='col-md-3 d-flex flex-column'>
                <img src="" alt="loading"/>
              </div>
              <div className='col-md-3 d-flex flex-column mt-5 '>
                <h3>{course.title}</h3>
                <p>Description: {course.description}</p>
              </div>

              <div className='col-md-3 mt-5'>
                <button className='btn btn-light'>
                  <Link to={`/courses/${course.id}`} className='fw-bold'>
                    View Course
                  </Link>
                </button>
              </div>
            </div>
          ))
        ) : (
          // Display all courses if no search results
          courses.map((course) => (
            <div key={course.id} className='row border-bottom p-3 bg-white mt-3'>
              {console.log(course)}
              <div className='col-md-3 d-flex flex-column'>
                <img src="" alt="loading"/>
              </div>
              <div className='col-md-3 d-flex flex-column mt-5 '>
                <h3>{course.title}</h3>
                <p>Description: {course.description}</p>
              </div>

              <div className='col-md-3 mt-5'>
                <button className='btn btn-light'>
                  <Link to={`/courses/${course.id}`} className='fw-bold'>
                    View Course
                  </Link>
                </button>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}