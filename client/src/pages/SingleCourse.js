import React, { useContext, useEffect, useState } from "react";
import { useParams} from "react-router-dom";
import { CourseContext } from "../context/CourseContext";

export default function SingleCourse() {
  const { id } = useParams();
  
  const [singleCourse, setSingleCourse] = useState(null);
  const { courses, onChange, setOnChange } = useContext(CourseContext);
  const [userRole, setUserRole] = useState('');  // Assume you can get this from user context or JWT

  useEffect(() => {
    const course = courses.find((course) => course.id === parseInt(id));
    setSingleCourse(course);
  }, [id, courses]);

  const handleUpdate = () => {
    const updatedTitle = prompt("Enter new course title:", singleCourse.title);
    const updatedDescription = prompt("Enter new description:", singleCourse.description);

    if (updatedTitle && updatedDescription) {
      fetch(`/courses/${id}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ title: updatedTitle, description: updatedDescription })
      })
      .then(response => {
        if (response.ok) {
          alert("Course updated successfully");
          setOnChange(!onChange); // Trigger re-fetch of data
        } else {
          alert("Error updating course");
        }
      });
    }
  };

  const handleDelete = () => {
    if (window.confirm("Are you sure you want to delete this course?")) {
      fetch(`/courses/${id}`, {
        method: "DELETE"
      })
      .then(response => {
        if (response.ok) {
          alert("Course deleted successfully");
          
        } else {
          alert("Error deleting course");
        }
      });
    }
  };

  return (
    <div className="container">
      {singleCourse && (
        <div key={singleCourse.id}>
          <h2 className="mb-3">{singleCourse.title}</h2>
          <div className="row border-bottom p-3 bg-white mt-3">
            <div className="d-flex">
              <div className="col-md-8 card p-3 d-flex flex-column justify-content-between">
                <div className="mt-4">
                  <h3>Details:</h3>
                  <p><strong>Title:</strong> {singleCourse.title}</p>
                  <p><strong>Description:</strong> {singleCourse.description}</p>
                  <p><strong>Status:</strong> {singleCourse.status}</p>
                </div>
                <div>
                  <h2>Did You Know?</h2>
                  <p>
                    Did you know that over 50% of online learners enroll in
                    multiple courses each year?With our platform, you can easily
                    explore a variety of courses tailored to your interests and
                    career goals. Join a community of lifelong learners and take
                    charge of your education today!
                  </p>
                </div>

                {userRole === "Instructor" && singleCourse.status === "Pending" && (
                  <>
                    <button onClick={handleUpdate} className="btn btn-primary">Update Course</button>
                    <button onClick={handleDelete} className="btn btn-danger">Delete Course</button>
                  </>
                )}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}


