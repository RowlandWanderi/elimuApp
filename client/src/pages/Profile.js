import React, { useContext, useState } from 'react'
import { UserContext } from '../context/UserContext'

export default function Profile() {
const {currentUser,updateUser, deleteAccount} = useContext(UserContext)



const [username, setUsername] = useState(currentUser && currentUser.username)
const [email, setEmail] = useState(currentUser && currentUser.email)



	const handleSubmit = (e)=>{
	e.preventDefault()

	// call your useContext function
	updateUser(username,email)
	
	
	}
  return (
<section className="vh-80" style={{ backgroundColor: '#f4f5f7' }}>
      <div className="container py-4 h-70">
        <div className="row d-flex justify-content-center align-items-center h-100">
          <div className="col col-lg-6 mb-4 mb-lg-0">
            <div className="card mb-3" style={{ borderRadius: '.5rem' }}>
              <div className="row g-0">
			 
                <div className="col-md-8">
                  <div className="card-body p-4">
                    <h6>Personal Details</h6>
                    <hr className="mt-0 mb-4" />
                    <div className="row pt-1">
					<div className="col-6 mb-3">
                        <h6>username</h6>
                        <p className="text-muted">{currentUser && currentUser.username}</p>
                      </div>
                      <div className="col-6 mb-3">
                        <h6>Email</h6>
                        <p className="text-muted">{currentUser && currentUser.email}</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className="card row mt-5 p-4" style={{ maxWidth: '700px', margin: '0 auto' }}>
        <h5>Update Profile</h5>
        <form onSubmit={handleSubmit}>
          <div className="form-group row my-4">
            <label className="form-label col-sm-2">Username</label>
            <div className="col-sm-10">
              <input value={username} onChange={(e) => setUsername(e.target.value)} type="text" className="form-control" />
            </div>
          </div>
          <div className="form-group row my-4">
            <label className="form-label col-sm-2">Email address</label>
            <div className="col-sm-10">
              <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} className="form-control" />
            </div>
          </div>
          <button type="submit" className="btn btn-success w-40">
            Save
          </button>
        </form>
      </div>
      <div className="card row mt-5 p-4 text-center" style={{ maxWidth: '700px', margin: '0 auto' }}>
        <h5> Delete Profile - Please note this action cannot be reversed</h5>
        <button onClick={deleteAccount} className="btn btn-danger btn-sm d-block mx-auto mt-2 w-50">
		Delete Account
		</button>
      </div>
    </section>
  )
}