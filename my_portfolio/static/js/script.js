const sections = document.querySelectorAll('section[id]')

window.addEventListener('scroll', scrollActive)

function scrollActive(){
    const scrollY = window.pageYOffset

    sections.forEach(current =>{
        const sectionHeight = current.offsetHeight
        const sectionTop = current.offsetTop - 50;
        sectionId = current.getAttribute('id')

        if(scrollY > sectionTop && scrollY <= sectionTop + sectionHeight){
            document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.add('active')
        }else{
            document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.remove('active')
        }
    })
}

/*===== SCROLL REVEAL ANIMATION =====*/
const sr = ScrollReveal({
    origin: 'top',
    distance: '80px',
    duration: 2000,
    reset: true
})

/*SCROLL HOME*/
sr.reveal('.text-uppercase', {})
sr.reveal('.social', {delay: 200})
sr.reveal('.home__image', {origin:'right', delay: 400})

/*SCROLL ABOUT*/
sr.reveal('.about_img', {delay: 500})
sr.reveal('.about_profession', {delay: 400})
sr.reveal('.about_text', {delay: 500})

/*SCROLL SKILLS*/
sr.reveal('.skills-title', {})
sr.reveal('.skills-text', {})
sr.reveal('.skills-name', {distance: '20px', delay: 50, interval: 100})

/*SCROLL PORTFOLIO*/
sr.reveal('.card-img-top', {interval: 200})

/*SCROLL CONTACT*/
sr.reveal('.contact__subtitle', {})
sr.reveal('.contact__text', {interval: 200})
sr.reveal('.message', {delay: 400})



function myFunction() {
    document.getElementById("contact-form").reset();
  }
