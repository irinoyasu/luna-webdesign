/* ============================================
   人生9割損してるサークル — Main JavaScript
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {
  initSplashScreen();
  initNavigation();
  initScrollReveal();
  initCRTViewer();
  initChalkboard();
  initJoinForm();
});

/* --- Splash Screen --- */
function initSplashScreen() {
  const splash = document.getElementById('splash-screen');
  if (!splash) return;

  setTimeout(() => {
    splash.classList.add('fade-out');
    setTimeout(() => {
      splash.classList.add('hidden');
    }, 600);
  }, 2000);
}

/* --- Navigation --- */
function initNavigation() {
  const hamburger = document.getElementById('hamburger');
  const navLinks = document.getElementById('nav-links');

  if (!hamburger || !navLinks) return;

  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navLinks.classList.toggle('open');
  });

  // Close nav on link click
  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      hamburger.classList.remove('active');
      navLinks.classList.remove('open');
    });
  });

  // Hide nav links on scroll
  let lastScroll = 0;
  window.addEventListener('scroll', () => {
    const currentScroll = window.scrollY;
    if (currentScroll > lastScroll && currentScroll > 100) {
      hamburger.classList.remove('active');
      navLinks.classList.remove('open');
    }
    lastScroll = currentScroll;
  });
}

/* --- Scroll Reveal --- */
function initScrollReveal() {
  const reveals = document.querySelectorAll('.reveal');
  if (reveals.length === 0) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    },
    {
      threshold: 0.15,
      rootMargin: '0px 0px -50px 0px',
    }
  );

  reveals.forEach((el) => observer.observe(el));
}

/* --- CRT TV Slide Viewer --- */
function initCRTViewer() {
  const slides = document.querySelectorAll('.crt-slide');
  const prevBtn = document.getElementById('crt-prev');
  const nextBtn = document.getElementById('crt-next');
  const counter = document.getElementById('slide-counter');
  const staticOverlay = document.getElementById('crt-static');
  const dialLeft = document.getElementById('dial-left');
  const dialRight = document.getElementById('dial-right');

  if (slides.length === 0) return;

  let currentSlide = 0;
  let dialRotation = 0;

  function showSlide(index) {
    // Show static effect
    if (staticOverlay) {
      staticOverlay.classList.add('active');
      setTimeout(() => staticOverlay.classList.remove('active'), 300);
    }

    slides.forEach((slide) => slide.classList.remove('active'));
    slides[index].classList.add('active');

    if (counter) {
      counter.textContent = `${index + 1} / ${slides.length}`;
    }

    // Rotate dial
    dialRotation += 45;
    if (dialRight) {
      dialRight.style.transform = `rotate(${dialRotation}deg)`;
    }
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      currentSlide = (currentSlide - 1 + slides.length) % slides.length;
      showSlide(currentSlide);
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      currentSlide = (currentSlide + 1) % slides.length;
      showSlide(currentSlide);
    });
  }

  // Click on dials
  if (dialLeft) {
    dialLeft.addEventListener('click', () => {
      currentSlide = (currentSlide - 1 + slides.length) % slides.length;
      showSlide(currentSlide);
      dialLeft.style.transform = `rotate(${-dialRotation}deg)`;
    });
  }

  // Initialize first slide
  showSlide(0);
}

/* --- Chalkboard Sticky Notes --- */
function initChalkboard() {
  const input = document.getElementById('chalk-input');
  const submitBtn = document.getElementById('chalk-submit');
  const notesContainer = document.getElementById('chalk-notes');

  if (!input || !submitBtn || !notesContainer) return;

  // Load saved notes from localStorage
  const savedNotes = JSON.parse(localStorage.getItem('chalkNotes') || '[]');
  savedNotes.forEach((note) => addNoteToBoard(note, notesContainer));

  submitBtn.addEventListener('click', () => {
    const text = input.value.trim();
    if (!text) return;

    const noteData = {
      text,
      rotation: (Math.random() * 6 - 3).toFixed(1),
      color: getRandomNoteColor(),
      timestamp: Date.now(),
    };

    addNoteToBoard(noteData, notesContainer);
    savedNotes.push(noteData);
    localStorage.setItem('chalkNotes', JSON.stringify(savedNotes));
    input.value = '';
  });

  input.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
      submitBtn.click();
    }
  });
}

function getRandomNoteColor() {
  const colors = [
    '#fff9c4', // Yellow
    '#f8bbd0', // Pink
    '#b2ebf2', // Cyan
    '#c8e6c9', // Green
    '#d1c4e9', // Lavender
    '#ffe0b2', // Orange
  ];
  return colors[Math.floor(Math.random() * colors.length)];
}

function addNoteToBoard(noteData, container) {
  const note = document.createElement('div');
  note.className = 'chalk-note';
  note.style.cssText = `
    background-color: ${noteData.color};
    transform: rotate(${noteData.rotation}deg);
  `;
  note.textContent = noteData.text;
  container.appendChild(note);
}

/* --- Join Form --- */
function initJoinForm() {
  const form = document.getElementById('join-form');
  const ghost = document.getElementById('join-ghost');

  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = form.querySelector('#form-name');
    const email = form.querySelector('#form-email');
    const message = form.querySelector('#form-message');

    // Simple validation
    let valid = true;
    [name, email, message].forEach((field) => {
      if (field && !field.value.trim()) {
        field.style.borderColor = '#FF6B6B';
        field.style.boxShadow = '3px 3px 0px #FF6B6B';
        valid = false;
      } else if (field) {
        field.style.borderColor = '#000';
        field.style.boxShadow = 'none';
      }
    });

    if (!valid) return;

    // Success animation
    if (ghost) {
      ghost.style.animation = 'none';
      ghost.offsetHeight; // Trigger reflow
      ghost.style.animation = 'ghost-celebrate 0.8s ease forwards';
    }

    // Show success message
    const successMsg = document.createElement('div');
    successMsg.style.cssText = `
      background-color: #4ECDC4;
      color: #fff;
      font-family: 'Dela Gothic One', sans-serif;
      padding: 16px 24px;
      border: 3px solid #000;
      box-shadow: 4px 4px 0px #000;
      text-align: center;
      margin-top: 16px;
      animation: pop-in 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    `;
    successMsg.textContent = '🎉 送信しました！ありがとう！';

    form.reset();
    form.appendChild(successMsg);

    setTimeout(() => {
      successMsg.remove();
    }, 4000);
  });
}

/* --- Additional Animations (injected as style) --- */
const styleSheet = document.createElement('style');
styleSheet.textContent = `
  @keyframes ghost-celebrate {
    0% { transform: scale(1) rotate(0deg); }
    25% { transform: scale(1.2) rotate(-10deg); }
    50% { transform: scale(1.3) rotate(10deg) translateY(-20px); }
    75% { transform: scale(1.1) rotate(-5deg) translateY(-10px); }
    100% { transform: scale(1) rotate(0deg) translateY(0); }
  }

  @keyframes pop-in {
    0% { transform: scale(0.8); opacity: 0; }
    100% { transform: scale(1); opacity: 1; }
  }
`;
document.head.appendChild(styleSheet);
