# The Scallywags Nanny Dog Walking Service Website & Booking Platform

![Scallywags Nanny logo](/assets/images/SN-logo.jpg)

By Kat Dawes

---

This is the documentation for my web application **The Scallywags Nanny Dog Walking Service Website & Booking Platform**

It is my fourth project for Code Institute’s Diploma in Web Application Development.

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

The user stories are based on questions asked of the business owner. 

Questions asked: 



Resulting user profiles: 
- New potential customer who wants to research services
- New client who wants to book an initial meetup to discuss services and allow their pet/s to meet the business owner 
- Current (registered) client who wants to book/amend booking/update pet details quickly
- Potential client who wants to check information on services and apply to become a customer

As there are so many variables (pets with different needs, walks of different lengths etc.), all customers meet with the owner in person before being able to use the site to book walks. 


---

### Research

#### Market Review

I looked at various sites which offer similar services. 

#### Pawshake

![Pawshake](https://www.pawshake.co.uk/)

- Large site offering services from lots of different individuals 
- Can book 'Meet & Greet' online
- Online booking only after this initial contact
- Clear description of how their system works. https://www.pawshake.co.uk/how-does-pawshake-work
- FAQs etc. get a bit complicated 

#### Sppot

! [Sppot dog walking services](https://sppot.co.uk/dog-walking-service/)

- Sppot does not allow booking via the site; clients must contact them using the form
- The site has clear information about the services offered
- The site offers a lot of contact options ![Sppot Contact Page](https://sppot.co.uk/contact-us/)
- The site is attractive, with pictures of happy dogs

#### Running Duck 

! [Running Duck](https://runningduckpetservices.co.uk/house-sitter-wales/)

- I looked at this site as it is a small service rather than one of the large aggregate sites 
- Reviews and details of sitters are included
- Jumbled design with some good elements; friendly feel of a small, dedicated business 

---

## Deployment


---

### Features

- User Authentication

    Register, login, logout.
    Profiles with editable address and phone number fields.

- Pet Management

    Add/edit/remove pets.
    Form validation for pet details (e.g., mandatory fields like name and age).

- Booking System

    Users can view available slots for dog walking/sitting.
    Booking forms with validation (e.g., check for overlapping slots).

- Stripe Integration

    Payment for bookings through Stripe’s test mode.
    Unlock booking confirmation upon successful payment.

- Navigation and Layout

    Main navigation bar with links: Home, About, Login/Register, My Pets, Bookings.
    Use Bootstrap for responsive design.

- JavaScript Enhancements

    Real-time validation of booking forms (e.g., prevent double-booking on the same slot).
    Interactive calendar to select available slots.

---

### Further Developments

- Ability to book pet-sitting days/weeks online as well as walks. 
- Email notifications for booking confirmations.
- Google Maps integration for service areas.
- Admin dashboard to manage bookings and users.

--- 

## Design, layout, colours

The site needs to conform to the principles of UX in all five different planes.

![Usability](/assets/images/princip-UX.png)

### Content - elements to include

**Headline** - The Scallywags Nanny 

**Tag-line** - Your trusted dog-walking and pet-sitting service in and around Bristol 


---

### Structure

The website consists of four pages: Home, About, Contact, Services  

### Wireframes

I first sketched (on paper) the basic layout for the pages.

Keeping the design clean and simple was a priority both for UX and responsiveness.

- insert scans of drawings

- Figma 

---

#### The Scallywags Nanny Home Page 

Landing page with title, image, tagline, introduction to services. 

Banner image: ![Doggy banner](/assets/images/SN-banner.png)

Logo ![Scallywags Nanny logo](/assets/images/SN-logo.jpg) 

#### The Scallywags Nanny Contact Page 

Contact details and an intro to the business owner, location map, contact form 

Image of business owner: ![Emma O'Leary](/assets/images/SN-ems.jpg)

---

### Colours - Surface plane

The Scallywags Nanny brand uses earth-themed colours, with the logo in yellow, black and white. Whites, blues and greens feature heavily. The app will reflect this.

Colours needed for:

- Titles
- subtitles
- Body text - black
- Backgrounds

![SGS site colours](/assets/images/SGS-colours.png)

---

### Fonts

#### Legibility, accessibility, contrast

I wanted to ensure readability and consistency throughout the app, maintaining a balance between style and readability. I also wanted to ensure that the fonts complement the earthy theme of the main site.

- GoogleFonts
- FontAwesome?
- [ezGIF](https://ezgif.com/) - Creating GIFs for the README
- [Techsini Mockup](https://techsini.com/multi-mockup/) - Creating the mockup images for the README
- [Favicon.io](https://favicon.io/favicon-converter/) - Used to create and add the favicon to the browser tab

Colour palettes from [canva.com/colours](http://canva.com/colours)

1. [Six Hands Rough](https://www.onlinewebfonts.com/download/f6db36f5c636e2adf912702a4ad751ec) font for headings

2. **Roboto Slab:** To provide a contrast to the script font and give a modern and lcean look, I'll use this for subheadings.

3. **Montserrat:** Montserrat is clean and easy to read. I will use this for body text e.g. product description.

4. **Dancing Script:** Dancing Script is another script font, but it's a bit more formal than Pacifico. It can work well for adding an elegant touch to your beach-themed site.

5. **Nunito:** Nunito is a rounded sans-serif font that can be a good choice for body text. It's friendly and easy on the eyes.

6. **Playfair Display:** If you want to add a touch of sophistication to your headings, Playfair Display is an elegant serif font that can work well in combination with script or sans-serif fonts.

---

## Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [WordPress](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi-t4XAqtyAAxUxXEEAHbhkBBQQFnoECBwQAQ&url=https%3A%2F%2Fen-gb.wordpress.org%2F&usg=AOvVaw3_Yh8Jp55SAR0s1nidR2lh&opi=89978449) 
- Python
- PostgreSQL 
- Django

## Bugs and issues

The app does not (yet) work as planned. 

As such, the ReadMe does not yet reflect the  app in its current form. 

---

## Credits

https:// 

Mentor: Richard Wells 

CI tutors: 

---
