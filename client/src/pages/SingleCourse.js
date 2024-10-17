import React, { useContext, useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { CourseContext } from "../context/CourseContext";

export default function SingleCourse() {
  const { id } = useParams();
  const [singleCourse, setSingleCourse] = useState([]);
  const { courses } = useContext(CourseContext);

  useEffect(() => {
    const course = courses.find((singleCourse) => {
      return singleCourse.id === parseInt(id);
    });
    setSingleCourse(course);
  }, [id, courses]);

  return (
    <div className="container">
      {singleCourse && (
        <div key={singleCourse.id}>
          <h2 className="mb-3">{singleCourse.title}</h2>
          <div className="row border-bottom p-3 bg-white mt-3">
            <div className="d-flex">
              <div className="col-md-4">
                <img
                  src=""
                  alt={singleCourse.title}
                  className="img-fluid"
                  style={{ maxWidth: "100%", height: "auto" }}
                />
              </div>
              <div className="col-md-8 card p-3 d-flex flex-column justify-content-between">
                <div className="mt-4">
                  <h3>Details:</h3>
                  <p>
                    <strong>Title:</strong> {singleCourse.title}
                  </p>
                  <p>
                    <strong>Description:</strong> {singleCourse.description}
                  </p>
                  <p>
                    <strong>Status:</strong> {singleCourse.status}
                  </p>
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
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
