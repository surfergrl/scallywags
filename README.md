# The Scallywags Nanny Dog Walking Service Website & Booking Platform

![Scallywags Nanny logo](https://github.com/surfergrl/scallywags/blob/main/static/node_modules/startbootstrap-small-business/dist/assets/SN-logo.jpg)

By Kat Dawes

---

This is the documentation for my web application **The Scallywags Nanny Dog Walking Service Website & Booking Platform**

It is my fourth project for Code Institute’s Diploma in Web Application Development.

The app is not fully operational. 

Operational:
- Structure and navigation 
- User interaction (contact form)
- Documentation (read me and intake form)
- Version control (GitHub)
- Attribution
- Deployment (Heroku)
- Security

Not implemented: 
- Database
- Django apps
- Stripe integration 

### Overview 
A Django-based platform where users can book dog walking or sitting sessions, save their pet's details, and make payments. Additional features include user authentication, Stripe integration for payments, and an intuitive UI/UX enhanced with JavaScript.

## Table of Contents

- Project Development & Planning
  - Project Goals
  - User Stories  
  - Research
- Content
- Design, Layout & Structure
  - Colours
- Features
- Structure & Site Functionality
  - Technologies Used
  - Database Structure 
  - Deployment - Setup Instructions: Step-by-step guide for local setup.
  - Testing & Bugs
- Credits

---

## Project Development and Planning

### Project Details & Goals

- Title: The Scallywags Nanny Dog Walking Service Website & Booking Platform 
- Purpose: To showcase dog-walking and dog-sitting services and allow clients to upload pet details and book services. 
- External user's goal: See the range of services and book to suit them. 
- Site owner's goals:
  - To showcase services 
  - To allow buyers to book easily 
  - To capture new clients 
  - To show that the company is established, experienced, trustworthy and caring 
  - To increase revenue
  - To reduce administrative tasks 
- Required skills: JavaScript, HTML, CSS, Python, PostgreSQL. Other skills: image manipulation, GitHub, Heroku. 

---

### User Stories

The user stories are based on questions asked of the business owner. This can be found in the file [user-intake.md](user-intake.md)

Resulting user profiles: 
- New potential customer who wants to research services
- New client who wants to book an initial meetup to discuss services and allow their pet/s to meet the business owner 
- Current (registered) client who wants to book/amend booking/update pet details quickly
- Potential client who wants to check information on services and apply to become a customer

As there are so many variables (pets with different needs, walks of different lengths etc.), all customers meet with the owner in person before being able to use the site to book walks. This should be bookable online. 

---

### Research

#### Market Review

I looked at various sites which offer similar services. 

![Pawshake](https://www.pawshake.co.uk/)

- Large site offering services from lots of different individuals 
- Can book 'Meet & Greet' online
- Online booking only after this initial contact
- Clear description of how their system works. https://www.pawshake.co.uk/how-does-pawshake-work
- FAQs etc. get a bit complicated 

![Sppot dog walking services](https://sppot.co.uk/dog-walking-service/)

- Sppot does not allow booking via the site; clients must contact them using the form
- The site has clear information about the services offered
- The site offers a lot of contact options ![Sppot Contact Page](https://sppot.co.uk/contact-us/)
- The site is attractive, with pictures of happy dogs

![Running Duck](https://runningduckpetservices.co.uk/house-sitter-wales/)

- I looked at this site as it is a small service rather than one of the large aggregate sites 
- Reviews and details of sitters are included
- Jumbled design with some good elements; friendly feel of a small, dedicated business

Most small or micro-business dog-walking services have a basic brochure website with no booking options. Or walkers use a bigger site like Pawshake. Emma wants to be top of her league with a professional site that does more than the basics. 

---

## Deployment

Available at https://git.heroku.com/scallywags.git 

---

### Features

#### User Authentication
- Register, login, logout. 
- Forgot password system. 
- Profiles with editable address, phone number and client photo fields.

#### Pet Management
- Add/edit/remove pets.
- Form validation for pet details (e.g., mandatory fields like name and age).
- Pet info: Name, age, breed, behavioural issues, medical issues, vet contact details, max walk length, any other notes, photo, equipment (lead etc.), treats y/n, commands to use, pickup instructions (e.g. keypad number).
- Agreemet to terms & conditions - mandatory tick box 

#### Booking System
- Users can view available slots for dog walking/sitting/meet & greet appointment.
- Booking forms with validation (e.g., check for overlapping slots).

#### Stripe Integration
- Payment for bookings through Stripe’s test mode.
- Email booking confirmation upon successful payment.
- (Future feature - appointment reminders.) 

#### Navigation and Layout
- Main navigation bar with links: Home, About, Contact, Services, Login
- Bootstrap for responsive design.

#### JavaScript Enhancements
- Real-time validation of booking forms (e.g., prevent double-booking on the same slot).
- Interactive calendar to select available slots.

---

### Further Developments

- Ability to book pet-sitting days/weeks online as well as walks. 
- Google Maps integration for service areas.
- Admin dashboard to manage bookings and users.

--- 

### Structure

#### App Structure

##### Main App (core)
- Handles the landing page, about section, navigation, and site-wide settings.

##### User Authentication App (users)
- Handles user registration, login, and profile management.

##### Pets App (pets)
- Allows users to save details about their pets (e.g., name, breed, age, medical notes).

##### Booking App (booking)
- Manages booking of dog walking or sitting sessions, availability, and schedule display.

##### Payments App (payments)
- Integrates Stripe for payment processing, tracks completed payments, and unlocks booking confirmations.

#### Database Structure 

##### User (AbstractUser)
- Extended user model for additional fields like address and phone number.

##### Pet
- Fields: user (ForeignKey), name, breed, age, medical_notes, profile_picture
- Relationship: Many pets per user.

##### Booking
- Fields: user (ForeignKey), pet (ForeignKey), service_type (choices: Walking, Sitting), date, time, duration, status (Pending/Confirmed)
- Relationship: One booking per pet per session.

##### Payment
- Fields: user (ForeignKey), booking (ForeignKey), amount, payment_status, transaction_id
- Relationship: One payment per booking.

---

## Design, layout, colours

The site needs to conform to the principles of UX in all five different planes.

![Usability](https://github.com/surfergrl/sgs-gift-guide/blob/main/assets/images/princip-UX.png) 

### Content - elements to include

##### Headline 
The Scallywags Nanny 

##### Tag-line 
Your trusted dog-walking and pet-sitting service in and around Bristol 

---
### Wireframes

I first sketched (on paper) the basic layout for the pages.

Keeping the design clean and simple was a priority both for UX and responsiveness.

- insert scans of drawings

- Wireframes

--- 

### Structure

The website consists of 5 pages: Home, About, Contact, Services and Login.   

---

#### The Scallywags Nanny Home Page 

Landing page with title, image, tagline, introduction to services. 

- Banner image:
![Doggy banner](https://github.com/surfergrl/scallywags/blob/main/static/node_modules/startbootstrap-small-business/dist/assets/SN-banner.png)

- Logo:
![Scallywags Nanny logo](https://github.com/surfergrl/scallywags/blob/main/static/node_modules/startbootstrap-small-business/dist/assets/SN-logo.jpg)

- Introductory text.
- Three cards with text sending users to About, Services or Contact pages via call to action buttons.

#### About Page 

- Collage image of business owner and dogs: ![Emma and dogs](https://github.com/surfergrl/scallywags/blob/main/static/node_modules/startbootstrap-small-business/dist/assets/SN-collage.jpg)
- Three cards with text detailing qualifications, services, why me? info and call to action (book or contact).

#### The Scallywags Nanny Contact Page 

- Intro text 'Every dog requires a meet-and-greet session before we can go out walking! Please get in touch via the form below.'
- Simple JavaScriprt contact form.  

#### The Scallywags Nanny Services Page 

- Javascript gallery 
- Login button
- Meet & Greet booking button
- Three cards with call to action (book or enquire) for bookable-online services

#### The Scallywags Nanny Login Page 

- Username/password form
- Forgot password? link
- Explanatory text right hand column 

---

### Colours - Surface plane

- The Scallywags Nanny brand uses earth-themed colours, with the logo in yellow, black and white. Whites, blues and greens feature heavily. The app will reflect this. 
- The client has provided lots of images of their own; the focus should be on these so the surrounding design should be simple to show them off.

---

### Fonts

#### Legibility, accessibility, contrast

I wanted to ensure readability and consistency throughout the app, maintaining a balance between style and readability. I also wanted to ensure that the fonts complement the earthy theme of the main site.

- GoogleFonts
- FontAwesome 
- [ezGIF](https://ezgif.com/) - GIFs for the README
- [Techsini Mockup](https://techsini.com/multi-mockup/) - mockup images for the README
- [Favicon.io](https://favicon.io/favicon-converter/) - Create and add favicon to the browser tab
- Colour palettes from [canva.com/colours](http://canva.com/colours)

Fonts - complement the logo colours/style  
1. [Six Hands Rough](https://www.onlinewebfonts.com/download/f6db36f5c636e2adf912702a4ad751ec) font for headings
2. subheadings
3. body text

---

## Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- Python
- Heroku
- GitHub
- 

## Testing, Bugs and issues

The app does not yet work as planned. 

As such, the ReadMe does not yet reflect the  app in its current form. 

---

## Credits

[Start Bootstrap](https://github.com/StartBootstrap/startbootstrap-small-business)

Mentor: Richard Wells 



---
