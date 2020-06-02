function parent(userID, password, email) {
  this.userID = userID;
  this.password = password;
  this.email = email; 	  

}

function child(name, parentUserID) {
  this.name = name;
  this.parentUserID = parentUserID;
}

function calendarEvent(eventID, childName){
  this.eventID = eventID;
  this.childName = childName;
}


(function () {
  const doc = document.documentElement

  doc.classList.remove('no-js')
  doc.classList.add('js')

  // Reveal animations
  if (document.body.classList.contains('has-animations')) {
    /* global ScrollReveal */
    const sr = window.sr = ScrollReveal()

    sr.reveal('.hero-title, .hero-paragraph, .hero-cta', {
      duration: 1000,
      distance: '40px',
      easing: 'cubic-bezier(0.5, -0.01, 0, 1.005)',
      origin: 'bottom',
      interval: 150
    })

    sr.reveal('.feature, .pricing-table', {
      duration: 600,
      distance: '40px',
      easing: 'cubic-bezier(0.5, -0.01, 0, 1.005)',
      interval: 100,
      origin: 'bottom',
      viewFactor: 0.5
    })

    sr.reveal('.feature-extended-image', {
      duration: 600,
      scale: 0.9,
      easing: 'cubic-bezier(0.5, -0.01, 0, 1.005)',
      viewFactor: 0.5
    })
  }
}())
