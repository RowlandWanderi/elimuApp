from app import app, db, User, Enrollment, Course
from faker import Faker
import random

fake = Faker()

# Array of ROLES for the users
rolesArray = ["Student", "Instructor", "Approver"]

# Array of book descriptions
book_descriptions = [
    "A psychological thriller about a woman who shoots her husband and then stops speaking.",
    "A coming-of-age story set in the marshes of North Carolina, blending mystery and romance.",
    "A novel that explores the infinite possibilities of life through the story of a woman who discovers a library of alternate realities.",
    "A practical guide to building good habits and breaking bad ones, emphasizing small changes that lead to significant transformations.",
    "A memoir of a woman who grows up in a strict and abusive household in rural Idaho, ultimately pursuing her education.",
    "The story of two twin sisters who take different paths in life, exploring themes of race, identity, and family.",
    "A retelling of Greek mythology through the eyes of Circe, the enchantress who turned Odysseus's men into pigs.",
    "A fictional oral history of a fictional rock band, exploring love, fame, and the music industry.",
    "A tale of magic and mystery, set in a circus that only opens at night, filled with enchanting performances and a fierce competition.",
    "The story of a Russian count who is sentenced to house arrest in a grand hotel, navigating the changing world around him.",
    "A sweeping tale of old Hollywood, following the life of a glamorous actress and her seven husbands.",
    "A survival story of a family in the Alaskan wilderness, dealing with love, loss, and the harsh realities of nature.",
    "A gripping novel about family dynamics and societal issues, set in a suburban neighborhood.",
    "A fantastical tale of a young woman who struggles to be remembered in a world that forgets her.",
    "A quirky and heartfelt story about a group of strangers held hostage during an open house.",
    "A poignant narrative set in Nazi Germany, narrated by Death, focusing on the power of books to sustain the human spirit.",
    "An epic historical saga following four generations of a Korean family as they navigate love and loss.",
    "A philosophical tale about following one's dreams and the journey toward personal legend.",
    "A sequel to The Handmaid's Tale, exploring the lives of women in a dystopian society.",
    "A contemporary love story that captures the complexities of modern relationships and emotional struggles."
]


def seed_data():
    with app.app_context():
        
        print('<<<<<<=Deleting existing seed data=>>>>>>')
        User.query.delete()
        Enrollment.query.delete()
        Course.query.delete()
        
        db.create_all()
        
        print('<<<<<<=Seeding new data to the tables=>>>>>>')
        
        # Users data
        users = []
        for _ in range(15):
            user = User(
                username=fake.name(),
                email=fake.email(),
                password=fake.password(),
                role=random.choice(rolesArray)
            )
            users.append(user)
            db.session.add(user)
        db.session.commit()
        
        # Courses data
        courses = []
        for _ in range(20):
            course = Course(
                title=fake.company(),
                description=random.choice(book_descriptions),
                user_id=random.choice(users).id  # Associate the course with a random user
            )
            courses.append(course)
            db.session.add(course)
        db.session.commit()
        
        # Enrollments data
        print('<<<<<<=Creating enrollments=>>>>>>')
        for user in users:
            for _ in range(random.randint(1, 5)):  # Each user enrolls in 1 to 5 courses
                enrollment = Enrollment(
                    student_id=user.id,
                    course_id=random.choice(courses).id
                )
                db.session.add(enrollment)
        db.session.commit()

        print('<<<<<<= Completed seeding! =>>>>>>')

if __name__ == '__main__':
    seed_data()