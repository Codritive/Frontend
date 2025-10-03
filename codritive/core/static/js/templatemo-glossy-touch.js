// ==================== Page Navigation ====================
let currentPage = 'home';
    function showPage(pageId) {
        document.querySelectorAll('.page').forEach(page => page.classList.remove('active'));
        document.getElementById(pageId).classList.add('active');

        document.querySelectorAll('.nav-links a').forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('onclick') === `showPage('${pageId}')`) {
                link.classList.add('active');
            }
        });

        currentPage = pageId;

        const footer = document.getElementById('footer');
        const activePage = document.getElementById(pageId);
        activePage.appendChild(footer);

        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
    window.addEventListener('DOMContentLoaded', () => {
        const footer = document.getElementById('footer');
        const homePage = document.getElementById('home');
        homePage.appendChild(footer);
    });

    // ==================== Parallax ====================
    document.addEventListener('mousemove', e => {
        const shapes = document.querySelectorAll('.shape');
        const x = e.clientX / window.innerWidth;
        const y = e.clientY / window.innerHeight;

        shapes.forEach((shape, index) => {
            const speed = (index + 1) * 0.5;
            const xPos = (x - 0.5) * speed * 20;
            const yPos = (y - 0.5) * speed * 20;
            shape.style.transform = `translate(${xPos}px, ${yPos}px)`;
        });
    });
            // Add scroll-based animations
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const parallax = document.querySelector('.bg-shapes');
        const speed = scrolled * 0.5;
        parallax.style.transform = `translateY(${speed}px)`;
    });

    // ==================== Form Submission ====================
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(e){
            e.preventDefault();
            const successMsg = document.createElement('div');
            successMsg.style.cssText = `
                position: fixed;
                top:50%; left:50%;
                transform: translate(-50%, -50%);
                background: rgba(46, 204, 113,0.9);
                color:white; padding:20px 40px;
                border-radius:10px; backdrop-filter: blur(20px);
                z-index:10000; animation: fadeIn 0.3s ease;
            `;
            successMsg.textContent = 'Message sent successfully! We\'ll get back to you soon.';
            document.body.appendChild(successMsg);
            setTimeout(()=>successMsg.remove(),3000);
            this.reset();
        });
    }
    // const form = document.querySelector('form');
    // if (form) {
    //     form.addEventListener('submit', function(e){
    //         e.preventDefault();
    //         const successMsg = document.createElement('div');
    //         successMsg.style.cssText = `
    //             position: fixed;
    //             top:50%; left:50%;
    //             transform: translate(-50%, -50%);
    //             background: rgba(46, 204, 113,0.9);
    //             color:white; padding:20px 40px;
    //             border-radius:10px; backdrop-filter: blur(20px);
    //             z-index:10000; animation: fadeIn 0.3s ease;
    //         `;
    //         successMsg.textContent = 'Message sent successfully! We\'ll get back to you soon.';
    //         document.body.appendChild(successMsg);
    //         setTimeout(()=>successMsg.remove(),3000);
    //         this.reset();
    //     });
    // }
            // Add ripple animation keyframes
    const style = document.createElement('style');
        style.textContent = `
            @keyframes ripple {
                to {
                    transform: scale(4);
                    opacity: 0;
                }
            }
        `;
    document.head.appendChild(style);
    const fadeStyle = document.createElement('style');
    fadeStyle.textContent = `
    @keyframes fadeIn {
        from {opacity:0; transform: translate(-50%, -50%) scale(0.8);}
        to {opacity:1; transform: translate(-50%, -50%) scale(1);}
    }`;
    document.head.appendChild(fadeStyle);
    
// ==================== FAQ ====================

document.addEventListener('DOMContentLoaded', () => {
    const faqItems = document.querySelectorAll('.faq-section .faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        const answer = item.querySelector('.faq-answer');
        const icon = question.querySelector('.icon');

        question.addEventListener('click', () => {
            faqItems.forEach(otherItem => {
                if (otherItem !== item) {
                    const otherAnswer = otherItem.querySelector('.faq-answer');
                    const otherQuestion = otherItem.querySelector('.faq-question');
                    const otherIcon = otherQuestion.querySelector('.icon');

                    otherAnswer.classList.remove('show');
                    otherAnswer.style.maxHeight = 0;
                    otherQuestion.classList.remove('active');
                    if (otherIcon) otherIcon.classList.remove('rotate');
                }
            });

            const isActive = question.classList.contains('active');
            if (!isActive) {
                question.classList.add('active');
                answer.classList.add('show');
                answer.style.maxHeight = answer.scrollHeight + "px";
                if (icon) icon.classList.add('rotate');
            } else {
                question.classList.remove('active');
                answer.classList.remove('show');
                answer.style.maxHeight = 0;
                if (icon) icon.classList.remove('rotate');
            }
        });
    });
});

    // carusel block
const wrapper = document.querySelector('.carousel-wrapper');
const items = wrapper.querySelectorAll('.carousel-item-link');
const prevBtn = document.querySelector('.carousel-btn.prev');
const nextBtn = document.querySelector('.carousel-btn.next');

const itemWidth = items[0].offsetWidth + 20;

items.forEach(item => {
  const clone = item.cloneNode(true);
  wrapper.appendChild(clone);
});

let autoplayInterval = setInterval(autoScroll, 2000);

function autoScroll() {
  scrollNext();
}

function scrollNext() {
  if (wrapper.scrollLeft >= wrapper.scrollWidth / 2) {
    wrapper.scrollLeft = 0;
  }
  wrapper.scrollBy({ left: itemWidth, behavior: 'smooth' });
}

function scrollPrev() {
  if (wrapper.scrollLeft <= 0) {
    wrapper.scrollLeft = wrapper.scrollWidth / 2;
  }
  wrapper.scrollBy({ left: -itemWidth, behavior: 'smooth' });
}

nextBtn.addEventListener('click', scrollNext);
prevBtn.addEventListener('click', scrollPrev);

wrapper.addEventListener('mouseenter', () => clearInterval(autoplayInterval));
wrapper.addEventListener('mouseleave', () => {
  autoplayInterval = setInterval(autoScroll, 2000);
});
